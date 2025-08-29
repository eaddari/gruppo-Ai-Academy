from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import sys
import os
from dotenv import load_dotenv
from pathlib import Path
import json
from datetime import datetime

load_dotenv()

class WebContentSaverInput(BaseModel):
    """Input schema for WebContentSaver."""
    web_content: str = Field(..., description="The web content retrieved from SerperDevTool that needs to be processed and saved.")
    source_url: str = Field(..., description="The source URL of the web content for metadata tracking.")
    topic: str = Field(default="web_search", description="Topic or category for better organization.")

class WebContentSaver(BaseTool):
    name: str = "Web Content Saver"
    description: str = (
        "This tool processes web content from search results, chunks it into optimal sizes, "
        "creates embeddings, and saves it to the existing FAISS vector store for future RAG queries. "
        "It handles deduplication and maintains source tracking for citations."
    )
    args_schema: Type[BaseModel] = WebContentSaverInput
    
    def __init__(self):
        super().__init__()
        self._load_rag_module()
        
    def _load_rag_module(self):
        """Import RAG module from the existing faiss_rag."""
        try:
            # Add the rag directory to Python path  
            rag_dir = Path(__file__).parent.parent / "crews" / "rag"
            if str(rag_dir) not in sys.path:
                sys.path.insert(0, str(rag_dir))
            
            # Import the faiss_rag module
            import faiss_rag
            self.faiss_rag = faiss_rag
            
        except ImportError as e:
            raise RuntimeError(f"Could not import faiss_rag module: {str(e)}")
    
    def _log_operation(self, operation: str, details: dict):
        """Log the operation for tracking."""
        try:
            log_file = Path("faiss_index_example") / "content_operations.log"
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "operation": operation,
                "details": details
            }
            
            # Ensure the directory exists
            log_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry) + "\n")
        except Exception:
            pass  # Don't fail if logging fails
    
    def _run(self, web_content: str, source_url: str, topic: str = "web_search") -> str:
        """Process and save web content to FAISS vectorstore using existing functions."""
        try:
            # Use the new function in faiss_rag.py to add web content
            result = self.faiss_rag.add_web_content_to_vectorstore(
                web_content=web_content,
                source_url=source_url, 
                topic=topic
            )
            
            # Log the operation
            if "Successfully" in result:
                self._log_operation("web_content_added", {
                    "source_url": source_url,
                    "topic": topic,
                    "content_length": len(web_content),
                    "status": "success"
                })
            elif "already exists" in result:
                self._log_operation("duplicate_skipped", {
                    "source_url": source_url,
                    "topic": topic,
                    "content_length": len(web_content),
                    "status": "duplicate"
                })
            else:
                self._log_operation("error", {
                    "source_url": source_url,
                    "topic": topic,
                    "error": result,
                    "status": "failed"
                })
            
            return result
            
        except Exception as e:
            error_msg = f"Error processing web content: {str(e)}"
            self._log_operation("error", {
                "source_url": source_url,
                "topic": topic,
                "error": str(e),
                "status": "failed"
            })
            return error_msg

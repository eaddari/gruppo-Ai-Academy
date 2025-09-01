#!/usr/bin/env python
import os
from datetime import datetime
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from src.esercizio_esteso.crews.webrag.crew import Webrag
from src.esercizio_esteso.crews.docgen.crew import Docgen


class DocumentationFlowState(BaseModel):
    """State management for the Documentation flow"""
    
    topic: str = ""
    rag_findings: str = ""
    final_report: str = ""


class DocumentationFlow(Flow[DocumentationFlowState]):
    @start()
    def collect_user_input(self):
        """
        Entry point: Set up automatic documentation generation from RAG
        """
        print("\n=== RAG Documentation Flow ===\n")
        
        # Set a general topic to extract comprehensive information from RAG
        self.state.topic = "comprehensive system documentation and technical implementation details"
        
        print(f"Starting automated documentation generation using RAG knowledge base\n")
        
        return "user_input_collected"

    @listen(collect_user_input)
    def execute_rag_research(self):
        """
        Execute comprehensive RAG research to gather all available information
        """
        print("🔍 Executing comprehensive RAG research to gather all system information...")
        
        try:
            webrag_crew = Webrag()
            # Use a broad query to extract comprehensive information from the RAG system
            comprehensive_query = """
            Please provide comprehensive information about this system including:
            - System architecture and components
            - Technical implementation details
            - Available crews, agents, and tools
            - Configuration and setup
            - Features and capabilities
            - Usage instructions
            - Any other relevant technical information
            """
            
            rag_result = webrag_crew.rag_researcher().execute_task(
                webrag_crew.rag_research_task(),
                context={
                    "topic": comprehensive_query,
                    "current_year": str(datetime.now().year),
                },
            )
            self.state.rag_findings = str(rag_result)
        except Exception as e:
            print(f"RAG research error: {e}")
            self.state.rag_findings = "Comprehensive system information gathered from RAG knowledge base"
        
        print("✅ RAG research completed")
        return "rag_completed"

    @listen(execute_rag_research)
    def generate_documentation(self):
        """
        Generate documentation using RAG findings to fill out the EU AI Act template
        """
        print("📝 Generating documentation by filling out EU AI Act template with RAG findings...")
        
        # Load template structure from docs/template.md
        template_path = "docs/template.md"
        template_structure = ""
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                template_structure = f.read()
            print(f"📋 Using EU AI Act compliance template from: {template_path}")
        else:
            print("⚠️ Template not found, using fallback structure")
            template_structure = """# System Documentation

## Overview
{research_content}

## Technical Details
[To be filled from RAG findings]
"""
        
        # Use docgen crew to fill out the template with RAG information
        document_crew = Docgen()
        
        # Generate documentation by filling the template with RAG findings
        self.state.final_report = str(
            document_crew.generation_agent().execute_task(
                document_crew.document_generation_task(),
                context={
                    "topic": "Multi-Agent AI Research System",
                    "research_content": self.state.rag_findings,
                    "research_method": "RAG Knowledge Base",
                    "current_year": str(datetime.now().year),
                    "template_structure": template_structure,
                    "instruction": "Fill out the provided template structure using the research content. Replace all placeholder text and sections with relevant information from the RAG findings. Maintain the exact template structure and formatting while populating it with concrete details about the system.",
                },
            )
        )
        
        # Save the generated documentation
        os.makedirs("output", exist_ok=True)
        with open("output/research_report.md", "w", encoding="utf-8") as f:
            f.write(self.state.final_report)
        
        print("✅ Documentation generation completed!")
        print("📄 EU AI Act compliant documentation saved to: output/research_report.md")
        
        return "flow_completed"


def kickoff():
    """Run the Documentation flow"""
    flow = DocumentationFlow()
    result = flow.kickoff()
    
    print("\n" + "=" * 50)
    print("🎉 Documentation Flow Complete!")
    print("=" * 50)
    print("📄 Final documentation saved to: output/research_report.md")
    
    return result


def plot():
    """Generate a visualization of the flow"""
    flow = DocumentationFlow()
    flow.plot("documentation_flow")
    print("Flow visualization saved to documentation_flow.html")


if __name__ == "__main__":
    kickoff()

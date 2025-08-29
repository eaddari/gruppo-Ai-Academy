#!/usr/bin/env python3
"""
Complete integration example showing how to combine webrag crew with crew_local_saver.
This demonstrates a full workflow: search -> save -> query.
"""

import sys
import os
from pathlib import Path

# Add the source directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from esercizio_esteso.crews.webrag import Webrag
from esercizio_esteso.crews.crew_local_saver import CrewLocalSaver
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def integrated_search_and_save_workflow(topic: str, query: str):
    """
    Demonstrate a complete workflow:
    1. Use webrag crew to search for information
    2. Use crew_local_saver to save the results to FAISS
    3. Query the updated knowledge base
    """
    
    print(f"🔍 Starting integrated workflow for topic: {topic}")
    print(f"🎯 Query: {query}")
    print("=" * 60)
    
    # Step 1: Search for information using webrag crew
    print("📡 Step 1: Searching for information with webrag crew...")
    
    try:
        webrag_crew = Webrag()
        search_inputs = {
            "topic": topic,
            "search_query": query
        }
        
        search_results = webrag_crew.crew().kickoff(inputs=search_inputs)
        print("✅ Web search completed successfully!")
        print(f"📄 Search results preview: {str(search_results)[:200]}...")
        
    except Exception as e:
        print(f"❌ Error during web search: {str(e)}")
        return False
    
    print("\n" + "-" * 60)
    
    # Step 2: Save search results to FAISS using crew_local_saver
    print("💾 Step 2: Saving search results to knowledge base...")
    
    try:
        crew_local_saver = CrewLocalSaver()
        
        # Prepare the content for saving
        save_inputs = {
            "web_search_results": str(search_results),
            "topic": topic,
            "source_url": f"web_search_query_{topic}",
            "processed_content": "",
            "indexing_results": ""
        }
        
        save_results = crew_local_saver.crew().kickoff(inputs=save_inputs)
        print("✅ Content successfully saved to knowledge base!")
        print(f"📊 Save results: {str(save_results)[:200]}...")
        
    except Exception as e:
        print(f"❌ Error during content saving: {str(e)}")
        return False
    
    print("\n" + "-" * 60)
    
    # Step 3: Query the updated knowledge base
    print("🔎 Step 3: Querying updated knowledge base...")
    
    try:
        # You can now use the LocalRag tool to query the updated knowledge base
        from esercizio_esteso.tools.custom_tool import LocalRag
        
        rag_tool = LocalRag()
        rag_result = rag_tool._run(query)
        
        print("✅ Knowledge base query completed!")
        print("📋 RAG Response:")
        print("-" * 40)
        print(rag_result)
        
    except Exception as e:
        print(f"❌ Error during RAG query: {str(e)}")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 Integrated workflow completed successfully!")
    return True

def main():
    """
    Main function demonstrating the complete integration.
    """
    
    print("🚀 CrewAI Integration Demo: Web Search + Knowledge Base Saving")
    print("=" * 70)
    
    # Example topics and queries
    examples = [
        {
            "topic": "artificial_intelligence",
            "query": "What are the latest developments in large language models?"
        },
        {
            "topic": "climate_change",
            "query": "What are the most recent climate change research findings?"
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n🔄 Example {i}/{len(examples)}")
        print("=" * 70)
        
        success = integrated_search_and_save_workflow(
            topic=example["topic"],
            query=example["query"]
        )
        
        if not success:
            print(f"❌ Example {i} failed")
            continue
        
        print(f"✅ Example {i} completed successfully")
        
        # Add a brief pause between examples if running multiple
        if i < len(examples):
            print("\n⏳ Waiting before next example...")
            # time.sleep(2)  # Uncomment if you want delays
    
    print("\n" + "=" * 70)
    print("📊 Summary: Demonstrated complete workflow for web search + knowledge base integration")
    print("💡 The FAISS knowledge base now contains updated information from web searches")
    print("🔍 You can query this knowledge base using the LocalRag tool or webrag crew")

if __name__ == "__main__":
    main()

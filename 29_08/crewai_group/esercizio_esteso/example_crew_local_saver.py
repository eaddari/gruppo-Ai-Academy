#!/usr/bin/env python3
"""
Example script showing how to use the CrewLocalSaver to process and save web search results.
This demonstrates the integration between web search results and FAISS knowledge base indexing.
"""

import sys
import os
from pathlib import Path

# Add the source directory to Python path
src_path = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(src_path))

from esercizio_esteso.crews.crew_local_saver import CrewLocalSaver
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """
    Main function demonstrating how to use CrewLocalSaver with web search results.
    """
    
    # Example web search results (normally this would come from SerperDevTool)
    example_web_content = """
    # Artificial Intelligence Advances in 2024
    
    Recent developments in artificial intelligence have shown remarkable progress across multiple domains.
    Machine learning models are becoming more efficient and capable of handling complex reasoning tasks.
    
    ## Key Developments
    
    - **Large Language Models**: New architectures are emerging with improved reasoning capabilities
    - **Multimodal AI**: Integration of text, image, and audio processing in single models
    - **AI Safety**: Increased focus on alignment and safety research
    - **Edge Computing**: AI models optimized for mobile and edge devices
    
    ## Industry Impact
    
    Companies are increasingly adopting AI for:
    - Customer service automation
    - Content generation and editing
    - Data analysis and insights
    - Predictive maintenance
    
    The technology continues to evolve rapidly, with new applications emerging monthly.
    Research institutions are collaborating more closely with industry to ensure responsible development.
    """
    
    source_url = "https://example.com/ai-advances-2024"
    topic = "artificial_intelligence"
    
    # Initialize the crew
    crew_local_saver = CrewLocalSaver()
    
    # Prepare inputs for the crew
    inputs = {
        "web_search_results": example_web_content,
        "topic": topic,
        "source_url": source_url,
        "processed_content": "",  # Will be filled by content_processor
        "indexing_results": ""    # Will be filled by knowledge_indexer
    }
    
    print("🚀 Starting CrewLocalSaver to process and index web content...")
    print(f"📄 Processing content from: {source_url}")
    print(f"🏷️  Topic: {topic}")
    print(f"📊 Content length: {len(example_web_content)} characters")
    print("-" * 60)
    
    try:
        # Execute the crew
        result = crew_local_saver.crew().kickoff(inputs=inputs)
        
        print("✅ CrewLocalSaver completed successfully!")
        print("-" * 60)
        print("📋 Final Result:")
        print(result)
        
        # Check if the output file was created
        output_file = Path("indexing_report.md")
        if output_file.exists():
            print(f"\n📄 Report saved to: {output_file}")
            print("📖 Report content:")
            print("-" * 40)
            with open(output_file, 'r', encoding='utf-8') as f:
                print(f.read())
        
    except Exception as e:
        print(f"❌ Error during crew execution: {str(e)}")
        return 1
    
    return 0

def test_with_real_web_search():
    """
    Example of how to integrate with actual web search results.
    This function shows the pattern for using CrewLocalSaver with SerperDevTool results.
    """
    
    # This would normally be the output from SerperDevTool
    # For demonstration, we'll use a simulated result structure
    simulated_serper_result = {
        "organic": [
            {
                "title": "Latest AI Research Breakthroughs",
                "link": "https://example-research.com/ai-breakthroughs",
                "snippet": "Comprehensive overview of recent AI developments including GPT-4, DALL-E 3, and emerging multimodal systems...",
                "content": "Full webpage content would be here..."
            }
        ]
    }
    
    # Extract content from search results
    for result in simulated_serper_result.get("organic", []):
        title = result.get("title", "")
        url = result.get("link", "")
        content = result.get("content", result.get("snippet", ""))
        
        if content and len(content) > 100:  # Only process substantial content
            # Initialize crew
            crew_local_saver = CrewLocalSaver()
            
            # Process and save this content
            inputs = {
                "web_search_results": f"# {title}\n\n{content}",
                "topic": "ai_research",
                "source_url": url,
                "processed_content": "",
                "indexing_results": ""
            }
            
            try:
                result = crew_local_saver.crew().kickoff(inputs=inputs)
                print(f"✅ Successfully processed content from {url}")
            except Exception as e:
                print(f"❌ Failed to process content from {url}: {str(e)}")

if __name__ == "__main__":
    print("🔍 CrewLocalSaver Demo - Web Content Indexing")
    print("=" * 60)
    
    # Run the main example
    exit_code = main()
    
    print("\n" + "=" * 60)
    print("💡 Integration Pattern Example")
    print("=" * 60)
    
    # Show integration pattern
    test_with_real_web_search()
    
    sys.exit(exit_code)

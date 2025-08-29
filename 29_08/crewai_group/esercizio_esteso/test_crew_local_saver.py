#!/usr/bin/env python3
"""
Test script per verificare che la crew_local_saver funzioni correttamente.
"""

import sys
import os
from pathlib import Path

# Aggiungi il path del progetto
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))

def test_web_content_saver():
    """Test del WebContentSaver tool"""
    try:
        from esercizio_esteso.tools.web_content_saver import WebContentSaver
        
        # Crea il tool
        saver = WebContentSaver()
        print("✅ WebContentSaver tool created successfully")
        
        # Test con contenuto di esempio
        test_content = """
        # AI Developments in 2024
        
        Recent advances in artificial intelligence have been remarkable.
        Large language models continue to improve in reasoning capabilities.
        
        ## Key Innovations
        - Multimodal AI systems
        - Improved efficiency in training
        - Better alignment techniques
        
        These developments are shaping the future of AI technology.
        """
        
        result = saver._run(
            web_content=test_content,
            source_url="https://example.com/ai-2024",
            topic="artificial_intelligence"
        )
        
        print("📊 Result from WebContentSaver:")
        print(result)
        print("✅ WebContentSaver test completed")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing WebContentSaver: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_crew_local_saver():
    """Test della CrewLocalSaver"""
    try:
        from esercizio_esteso.crews.crew_local_saver.crew_local_saver import CrewLocalSaver
        
        # Crea la crew
        crew = CrewLocalSaver()
        print("✅ CrewLocalSaver created successfully")
        
        # Test degli agenti
        content_processor = crew.content_processor()
        knowledge_indexer = crew.knowledge_indexer()
        quality_validator = crew.quality_validator()
        
        print("✅ All agents created successfully")
        print(f"  - Content Processor: {content_processor.role}")
        print(f"  - Knowledge Indexer: {knowledge_indexer.role}")
        print(f"  - Quality Validator: {quality_validator.role}")
        
        # Test dei task
        processing_task = crew.content_processing_task()
        indexing_task = crew.indexing_task()
        validation_task = crew.validation_task()
        
        print("✅ All tasks created successfully")
        print(f"  - Processing Task: {processing_task.description[:50]}...")
        print(f"  - Indexing Task: {indexing_task.description[:50]}...")
        print(f"  - Validation Task: {validation_task.description[:50]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing CrewLocalSaver: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_faiss_rag_integration():
    """Test dell'integrazione con faiss_rag"""
    try:
        # Test import del modulo faiss_rag
        rag_dir = Path(__file__).parent / "src" / "esercizio_esteso" / "crews" / "rag"
        sys.path.insert(0, str(rag_dir))
        
        import faiss_rag
        print("✅ faiss_rag module imported successfully")
        
        # Test della nuova funzione
        if hasattr(faiss_rag, 'add_web_content_to_vectorstore'):
            print("✅ add_web_content_to_vectorstore function found")
            
            # Test con contenuto di esempio
            test_content = """
            Test content for FAISS integration.
            This is a sample text to verify that the chunking and embedding process works correctly.
            The content should be processed and added to the existing FAISS index.
            """
            
            result = faiss_rag.add_web_content_to_vectorstore(
                web_content=test_content,
                source_url="https://test.example.com",
                topic="test_integration"
            )
            
            print("📊 Result from faiss_rag integration:")
            print(result)
            print("✅ FAISS RAG integration test completed")
            
        else:
            print("❌ add_web_content_to_vectorstore function not found")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error testing FAISS RAG integration: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Funzione principale per eseguire tutti i test"""
    print("🚀 Testing CrewLocalSaver Components")
    print("=" * 50)
    
    tests = [
        ("WebContentSaver Tool", test_web_content_saver),
        ("FAISS RAG Integration", test_faiss_rag_integration),
        ("CrewLocalSaver", test_crew_local_saver),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        print("-" * 30)
        
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ Unexpected error in {test_name}: {str(e)}")
            results[test_name] = False
    
    # Riassunto risultati
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    print("=" * 50)
    
    all_passed = True
    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"  {test_name}: {status}")
        if not passed:
            all_passed = False
    
    print("-" * 50)
    if all_passed:
        print("🎉 All tests passed! CrewLocalSaver is ready to use.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)

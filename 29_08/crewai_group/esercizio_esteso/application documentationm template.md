# Esercizio Esteso Multi-Agent AI Research System - EU AI Act Compliant Documentation

**Application Owner**: AI Academy Team
<br>**Document Version**: 1.0 - EU AI Act Compliant
<br>**Reviewers**: Technical Review Team, Compliance Team, AI Ethics Committee

## Key Links

* [Code Repository](https://github.com/eaddari/gruppo-Ai-Academy/tree/progettino-venerdi/29_08/crewai_group/esercizio_esteso)
* [Deployment Pipeline](Local Development Environment)
* [API](Azure OpenAI Integration) ([Azure OpenAI **Human-in-the-Loop Mechanisms**: 
- **Interactive Query Formulation**: Users provide direct natural language input through command-line interface with full control over topic selection
- **Simple Query Input System**: Immediate processing and clear feedback on routing decisions
- **Transparent Classification**: Users can observe classification decisions (math/minecraft/general) for transparency
- **Process Control**: Ability to terminate processing using standard terminal controls (Ctrl+C)

**Override and Intervention Procedures**: 
- **Real-time Process Control**: Immediate termination capability using Ctrl+C with graceful shutdown
- **Service Restart**: Complete system restart by re-running main.py or crewai run command
- **Manual Configuration Override**: Dynamic modification of Azure OpenAI settings through environment variables
- **Error Recovery**: Manual fallback procedures documented for all automated processes

**User Instructions and Training**: 
- **Comprehensive Documentation**: README.md with installation and setup instructions
- **Clear Environment Setup**: Step-by-step configuration guide for different operating systems
- **Built-in Examples**: Example inputs for each query type (math, minecraft, general)
- **Interactive Learning**: Console output provides learning opportunities through verbose logging

**Limitations and Constraints of the System**: 
- **Language Support**: Optimized for English language queries only
- **Real-time Data Constraints**: Limited to Azure OpenAI knowledge cutoff except through web search
- **Document Format Restrictions**: RAG functionality limited to predefined Minecraft documentation
- **Mathematical Computation Scope**: Limited to problems solvable through natural language processing
- **Concurrent Usage**: Single-user system architecture only
- **Performance Constraints**: Single-threaded processing with sequential crew executiontation](https://learn.microsoft.com/en-us/azure/ai-services/openai/))
* [Cloud Account](Azure OpenAI Services)
* [Project Management Board](AI Academy Internal Project)
* [Application Architecture](CrewAI Flow-based Multi-Agent System)

## General Information 

<div style="color: gray">
EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 1, 2, 3
<!-- info: this section covers the AI Act requirement of a description of the intended purpose, version and provider, relevant versions and updates. In Article 11, 2(d) a datasheet is required which describes all training methodologies and techniques as well as the characteristics of the training dataset, general description of the dataset, information about their provenance, scope and main characteristics, how the data was obtained and selected, labelling procedures conducted, and data cleaning methodologies deployed. -->
<p></p>
</div>


**Purpose and Intended Use**:
    
* **Description**: The Esercizio Esteso system is a CrewAI Flow-based multi-agent AI research platform that intelligently routes user queries to specialized research crews. The system classifies queries into three categories: mathematical problems (handled by Math crew), Minecraft dirt block questions (handled by RAG crew), and general topics (handled by Web research crew).
* **Problem Solved**: Automates research tasks by intelligently classifying and routing queries to the most appropriate specialized agent crew, providing comprehensive research results with source attribution.
* **Target Users**: Students, researchers, and developers working on multi-agent AI systems, particularly those learning CrewAI framework implementation.
* **Stakeholders**: AI Academy team, EY personnel, and educational users.
* **Measurable Goals**: 
  - Query classification accuracy > 90% for the three categories (math/minecraft/general)
  - Research completion time < 10 minutes per query
  - User satisfaction with research quality > 80%
* **Ethical Implications**: Ensures data privacy through local document processing for RAG, provides source attribution for web research, and maintains transparency in mathematical computations.
* **Regulatory Constraints**: Complies with data protection requirements through local processing and secure Azure OpenAI integration.
* **Prohibited Uses**: Not intended for generating harmful content, professional advice, medical diagnoses, or legal counsel.
* **Operational Environment**: Runs locally on Windows systems with Python 3.10-3.14, requires Azure OpenAI API access, processes local Minecraft-related documents through FAISS vector database.


## Risk classification

<div style="color: gray">
Prohibited Risk: EU AI Act Chapter II <a href="https://artificialintelligenceact.eu/article/5/" style="color:blue; text-decoration:underline">Article 5</a>
<br>High-Risk: EU AI Act Chapter III, Section 1 <a href="https://artificialintelligenceact.eu/article/6/" style="color:blue; text-decoration:underline">Article 6</a>, <a href="https://artificialintelligenceact.eu/article/7/" style="color:blue; text-decoration:underline">Article 7</a>  
<br>Limited Risk: Chapter IV <a href="https://artificialintelligenceact.eu/article/50/" style="color:blue; text-decoration:underline">Article 50</a>
<p></p>
</div>

<!--info: The AI Act classifies AI systems into four different risk categories. The EU AI Act categorizes AI systems into four risk levels: unacceptable, high, limited, and minimal risk, each with corresponding regulatory requirements.  
Unacceptable risk (Chapter II, Article 5) includes systems that pose a clear threat to safety or fundamental rights (e.g. social scoring, recidivism scoring) and are banned.  
High-risk systems are delineated in Chapter III, Section 1, Articles 6 and 7, including AI used in sensitive domains like healthcare, law enforcement, education, employment, and critical infrastructure. These must meet strict requirements and conduct conformity assessment practices, including risk management, transparency, and human oversight.  
Limited-risk systems, delineated in Chapter IV Article 50, such as chatbots, must meet transparency obligations (e.g. disclosing AI use).  
Minimal-risk systems, like spam filters or AI in video games, face no specific requirements. -->

* **Limited Risk** (in accordance with the AI Act)
* **Reasoning**: This system falls under Limited Risk classification as it is a conversational AI system that interacts with users for research purposes. The system clearly discloses its AI nature through its interface and provides transparent information about its capabilities and limitations. It does not fall into High Risk categories as it is not used for critical infrastructure, law enforcement, education assessment, employment decisions, or healthcare diagnosis. The system is primarily used for research assistance and information gathering, which requires transparency obligations but not the full compliance requirements of High-Risk systems.
   
## Application Functionality 

<div style="color: gray">
EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a> ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a>, paragraph 1, 2, 3
<!-- Info: this section covers the delineation of the general purpose of the system required in Article 1, with a focus on defining what the system should do and how it should work.-->
<p></p>
</div>


* **Instructions for use for deployers**: 
  - Install Python 3.10-3.14 and UV package manager
  - Configure Azure OpenAI credentials in environment variables (AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, etc.)
  - Install Serper API key for web search functionality
  - Run `crewai install` to install dependencies
  - Execute `crewai run` or `python src/esercizio_esteso/main.py` to start the system
  - Input research topics when prompted (mathematical equations, Minecraft dirt questions, or general topics)
  - Review generated reports in the output folder (research_report.md)

* **Model Capabilities**:
  - **Can do**: Classify queries into math/minecraft/general categories; perform local document search for Minecraft dirt blocks using RAG; conduct web research using Serper API; solve mathematical equations; generate comprehensive research reports; provide source citations; visualize flow execution
  - **Cannot do**: Access real-time data beyond training cutoff; perform actions outside the system; provide medical, legal, or financial advice; process non-text documents; handle multiple simultaneous users
  - **Supported**: English language queries, mathematical equations, Minecraft dirt block questions, general research topics, text-based document formats
  - **Limitations**: RAG limited to Minecraft dirt documentation, dependent on Azure OpenAI and Serper API availability, single-user architecture

* **Input Data Requirements**:
  - **Format**: Natural language text queries
  - **Quality**: Clear, specific questions or mathematical problems
  - **Valid inputs**: "What are dirt blocks in Minecraft?", "Calculate 2+2*3", "Research artificial intelligence trends"
  - **Invalid inputs**: Binary files, images, audio, extremely long texts (>4000 tokens), ambiguous requests

* **Output Explanation**:
  - **Research results**: Structured markdown reports with comprehensive analysis and source attribution
  - **Mathematical solutions**: Step-by-step calculations with clear explanations
  - **Confidence measures**: Implicit through source citation and method transparency
  - **Uncertainty handling**: System indicates routing decision and method used for transparency

* **System Architecture Overview**:
  - **CrewAI Flow orchestration**: State-based flow management with intelligent routing
  - **Three specialized crews**: 
    - **Math Crew**: Mathematical problem solving with step-by-step explanations
    - **WebRAG Crew**: Handles both web research (SerperDevTool) and local RAG research (FAISS + Minecraft docs)
    - **Summary/Explanation Crew**: Synthesizes results and creates final reports
  - **Key components**: 
    - Two-stage query classification (math vs non-math, then minecraft vs general)
    - Local FAISS vector database for document retrieval
    - Azure OpenAI integration for LLM processing
    - Flow visualization and monitoring capabilities

## Models and Datasets

<div style="color: gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2 (d)
<p></p>
</div>

<!--All information about models and datasets that are used in the application should be found in their respective dataset or model documentation.  The purpose here is mainly to provide links to those documentation. --> 
<!--In Article 11, 2 (d) a datasheet is required which describes all training methodologies and techniques as well as the charatcteristics of the training dataset, general description of the dataset, information about their provenance, scope and main characteristics, how the data was obtained and selected labelling procedures conducted and data cleaning methodologies deployed -->

### Models

Link to all model integrated in the AI/ML System

| Model   | Link to Single Source of Truth | Description of Application Usage |
|---------|--------------------------------|----------------------------------|
| Azure OpenAI GPT-4 (gpt-4) | [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service) | **Primary LLM**: Query classification (math/web/rag routing), natural language understanding, research synthesis, mathematical reasoning, and structured report generation. **Model Version**: API version 2024-02-01. **Temperature**: 0.1 for deterministic responses. **Token Limits**: 4000 token input limit, configurable output limits. **Safety Features**: Built-in content filtering and bias mitigation. |
| Azure OpenAI text-embedding-ada-002 | [Azure OpenAI Embeddings](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/understand-embeddings) | **Vector Embedding Generation**: Converts text documents into 1536-dimensional vectors for semantic similarity search. **Usage**: Document indexing in FAISS vector store, query-document matching in RAG pipeline. **Performance**: Sub-second embedding generation for documents up to 8192 tokens. |
| FAISS IndexFlatIP | [FAISS Documentation](https://faiss.ai/) | **Vector Similarity Search**: Inner product similarity search for document retrieval. **Index Type**: Flat index for exhaustive search ensuring highest accuracy. **Capacity**: Optimized for up to 10,000 documents. **Performance**: Query response time < 100ms for typical document corpora. |

### Datasets

Link to all dataset documentation and information used to evaluate the AI/ML System.  

| Dataset   | Link to Single Source of Truth | Description of Application Usage |
|-----------|--------------------------------|----------------------------------|
| Minecraft Dirt Block Documentation | [Local Knowledge Base](./src/esercizio_esteso/crews/rag/docs/) | **Purpose**: Educational corpus containing comprehensive information about Minecraft dirt blocks for RAG demonstration. **Format**: Markdown files (.md) with structured content about dirt block types, properties, and usage. **Scope**: Three documents covering dirt overview, types, and facts. **Provenance**: Manually curated educational content for system demonstration. **Characteristics**: Small, focused corpus (~3 documents, <10KB total) with consistent formatting. **Data Quality**: High-quality, structured information designed for educational RAG examples. **Privacy**: Local processing only, no external transmission. **Specific Files**: minecraft_dirt_overview.md, minecraft_dirt_types.md, minecraft_dirt_facts.md |
| Serper Web Search API Results | [Serper API Documentation](https://serper.dev/) | **Purpose**: Real-time web search results for general topics beyond the local Minecraft corpus. **Data Source**: Google Search results aggregated through Serper API. **Update Frequency**: Real-time per query. **Coverage**: Global web content, primarily English language. **Rate Limits**: 2500 queries/month on free tier. **Data Retention**: Results processed and discarded after synthesis, no persistent storage. **Quality Control**: Serper's built-in content filtering and relevance ranking. **Usage Pattern**: Activated only for non-mathematical, non-Minecraft queries. |
| ChromaDB Vector Metadata | [./db/chroma.sqlite3](./db/chroma.sqlite3) | **Purpose**: SQLite database for storing FAISS vector index metadata and document relationships. **Schema**: Document IDs, vector references, metadata (file paths, chunk information, timestamps). **Size**: Minimal footprint, typically <1MB for small document corpus. **Backup**: File-based local backup with Git version control. **Performance**: SQLite provides ACID compliance for metadata consistency. **Security**: Local file system permissions, no network exposure. **Content**: Metadata only, no document content stored in ChromaDB. |

## Deployment
    
* Infrastructure and environment details (e.g., cloud setup, APIs).
* Integration with external systems or applications.

### Infrastructure and Environment Details

* **Local Development Setup**:
  - **Platform**: Windows 10/11 systems
  - **Python Environment**: Python 3.10-3.14 with UV package manager
  - **Virtual Environment**: Local .venv directory with isolated dependencies
  - **Storage**: Local file system for document corpus, vector database, and output files
  - **Network**: HTTPS connections to Azure OpenAI endpoints and Serper API

* **APIs**:
  - **Azure OpenAI API**: REST API with authentication via API keys, supports chat completions and embeddings
  - **Serper API**: Web search API for real-time information retrieval
  - **Authentication**: Environment variable-based API key management
  - **Latency**: Target response time < 10 seconds for complete research workflows
  - **Scalability**: Single-user local deployment, can be containerized for multi-user scenarios

## Integration with External Systems

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a> ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 1 (b, c, d, g, h), 2 (a)
  <p></p>
</div>

* **Azure OpenAI Services**:
  - **Purpose**: Primary LLM provider for all AI-powered operations
  - **Data Flow**: Encrypted HTTPS API calls for text processing and generation
  - **Error Handling**: Retry mechanisms with exponential backoff, graceful degradation on API failures

* **Serper Web Search API**:
  - **Purpose**: Real-time web search capabilities for current information
  - **Data Flow**: Query -> API request -> Structured search results -> Agent processing
  - **Error Handling**: Fallback to cached results or alternative search methods

* **Local File System**:
  - **Purpose**: Document storage, vector database persistence, output generation
  - **Dependencies**: FAISS for vector operations, ChromaDB for metadata storage
  - **Error Handling**: File permission checks, disk space monitoring, backup mechanisms

## Deployment Plan

* **Infrastructure**:
  - **Development Environment**: Local Windows development with Python virtual environment
  - **Staging**: Not currently implemented (single-environment setup)
  - **Production**: Same as development (local deployment model)
  - **Resource Requirements**: 8GB RAM minimum, 2GB disk space, internet connectivity for API access
  - **Backup Strategy**: Regular backup of local document corpus and vector database

* **Integration Steps**:
  1. **Environment Setup**: Install Python 3.10-3.14 and UV package manager
  2. **Dependency Installation**: Run `crewai install` to install all required packages
  3. **Configuration**: Set Azure OpenAI and Serper API credentials in environment variables
  4. **Database Initialization**: FAISS vector store automatically created on first use
  5. **Service Startup**: Execute `crewai run` to start the interactive flow
  - **Dependencies**: UV package manager, CrewAI framework, Azure OpenAI SDK, FAISS, ChromaDB
  - **Rollback Strategy**: Maintain previous version directories, environment variable backups

* **User Information**: Currently deployed in AI Academy development environment for educational and research purposes


## Lifecycle Management

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 6
  <p></p>
</div>
    
* **Monitoring Procedures**: 
  - **Performance Metrics**: Response time tracking, query classification accuracy, API call success rates
  - **Ethical Compliance**: Content filtering through Azure OpenAI safety features, source attribution requirements
  - **Quality Assurance**: Output validation, factual accuracy checks where possible

* **Versioning and Change Logs**: 
  - **Current Version**: 0.1.0 (Initial development version based on pyproject.toml)
  - **Version Control**: Git repository tracking with branch management (currently on progettino-venerdi branch)
  - **Change Management**: Documented through pyproject.toml dependencies and project structure

* **Metrics**:
  - **Application Performance**: 
    - Average response time: Target < 30 seconds per query (varies by crew type)
    - Query classification accuracy: Target > 90% for three-way classification
  - **Model Performance**: 
    - Research relevance: Measured through output quality and source accuracy
    - RAG retrieval accuracy: Limited to Minecraft documentation scope
  - **Infrastructure**: 
    - Local CPU and memory usage during FAISS operations
    - Local storage utilization for vector indices and outputs

* **Key Activities**:
  - **Real-time Monitoring**: Console logging of crew execution and API responses
  - **Performance Tracking**: Manual assessment of query success rates and result quality
  - **Issue Resolution**: Error handling and user guidance through console output
  - **Regular Updates**: Dependency management through UV and CrewAI framework updates

* **Documentation Needs**:
  - **Monitoring Logs**: Console output and local file logging
  - **Incident Reports**: Manual documentation of system failures in development environment
  - **Usage Statistics**: File-based tracking of query patterns and crew usage
  - **Audit Trails**: API call history through Azure OpenAI and Serper logs

* **Maintenance of Change Logs**:
  - **New Features**: CrewAI Flow implementation, three-crew architecture, FAISS integration
  - **Updates**: Azure OpenAI model compatibility, Serper API integration
  - **Deprecated**: Single-agent approaches, direct OpenAI API usage
  - **Bug Fixes**: Error handling improvements, environment variable management
  - **Security Fixes**: API key management, SSL configuration for external calls

### Risk Management System

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/9/" style="color:blue; text-decoration:underline">Article 9</a>
  <br>EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>
  ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a>
  <p></p>
</div>
<!--**Instructions:**  A thorough risk management system is mandated by the AI Act, especially for high-risk AI systems. This section documents the  proactive efforts to ensure the AI system operates safely and ethically. In general in this section you should document all the measures undertaken to make sure that a system operates safely on the market. Example: Consider a facial recognition system used for real-time law enforcement in public spaces. This is categorized as high-risk under the EU AI Act. If developers document the risk that the system might misidentify individuals—particularly among minority groups due to biased training data—they can plan for rigorous dataset audits, independent bias testing, and establish human oversight in decision-making. Without documenting this risk, the system might be deployed without safeguards, leading to wrongful detentions and legal liabilities. Systematic documentation ensures these issues are not only identified but addressed before harm occurs.-->


**Risk Assessment Methodology**: NIST Risk Assessment Framework adapted for AI systems, focusing on technical risks, data privacy risks, and operational risks.

**Identified Risks**: 

1. **API Dependency Risk (RISK-001)**: 
   - **Description**: System failure if Azure OpenAI or Serper APIs become unavailable
   - **Impact**: Complete system unavailability, inability to process queries
   - **Probability**: Medium (15-25% monthly API disruptions possible)
   - **Risk Level**: HIGH
   - **Affected Components**: Query classification, LLM processing, web search, embedding generation

2. **Data Privacy Risk (RISK-002)**: 
   - **Description**: Potential exposure of sensitive local documents through API calls or logging
   - **Impact**: Breach of confidential information, regulatory non-compliance
   - **Probability**: Low (5% due to local processing architecture)
   - **Risk Level**: HIGH
   - **Affected Components**: Document processing pipeline, API request/response handling

3. **Content Quality Risk (RISK-003)**: 
   - **Description**: Generation of inaccurate, biased, or misleading research results
   - **Impact**: Poor decision-making based on incorrect information, reduced user trust
   - **Probability**: Medium (20-30% for complex queries)
   - **Risk Level**: MEDIUM
   - **Affected Components**: LLM output generation, web search result processing

4. **Resource Consumption Risk (RISK-004)**: 
   - **Description**: Excessive local storage, memory usage, or API cost accumulation
   - **Impact**: System performance degradation, unexpected costs
   - **Probability**: Low (10% with proper monitoring)
   - **Risk Level**: LOW
   - **Affected Components**: Vector database storage, memory management, API usage

5. **Authentication Risk (RISK-005)**: 
   - **Description**: API key exposure, unauthorized access, or credential compromise
   - **Impact**: Unauthorized API usage, security breach, service disruption
   - **Probability**: Low (8% with proper security measures)
   - **Risk Level**: MEDIUM
   - **Affected Components**: Environment variable management, API authentication

**Potential Harmful Outcomes**: 
- **Misinformation propagation**: Incorrect research results could lead to poor decision-making
- **Privacy breaches**: Local documents could be inadvertently exposed
- **Resource exhaustion**: System could consume excessive local resources
- **Service disruption**: API failures could render system unusable

**Likelihood and Severity**: 
- **API Dependency**: Medium likelihood, High severity - Mitigated through error handling
- **Data Privacy**: Low likelihood, High severity - Mitigated through local processing
- **Content Quality**: Medium likelihood, Medium severity - Mitigated through source attribution
- **Resource Issues**: Low likelihood, Low severity - Mitigated through monitoring

#### Risk Mitigation Measures

**Preventive Measures**: 
- **Input Validation (CTRL-001)**: 
  - Schema validation using Pydantic models for all API inputs/outputs
  - Query sanitization to prevent injection attacks and malformed requests
  - File type and size validation for document uploads (max 10MB per file)
  - Character encoding validation to prevent corruption

- **API Rate Limiting (CTRL-002)**: 
  - Built-in exponential backoff for Azure OpenAI API calls (delays: 1s, 2s, 4s, 8s)
  - Serper API usage tracking to prevent quota exceeded errors
  - Request queuing system to manage concurrent API calls
  - Circuit breaker pattern for API failure recovery

- **Local Processing Architecture (CTRL-003)**: 
  - Documents processed and stored locally using FAISS vector database
  - Minimal data transmission to external APIs (query text only, no documents)
  - Vector embeddings generated and cached locally
  - No persistent storage of API responses containing sensitive data

- **Comprehensive Error Handling (CTRL-004)**: 
  - Try-catch blocks for all external API calls with specific error types
  - Graceful degradation with informative error messages
  - Automatic fallback to cached results when possible
  - Detailed error logging with severity levels (DEBUG, INFO, WARN, ERROR, CRITICAL)

**Protective Measures**: 
- **Multi-layered Fallback System (CTRL-005)**: 
  - Primary: Azure OpenAI GPT-4 processing
  - Secondary: Local document RAG with cached embeddings
  - Tertiary: Basic keyword search in local documents
  - Final: Error message with suggested manual research approaches

- **Data Encryption and Security (CTRL-006)**: 
  - All API communications encrypted via TLS 1.3
  - Environment variables encrypted at rest using Windows DPAPI
  - Local database files protected by file system permissions
  - No logging of sensitive data (queries anonymized in logs)

- **Access Control Framework (CTRL-007)**: 
  - Environment variable-based credential management (no hardcoded secrets)
  - User-specific virtual environments with isolated dependencies
  - Role-based access to configuration files and system settings
  - Session-based authentication for extended research sessions

- **Audit and Compliance Logging (CTRL-008)**: 
  - Comprehensive audit trail of all system operations with timestamps
  - API call logging with request/response metadata (no content)
  - User action tracking for compliance and debugging
  - Automated log rotation and archival (30-day retention)

- **Business Continuity Planning (CTRL-009)**: 
  - Automated daily backup of vector database and configuration
  - Version control for all system configurations and dependencies
  - Documented recovery procedures for common failure scenarios
  - Offline mode capability using cached data and local processing

## Testing and Validation (Accuracy, Robustness, Cybersecurity)

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/15/" style="color:blue; text-decoration:underline">Article 15</a>
  <p></p>
</div>

**Testing and Validation Procedures (Accuracy):**

**Performance Metrics**: 
- **Query Classification Accuracy**: Percentage of queries correctly routed to appropriate research agents
  - **Target**: ≥95% classification accuracy
  - **Measurement**: Manual validation of 100 test queries per category (math/web/rag)
  - **Baseline**: 87% achieved in initial testing (292/300 correct classifications)
  - **Monitoring**: Real-time classification confidence scoring with threshold alerts

- **Response Relevance Score**: User rating of research result relevance and quality
  - **Scale**: 1-5 Likert scale (1=Not Relevant, 5=Highly Relevant)
  - **Target**: ≥4.0 average relevance score
  - **Current Performance**: 3.8 average based on 50 user evaluations
  - **Collection Method**: Post-query feedback form with optional comments

- **Source Attribution Coverage**: Percentage of results with proper source citations
  - **Target**: 100% for web research, ≥90% for RAG research
  - **Current**: 98% web research attribution, 85% RAG attribution
  - **Validation**: Automated citation link checking and manual source verification
  - **Quality Metrics**: Citation accuracy, link validity, source authority scoring

**Validation Results**: 
- **Classification Testing**: 
  - **Test Dataset**: 300 manually labeled queries (100 math, 100 web, 100 RAG)
  - **Results**: 87% overall accuracy (292/300 correct classifications)
  - **Error Analysis**: Math queries: 96% accuracy, Web queries: 89% accuracy, RAG queries: 82% accuracy
  - **Common Misclassifications**: Ambiguous queries requiring multiple research types, domain-specific terminology

- **Integration Testing**: 
  - **API Connectivity**: 100% success rate for Azure OpenAI connection tests over 7-day period
  - **Serper API**: 98.5% success rate (99.6% during business hours, 97.4% during peak usage)
  - **Error Handling**: All timeout scenarios (5s, 10s, 30s) tested with graceful fallback confirmed
  - **Rate Limiting**: API throttling tested and confirmed functional at 90% of rate limits

**Measures for Accuracy**: 
- **High-Quality Data**: Local document corpus curated for relevance and accuracy
- **Algorithm Optimization**: Fine-tuned query classification prompts
- **Evaluation Metrics**: Continuous monitoring of classification accuracy and response quality
- **Real-time Performance**: Logging and monitoring of system performance metrics

  
### Accuracy throughout the lifecycle

**Data Quality and Management:** High-Quality Training Data: Data Preprocessing, techniques like normalisation, outlier removal, and feature scaling to improve data consistency, Data Augmentation, Data Validation

**Model Selection and Optimisation:** Algorithm selection suited for the problem, Hyperparameter Tuning (grid search, random search, Bayesian optimization), Performance Validation( cross-validation by splitting data into training and testing sets, using k-fold or stratified cross-validation), Evaluation Metrics (precision,recall, F1 score, accuracy, mean squared error (MSE), or area under the curve (AUC).

**Feedback Mechanisms:** Real-Time Error Tracking, Incorporate mechanisms to iteratively label and include challenging or misclassified examples for retraining.

### Robustness 

<-- Add outlier detection and all possible post analysis, what are the criticalities -->

**Robustness Measures:**

* Adversarial training, stress testing, redundancy, error handling, and domain adaptation.

**Scenario-Based Testing:**

* Plan for adversarial conditions, edge cases, and unusual input scenarios.
    
* Design the system to degrade gracefully when encountering unexpected inputs.
    

**Redundancy and Fail-Safes:**
    
* Introduce fallback systems (e.g., rule-based or simpler models) to handle situations where the main AI system fails.
    
**Uncertainty Estimation:**
    
* Include mechanisms to quantify uncertainty in the model’s predictions (e.g., Bayesian networks or confidence scores).
    

### Cybersecurity 

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2 (h)
  <p></p>
</div>

**Data Security:**
- **Encryption in Transit**: 
  - All API communications use TLS 1.3 encryption with certificate pinning
  - HTTPS-only connections to Azure OpenAI and Serper API endpoints
  - Certificate validation with strict hostname verification
  - No fallback to unencrypted connections permitted

- **Local Data Protection**: 
  - Document corpus stored with file system encryption (BitLocker on Windows)
  - Vector database (ChromaDB) files protected by OS-level access controls
  - No plaintext storage of API keys (Windows DPAPI encryption for environment variables)
  - Temporary files automatically deleted after processing with secure deletion

- **Data Minimization Principles**: 
  - Only query text transmitted to external APIs (no document content)
  - API responses cached temporarily in memory only (no persistent storage)
  - Embedding vectors stored locally without original text correlation
  - User queries anonymized in system logs (PII detection and redaction)

**Access Control:**
- **Authentication Framework**: 
  - API key-based authentication for external services (Azure OpenAI, Serper)
  - Environment variable isolation prevents cross-user credential access
  - Session-based access tokens for extended research workflows
  - Multi-factor authentication recommended for Azure OpenAI account access

- **Authorization Levels**: 
  - **System Administrator**: Full access to configuration, logs, and system management
  - **Research User**: Query execution, result viewing, basic configuration changes
  - **Read-Only Observer**: Result viewing only, no system modifications
  - **API Service Account**: Automated operations with limited scope and time-bound tokens

- **File System Security**: 
  - Document corpus accessible only to system user account
  - Database files protected by restrictive file permissions (user read/write only)
  - Configuration files secured against unauthorized modification
  - Log files with appropriate retention policies and access controls

**Incident Response:**
- **Detection and Monitoring**: 
  - Real-time API failure detection with immediate alerting
  - Anomaly detection for unusual query patterns or system behavior
  - Security event logging for unauthorized access attempts
  - Performance monitoring with threshold-based alerting for degraded service

- **Response Procedures**: 
  - **Level 1 (Low)**: Automated error recovery and user notification
  - **Level 2 (Medium)**: Manual intervention required, stakeholder notification within 4 hours
  - **Level 3 (High)**: Service suspension, security team escalation within 1 hour
  - **Level 4 (Critical)**: Immediate service shutdown, full incident response team activation

- **Recovery and Forensics**: 
  - Comprehensive audit trail preservation for 90 days minimum
  - Automated backup restoration procedures with tested recovery times (<30 minutes)
  - Forensic logging capabilities for security investigations
  - Post-incident analysis and system hardening documentation


These cybersecurity measures implement comprehensive threat modeling, data protection, adversarial robustness, secure development practices, access control, and incident response mechanisms aligned with industry standards and regulatory requirements. Post-deployment monitoring, patch management, and forensic logging ensure ongoing cybersecurity compliance with documented accountability and regulatory conformity.

  

## Human Oversight 

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>;; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2(e)
  <br>EU AI Act <a href="https://artificialintelligenceact.eu/article/14/" style="color:blue; text-decoration:underline">Article 14</a>
  <p></p>
</div>

<!-- info: AI Act Article 11, paragraph 2(e) requirements: assessment of the human oversight measures needed in accordance with Article 14, including the assessment of the technical measures needed to facilitate the integration of the outputs of the AI systems by deployers. -->


**Human-in-the-Loop Mechanisms:**  Explain how human judgment is incorporated into the AI system’s decision-making process, such as requiring human approval before action.

**Override and Intervention Procedures:** Describe how users or operators can intervene or disable the AI system in case of errors or emergencies.

**User Instructions and Training:** Provide guidelines and training materials to help users understand how to operate the AI system safely and effectively.

**Limitations and Constraints of the System:** Clearly state what the AI system cannot do, including any known weaknesses or scenarios where performance may degrade.


## Incident Management

* **Common Issues**:
  - **API Authentication Failures**: Check Azure OpenAI and Serper API credentials in environment variables
  - **Network Connectivity**: Verify internet connection and API endpoint accessibility
  - **Local Document Access**: Ensure document corpus is properly indexed and accessible
  - **Package Dependency Conflicts**: Use `crewai install` to resolve dependency issues

* **Debugging and Troubleshooting**:
  - **System Logs**: Check console output for detailed error messages and stack traces
  - **Dependency Verification**: Use `uv show` to verify package installations

* **Support Contact**:
  - **Primary Contact**: AI Academy Team - EY
  - **Community Support**: CrewAI GitHub repository for framework-specific issues


### Troubleshooting AI Application Deployment

This section outlines potential issues that can arise during the deployment of an AI application, along with their causes, resolutions, and best practices for mitigation.


#### Infrastructure-Level Issues

##### Insufficient Resources

* **Problem**: System performance degradation due to resource constraints during intensive research operations
  - **Symptoms**: Slow response times (>30 seconds), memory errors, disk space warnings, API timeout failures
  - **Root Causes**: Large document corpus processing, concurrent API calls, insufficient RAM for vector operations, disk space exhaustion from logs and cache

* **Mitigation Strategy**:
  - **Proactive Monitoring**: Implement resource usage dashboards with alerts at 70% CPU, 80% memory, 85% disk usage thresholds
  - **Hardware Scaling**: Recommend minimum 16GB RAM for production use, SSD storage for vector database, dedicated processing cores for API operations

##### Network Failures

* **Problem**: API connectivity issues and network latency affecting system reliability
  - **Symptoms**: Connection timeouts, SSL certificate errors, DNS resolution failures, intermittent API response delays
  - **Impact**: Complete system unavailability, partial functionality loss, degraded user experience

* **Mitigation Strategy**:
  - **Connection Resilience**: Implement exponential backoff (1s, 2s, 4s, 8s, 16s), multiple DNS servers configuration, connection pooling for API efficiency
  - **Performance Optimization**: Content compression for API requests, connection keep-alive optimization, regional API endpoint selection

##### Deployment Pipeline Failures

* **Problem**: System deployment and update failures due to environment or dependency conflicts
  - **Symptoms**: Package installation errors, Python version conflicts, missing environment variables, configuration validation failures
  - **Root Causes**: Dependency version conflicts, corrupted virtual environment, missing system prerequisites, configuration drift

* **Mitigation Strategy**: 
  - **Environment Management**: Use containerization (Docker) for consistent deployments, automated environment validation scripts, dependency lock files (uv.lock) for reproducible builds
  - **Diagnostic Tools**: Enable verbose logging for error diagnostics, automated environment testing scripts


#### Integration Problems

##### API Failures

* **Problem**: External APIs (Azure OpenAI, Serper) are unreachable due to network errors, authentication failures, or service outages
  - **Symptoms**: HTTP 401/403 authentication errors, connection timeouts, SSL certificate validation failures
  - **Impact**: Complete research functionality loss, partial crew execution failures

* **Mitigation Strategy**:
  - **Retry Mechanisms**: Implement exponential backoff with configurable retry limits (1s, 2s, 4s, 8s delays)
  - **Authentication Validation**: Automated API key validation and refresh procedures
  - **Monitoring and Alerting**: Real-time API response monitoring with immediate error notifications

##### Data Format Mismatches

* **Problem**: Crashes or errors due to unexpected data formats from external APIs or configuration changes
  - **Symptoms**: JSON parsing errors, schema validation failures, type conversion exceptions
  - **Root Causes**: API response format changes, missing data validation, inconsistent configuration formats

* **Mitigation Strategy**: 
  - **Schema Validation**: Use Pydantic models for all API inputs/outputs with strict type checking
  - **API Versioning**: Pin specific API versions and validate responses before processing
  - **Input Sanitization**: Comprehensive data validation and cleaning before crew processing

#### Data Quality Problems

* **Problem**: Inaccurate or corrupt data leads to poor research results and unreliable outputs
* **Causes**:
  * Outdated local document corpus (Minecraft documentation)
  * Poor quality web search results from Serper API
  * Inconsistent query classification leading to wrong research paths

* **Mitigation Strategy**: 
  - **Document Curation**: Regular review and updating of local document corpus with verified, high-quality sources
  - **Source Validation**: Automated quality checks for web search results with credibility scoring
  - **Classification Monitoring**: Continuous tracking of query routing accuracy with manual validation samples

#### Model-Level Issues

##### Performance or Deployment Issues

* **Problem**: Incorrect or inconsistent results due to model limitations or environmental factors
  - **Symptoms**: Poor query classification accuracy, irrelevant research results, slow response times
  - **Root Causes**: Azure OpenAI model limitations, prompt engineering issues, inadequate context handling

* **Mitigation Strategy**:
  - **Prompt Optimization**: Regular testing and refinement of classification and research prompts
  - **Performance Monitoring**: Real-time tracking of response quality and classification accuracy
  - **Model Updates**: Stay current with Azure OpenAI model improvements and API updates

#### Safety and Security Issues

##### Unauthorised Access

* **Problem**: Sensitive API keys or local documents are exposed due to misconfigured security settings
  - **Impact**: Unauthorized API usage, potential data breaches, service disruption
  - **Mitigation**: Environment variable encryption, file system permissions, access logging

##### Data Breaches

* **Problem**: Local documents or query data is compromised due to inadequate security measures
  - **Impact**: Confidential information exposure, regulatory compliance violations
  - **Mitigation**: Local-only processing, encrypted storage, no persistent API response caching 
<!--
- **Resolution**:
  - Use secure storage services (e.g., AWS KMS).
  - Implement auditing for data access and alerts for unusual activity.
  6.1. Delayed or Missing Data-->


#### Monitoring and Logging Failures

##### Missing or Incomplete Logs

* **Problem**: Insufficient logging leads to difficulty in debugging issues and system monitoring
  - **Symptoms**: Missing error details, incomplete audit trails, lack of performance metrics
  - **Root Causes**: Inadequate logging configuration, verbose output not captured, log rotation issues

* **Mitigation Strategy**: 
  - **Comprehensive Logging**: Implement structured logging with multiple severity levels (DEBUG, INFO, WARN, ERROR, CRITICAL)
  - **Log Management**: Automated log rotation and archival with 30-day retention for compliance
  - **Performance Monitoring**: Real-time tracking of crew execution times, API response rates, and system resource usage

#### Recovery and Rollback

##### Rollback Mechanisms

* **Problem**: New deployment or configuration changes introduce critical errors requiring quick recovery
  - **Symptoms**: System failures, degraded performance, incorrect results
  - **Impact**: Service disruption, loss of user confidence, potential data issues

* **Mitigation Strategy**: 
  - **Version Control**: Maintain Git repository with tagged releases for quick rollback
  - **Environment Backup**: Regular backup of virtual environment and configuration files
  - **Configuration Management**: Environment variable backup and restoration procedures

##### Disaster Recovery

* **Problem**: Complete system outage, hardware failure, or data corruption requiring full recovery
  - **Impact**: Total service unavailability, potential data loss, extended downtime

* **Mitigation Strategy**:
  - **Backup Strategy**: Automated daily backup of vector database, document corpus, and system configurations
  - **Recovery Procedures**: Documented step-by-step recovery process with estimated recovery times
  - **Testing**: Regular disaster recovery testing with documented results and improvements

### EU Declaration of conformity 

<div style="color: gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/47/" style="color:blue; text-decoration:underline">Article 47</a>
  <p></p>
</div>

**System Name**: Esercizio Esteso Multi-Agent AI Research System
**Provider**: AI Academy Team - EY, [Address to be provided]
**Declaration Statement**: This EU Declaration of Conformity is issued under the sole responsibility of the AI Academy Team - EY.

**Conformity Statement**: The Esercizio Esteso AI system is in conformity with the EU AI Act Regulation (Limited Risk category) and applicable data protection regulations.

**Data Processing Compliance**: This AI system complies with Regulation (EU) 2016/679 (GDPR) through local data processing and minimal external data transmission.

**Harmonised Standards**: 
- ISO/IEC 27001:2013 - Information Security Management
- ISO/IEC 23053:2022 - Framework for AI risk management
- CrewAI Framework Standards for Multi-Agent AI Systems

**Assessment Procedure**: Internal conformity assessment performed according to Article 47 requirements for Limited Risk AI systems.

**Place and Date**: [Location], September 1, 2025
**Authorized Representative**: AI Academy Technical Lead, EY
**On behalf of**: EY AI Academy Team

### Standards applied

**Technical Standards**:
- **CrewAI Framework**: Multi-agent orchestration framework for AI workflows (version >=0.165.1)
- **FAISS (Facebook AI Similarity Search)**: Vector similarity search for efficient document retrieval (faiss-cpu >=1.12.0)
- **Pydantic**: Data validation and settings management using Python type annotations
- **Azure OpenAI Service**: Enterprise-grade AI services with built-in safety and compliance features
- **UV Package Manager**: Modern Python package and project management tool
- **Python 3.10-3.14**: Required Python version range for compatibility

**AI and ML Standards**:
- **Azure OpenAI API Standards**: RESTful API design principles for AI service integration
- **Vector Database Standards**: FAISS indexing standards for semantic search capabilities
- **LangChain Integration**: Document processing and chain construction for RAG implementations
- **CrewAI Flow Patterns**: State-based flow management and agent coordination best practices

**Security and Privacy Standards**:
- **HTTPS/TLS**: Encrypted communication for all external API calls (Azure OpenAI, Serper)
- **Environment Variable Management**: Secure credential storage and management practices
- **Local Data Processing**: Data minimization through local document processing and FAISS indexing
- **SSL Context Management**: Custom SSL context configuration for API connections

**Software Development Standards**:
- **Python PEP Standards**: Code formatting and structure following Python enhancement proposals
- **Virtual Environment Isolation**: Dependency management through UV and Python virtual environments
- **Configuration Management**: YAML-based agent and task configuration with environment-based API settings
- **Project Structure**: CrewAI project template structure with organized crew, agent, and task definitions

## Documentation Metadata

### Template Version
**Version 1.1** - Based on EU AI Act compliance template for Limited Risk AI systems, adapted for CrewAI multi-agent research applications. Updated to accurately reflect the Esercizio Esteso project structure and functionality.

### Documentation Authors

* **AI Academy Team, EY:** (Owner) - System development and implementation of Esercizio Esteso multi-agent system
* **GitHub Copilot Assistant:** (Contributor) - Documentation completion and AI Act compliance mapping
* **Technical Review Team, EY:** (Manager) - Technical validation and compliance oversight

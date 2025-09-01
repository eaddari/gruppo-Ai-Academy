# Application Documentation Template

**Application Owner**: cd "c:\Users\FJ138WZ\OneDrive - EY\Documents\Ai Academy\gruppo-Ai-Academy\29_08\crewai_group\esercizio_esteso" ; python -c "from src.esercizio_esteso.crews.rag.faiss_rag import test_rag; test_rag()"
<br>**Document Version**: idk
<br>**Reviewers**: idk

## Key Links

* [Code Repository](idk)
* [Deployment Pipeline](idk)
* [API]() ([Swagger Docs]())
* [Cloud Account]()
* [Project Management Board]()
* [Application Architecture]()

## General Information 

<div style="color: gray">
EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 1, 2, 3
<!-- info: this section covers the AI Act requirement of a description of the intended purpose, version and provider, relevant versions and updates. In Article 11, 2(d) a datasheet is required which describes all training methodologies and techniques as well as the characteristics of the training dataset, general description of the dataset, information about their provenance, scope and main characteristics, how the data was obtained and selected, labelling procedures conducted, and data cleaning methodologies deployed. -->
<p></p>
</div>

**Purpose and Intended Use**:
    
* The Esercizio Esteso project is a multi-agent AI research system built with CrewAI, enabling intelligent routing between specialized research crews for documentation, web search, and mathematical problem-solving.
* The system is modular and extensible, supporting the addition of new crews, agents, and tools for specialized tasks.
* Key features include intelligent routing between research crews, extensible architecture, documentation/web search/math problem-solving capabilities, custom tools for Q&A with citations, and dynamic RAG function loading.
* The system is documented using Sphinx, with the genericflow package providing additional flow management and tooling capabilities.
* [Information not available]: Intended sector of deployment.
* [Information not available]: Clearly stated problem the AI application aims to solve.
* [Information not available]: Target users and stakeholders.
* [Information not available]: Measurable goals and key performance indicators (KPIs).
* [Information not available]: Ethical implications and regulatory constraints.
* [Information not available]: Prohibited uses or potential misuse scenarios.
* **Operational environment:** The system is designed to operate in Python environments, expecting a Python virtual environment at `.venv/Scripts/python.exe` for tool execution, with a fallback to the system Python executable if not found. The `rag` directory must be added to the Python path for dynamic function imports. The system is documented using Sphinx and supports extensibility for new agents and tools.

## Risk classification

<div style="color: gray">
Prohibited Risk: EU AI Act Chapter II <a href="https://artificialintelligenceact.eu/article/5/" style="color:blue; text-decoration:underline">Article 5</a>
<br>High-Risk: EU AI Act Chapter III, Section 1 <a href="https://artificialintelligenceact.eu/article/6/" style="color:blue; text-decoration:underline">Article 6</a>, <a href="https://artificialintelligenceact.eu/article/7/" style="color:blue; text-decoration:underline">Article 7</a>  
<br>Limited Risk: Chapter IV <a href="https://artificialintelligenceact.eu/article/50/" style="color:blue; text-decoration:underline">Article 50</a>
<p></p>
</div>

* [Information not available]: High / Limited / Minimal (in accordance with the AI Act)
* [Information not available]: Reasoning for the above classification

## Application Functionality 

<div style="color: gray">
EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a> ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a>, paragraph 1, 2, 3
<!-- Info: this section covers the delineation of the general purpose of the system required in Article 1, with a focus on defining what the system should do and how it should work.-->
<p></p>
</div>

* **Instructions for use for deployers**: <div style="color: gray">(EU AI Act <a href="https://artificialintelligenceact.eu/article/13/" style="color:blue; text-decoration:underline">Article 13</a>)</div>
    - Ensure the Python virtual environment is set up at `.venv/Scripts/python.exe` for tool execution. If not found, the system will fallback to the system Python executable.
    - The `rag` directory must be added to the Python path for dynamic function imports.
    - Add content using reStructuredText syntax for documentation.
    - Provide questions to custom tools for answers with citations.
    - Configuration for tools should conform to pydantic's `ConfigDict`, ensuring structured and validated settings.

* **Model Capabilities**:
    - The application enables intelligent routing between specialized research crews for documentation, web search, and mathematical problem-solving.
    - Supports modular and extensible architecture, allowing addition of new crews, agents, and tools.
    - Custom tools include a question-and-answer interface with source citations and dynamic import of RAG (Retrieval-Augmented Generation) functions.
    - Vision tools are available, expanding the system’s capabilities.
    - [Information not available]: Supported languages, data types, or scenarios.
    - [Information not available]: Limitations.

* **Input Data Requirements**:
    - [Information not available]: Format and quality expectations for input data.
    - [Information not available]: Examples of valid and invalid inputs.

* **Output Explanation**:
    - [Information not available]: How to interpret predictions, classifications, or recommendations.
    - [Information not available]: Uncertainty or confidence measures, if applicable.

* **System Architecture Overview**:
    - The system is built using CrewAI for multi-agent orchestration.
    - Crews are organized within the `esercizio_esteso.crews` package.
    - Custom tools are implemented in the `esercizio_esteso.tools` and `genericflow.tools.custom_tool` modules.
    - Vision tools are available in the `esercizio_esteso.tools.vision_tools` module.
    - The system is documented using Sphinx, with the `genericflow` package providing additional flow management and tooling capabilities.
    - The architecture supports dynamic import capabilities for RAG functions and expects a Python virtual environment for execution.

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
| [Information not available] | [Information not available] | [Information not available] |

### Datasets

Link to all dataset documentation and information used to evaluate the AI/ML System.  
(Note, Model Documentation should also contain dataset information and links for all datasets used to train and test each respective model) 

| Dataset   | Link to Single Source of Truth | Description of Application Usage |
|-----------|--------------------------------|----------------------------------|
| [Information not available] | [Information not available] | [Information not available] |

## Deployment
    
* Infrastructure and environment details (e.g., cloud setup, APIs).
* Integration with external systems or applications.

### Infrastructure and Environment Details

* **Cloud Setup**:
  * [Information not available]: Specify cloud provider (e.g., AWS, Azure, GCP) and regions.
  * [Information not available]: List required services: compute (e.g., EC2, Kubernetes), storage (e.g., S3, Blob Storage), and databases (e.g., DynamoDB, Firestore).
  * [Information not available]: Define resource configurations (e.g., VM sizes, GPU/TPU requirements).
  * [Information not available]: Network setup: VPC, subnets, and security groups.

* **APIs**:
  * [Information not available]: API endpoints, payload structure, authentication methods (e.g., OAuth, API keys).
  * [Information not available]: Latency and scalability expectations.

## Integration with External Systems

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a> ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 1 (b, c, d, g, h), 2 (a)
  <p></p>
</div>

* **Systems**:
  * [Information not available]: List dependencies 
  * [Information not available]: Data flow diagrams showing interactions.
  * [Information not available]: Error-handling mechanisms for APIs or webhooks

## Deployment Plan

* **Infrastructure**:
  * [Information not available]: List environments: development, staging, production.
  * [Information not available]: Resource scaling policies (e.g., autoscaling, redundancy).
  * [Information not available]: Backup and recovery processes.
* **Integration Steps**:
  * [Information not available]: Order of deployment (e.g., database migrations, model upload, service launch).
  * [Information not available]: Dependencies like libraries, frameworks, or APIs.
  * [Information not available]: Rollback strategies for each component.
* **User Information**: [Information not available]: where is this under deployment?

## Lifecycle Management

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 6
  <p></p>
</div>
    
* [Information not available]: Monitoring procedures for performance and ethical compliance.
* [Information not available]: Versioning and change logs for model updates.
* **Metrics**:
  * [Information not available]: Application performance: response time, error rate.
  * [Information not available]: Model performance: accuracy, precision, recall.
  * [Information not available]: Infrastructure: CPU, memory, network usage.
* **Key Activities**:
  * [Information not available]: Monitor performance in real-world usage.
  * [Information not available]: Identify and fix drifts, bugs, or failures.
  * [Information not available]: Update the model periodically.
* **Documentation Needs**:
  * [Information not available]: **Monitoring Logs**: Real-time data on accuracy, latency, and uptime.
  * [Information not available]: **Incident Reports**: Record of failures, impacts, and resolutions.
  * [Information not available]: **Retraining Logs**: Data updates and changes in performance.
  * [Information not available]: **Audit Trails**: Comprehensive history of changes to ensure compliance.
-**Manteinance of change logs**: 
* [Information not available]: new features added
* [Information not available]: updates to existing functionality
* [Information not available]: deprecated features
* [Information not available]: removed features
* [Information not available]: bug fixes
* [Information not available]: security and vulnerability fixes

### Risk Management System

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/9/" style="color:blue; text-decoration:underline">Article 9</a>
  <br>EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>
  ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a>
  <p></p>
</div>
<!--**Instructions:**  A thorough risk management system is mandated by the AI Act, especially for high-risk AI systems. This section documents the  proactive efforts to ensure the AI system operates safely and ethically. In general in this section you should document all the measures undertaken to make sure that a system operates safely on the market. Example: Consider a facial recognition system used for real-time law enforcement in public spaces. This is categorized as high-risk under the EU AI Act. If developers document the risk that the system might misidentify individuals—particularly among minority groups due to biased training data—they can plan for rigorous dataset audits, independent bias testing, and establish human oversight in decision-making. Without documenting this risk, the system might be deployed without safeguards, leading to wrongful detentions and legal liabilities. Systematic documentation ensures these issues are not only identified but addressed before harm occurs.-->

**Risk Assessment Methodology:** [Information not available]

**Identified Risks:** 
[Information not available]

**Potential Harmful Outcomes:** [Information not available]

**Likelihood and Severity:** [Information not available]

#### Risk Mitigation Measures

**Preventive Measures:** [Information not available]

**Protective Measures:** [Information not available]

## Testing and Validation (Accuracy, Robustness, Cybersecurity)

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/15/" style="color:blue; text-decoration:underline">Article 15</a>
  <p></p>
</div>

**Testing and Validation Procedures (Accuracy):**
[Information not available]

**Performance Metrics:** [Information not available]

**Validation Results:** [Information not available]

**Measures for Accuracy:** [Information not available]

### Accuracy throughout the lifecycle

**Data Quality and Management:** [Information not available]

**Model Selection and Optimisation:** [Information not available]

**Feedback Mechanisms:** [Information not available]

### Robustness 

**Robustness Measures:**
[Information not available]

**Scenario-Based Testing:**
[Information not available]

**Redundancy and Fail-Safes:**
[Information not available]

**Uncertainty Estimation:**
[Information not available]

### Cybersecurity 

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2 (h)
  <p></p>
</div>

**Data Security:** [Information not available]

**Access Control:** [Information not available]

**Incident Response :** [Information not available]

These measures include threat modelling, data security, adversarial robustness, secure development practices, access control, and incident response mechanisms.

Post-deployment monitoring, patch management, and forensic logging are crucial to maintaining ongoing cybersecurity compliance.

Documentation of all cybersecurity processes and incidents is mandatory to ensure accountability and regulatory conformity.

## Human Oversight 

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>;; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2(e)
  <br>EU AI Act <a href="https://artificialintelligenceact.eu/article/14/" style="color:blue; text-decoration:underline">Article 14</a>
  <p></p>
</div>

<!-- info: AI Act Article 11, paragraph 2(e) requirements: assessment of the human oversight measures needed in accordance with Article 14, including the assessment of the technical measures needed to facilitate the integration of the outputs of the AI systems by deployers. -->

**Human-in-the-Loop Mechanisms:**  [Information not available]

**Override and Intervention Procedures:** [Information not available]

**User Instructions and Training:** [Information not available]

**Limitations and Constraints of the System:** [Information not available]

## Incident Management
<!-- what happens when things go wrong. This part is particularly important to provide information on how incidents were dealth with and the processes put in place to minimize damage when things go wrong. -->
* **Common Issues**:
  * [Information not available]: List common errors and their solutions.
  * [Information not available]: Logs or debugging tips for advanced troubleshooting.
* **Support Contact**:
  * [Information not available]: How to reach technical support or community forums.

### Troubleshooting AI Application Deployment

This section outlines potential issues that can arise during the deployment of an AI application, along with their causes, resolutions, and best practices for mitigation.

#### Infrastructure-Level Issues

##### Insufficient Resources

* **Problem**: Inaccurate resource estimation for production workloads.
  * Unexpected spikes in user traffic can lead to insufficient resources such as compute, memory or storage that can lead to crashes and bad performance

* **Mitigation Strategy**:
<!-- describe here the resolution strategy such as:
-  Enable autoscaling (e.g., Kubernetes Horizontal Pod Autoscaler).
  - Monitor usage metrics and adjust resource allocation dynamically.
  - Implement rate-limiting for traffic spikes. -->


##### Network Failures

* **Problem**:  network bottlenecks  can lead to inaccessible or experiences latency of the application.

* **Mitigation Strategy**:
<!-- 
  - Test network connectivity 
  - Use content delivery networks (CDNs) or regional load balancers.
  - Ensure proper failover mechanisms.-->


##### Deployment Pipeline Failures

* **Problem**: pipeline fails to build, test, or deploy because of issues of compatibility between application code and infrastructure, environment variables or credentials misconfiguration.

* **Mitigation Strategy**: 
<!--:
  - Roll back to the last stable build.
  - Fix pipeline scripts and use containerisation for environment consistency.
  - Enable verbose logging for error diagnostics.-->


#### Integration Problems

##### API Failures

* **Problem**: External APIs or internal services are unreachable due to network errors or authentication failures.

* **Mitigation Strategy**:
<!--:
  - Implement retries with exponential backoff.
  - Validate API keys or tokens and refresh as needed.
  - Log and monitor API responses for debugging. -->

##### Data Format Mismatches

* **Problem**: Crashes or errors due to unexpected data formats such as changes in the schema of external data sources or missing data validation steps.

* **Mitigation Strategy**: 

<!--
  - Use schema validation tools (e.g., JSON schema validators).
  - Add versioning to APIs and validate inputs before processing.-->


#### Data Quality Problems

* **Problem**: Inaccurate or corrupt data leads to poor predictions.
* **Causes**:
  * No data validation or cleaning processes.
  * Inconsistent labelling in training datasets.

* **Mitigation Strategy**: 
<!--
- **Resolution**:
  - Automate data quality checks (e.g., Great Expectations framework).
  - Regularly audit and clean production data.-->


#### Model-Level Issues

##### Performance or Deployment Issues

* **Problem**: Incorrect or inconsistent results due to data drift or inadequate training data for the real world deployment domain. 

* **Mitigation Strategy**:

<!--
- **Resolution**:
  - Monitoring for data drift and retraining of the model as needed.
  - Regularly update the model -->


#### Safety and Security Issues

##### Unauthorised Access

* **Problem**: Sensitive data or APIs are exposed due to misconfigured authentication and authorization.

##### Data Breaches

* **Problem**: User or model data is compromised due to insecure storage or lack of monitoring and logging of data access. 

* **Mitigation Strategy**: 
<!--
- **Resolution**:
  - Use secure storage services (e.g., AWS KMS).
  - Implement auditing for data access and alerts for unusual activity.
  6.1. Delayed or Missing Data-->


#### Monitoring and Logging Failures

##### Missing or Incomplete Logs

* **Problem**: Lack of information to debug issues due to inefficient logging. Critical issues go unnoticed, or too many false positives occur by lack of implementation ofactionable information in alerts. 

* **Mitigation Strategy**: 


<!--
- **Resolution**:
  - Fine-tune alerting thresholds and prioritise critical alerts.
  - Use tools like Prometheus Alertmanager to manage and group alerts. -->


#### Recovery and Rollback

##### Rollback Mechanisms

* **Problem**: New deployment introduces critical errors.

* **Mitigation Strategy**: 

<!--
- **Resolution**:
  - Use blue-green or canary deployments to minimise impact.
  - Maintain backups of previous versions and configurations. -->

##### Disaster Recovery

* **Problem**: Complete system outage or data loss.

* **Mitigation Strategy**:

<!--
- **Resolution**:
  - Test and document disaster recovery plans.
  - Use automated backups and verify restore procedures.-->

### EU Declaration of conformity 

<div style="color: gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/47/" style="color:blue; text-decoration:underline">Article 47</a>
  <p></p>
</div>

<!-- when applicable and certifications are available: it requires a systems name as well as the name and address of the provider; a statement that the EU declaration of conformity referred to in Article 47 is issued under the sole responsibility of the provider; a statement that the AI system is in conformity with this Regulation and, if applicable, with any other relevant Union law that provides for the issuing of the EU declaration of conformity referred to in Article 47, Where an AI system involves the processing of personal data;  a statement that that AI system complies with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, reference to the harmonised standards used or any other common specification in relation to which
conformity is declared; the name and identification number of the notified body, a description of the conformity
assessment procedure performed, and identification of the certificate issued; the place and date of issue of the declaration, the name and function of the person who signed it, as well as an
indication for, or on behalf of whom, that person signed, a signature.-->

[Information not available]

### Standards applied

<!-- Document here the standards and frameworks used-->

[Information not available]

## Documentation Metadata

### Template Version
<!-- info: link to model documentation template (i.e. could be a GitHub link) -->

[Information not available]

### Documentation Authors
<!-- info: Give documentation authors credit

Select one or more roles per author and reference author's
emails to ease communication and add transparency. -->

* [Information not available]: (Owner / Contributor / Manager)
* [Information not available]: (Owner / Contributor / Manager)
* [Information not available]: (Owner / Contributor / Manager)
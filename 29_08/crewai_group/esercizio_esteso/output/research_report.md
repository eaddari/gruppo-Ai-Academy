# Application Documentation Template

**Application Owner**: idkidk
<br>**Document Version**: i
<br>**Reviewers**: [Information not available]

## Key Links

* [Code Repository]()  
* [Deployment Pipeline]()  
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
    
* Description of the AI system's intended purpose, including the sector of deployment.  
  - Esercizio Esteso is an AI system built on a multi-agent architecture using CrewAI, designed to intelligently route research tasks to specialized crews based on task type (documentation, web search, or mathematical problem-solving).  
* Clearly state the problem the AI application aims to solve.  
  - The system addresses the need for efficient, automated research assistance, documentation management, and mathematical problem-solving by leveraging specialized AI agents and tools.  
* Delineate target users and stakeholders.  
  - [Information not available]
* Set measurable goals and key performance indicators (KPIs).  
  - [Information not available]
* Consider ethical implications and regulatory constraints.  
  - [Information not available]
* Clear statement on prohibited uses or potential misuse scenarios.  
  - [Information not available]
* **Operational environment:** Describe where and how the AI system will operate, such as on mobile devices, cloud platforms, or embedded systems.  
  - The system is implemented in Python and operates within a Python virtual environment. It is designed to be extensible and can be deployed in environments supporting Python and Sphinx-based documentation workflows.

## Risk classification

<div style="color: gray">
Prohibited Risk: EU AI Act Chapter II <a href="https://artificialintelligenceact.eu/article/5/" style="color:blue; text-decoration:underline">Article 5</a>
<br>High-Risk: EU AI Act Chapter III, Section 1 <a href="https://artificialintelligenceact.eu/article/6/" style="color:blue; text-decoration:underline">Article 6</a>, <a href="https://artificialintelligenceact.eu/article/7/" style="color:blue; text-decoration:underline">Article 7</a>  
<br>Limited Risk: Chapter IV <a href="https://artificialintelligenceact.eu/article/50/" style="color:blue; text-decoration:underline">Article 50</a>
<p></p>
</div>

* [Information not available]
* reasoning for the above classification  
   [Information not available]
   
## Application Functionality 

<div style="color: gray">
EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a> ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a>, paragraph 1, 2, 3
<!-- Info: this section covers the delineation of the general purpose of the system required in Article 1, with a focus on defining what the system should do and how it should work.-->
<p></p>
</div>

* **Instructions for use for deployers**: <div style="color: gray">(EU AI Act <a href="https://artificialintelligenceact.eu/article/13/" style="color:blue; text-decoration:underline">Article 13</a>)</div>
  - Deployers must configure a Python virtual environment, ensure the rag directory is accessible for dynamic imports, and manage dependencies for the esercizio_esteso and genericflow packages. Documentation content should be added using reStructuredText syntax.
* **Model Capabilities**:
  * What the application can and cannot do (limitations).
    - The application can intelligently route research tasks to specialized crews for documentation retrieval, web search, and mathematical problem-solving. It supports extensibility via custom tools and dynamic function imports. Limitations include lack of detailed input/output requirements and unspecified agent names.
  * Supported languages, data types, or scenarios.
    - [Information not available]
* **Input Data Requirements**:
  * Format and quality expectations for input data.
    - Users provide questions as input; the system expects well-formed queries for optimal results.
  * Examples of valid and invalid inputs.
    - [Information not available]
* **Output Explanation**:
  * How to interpret predictions, classifications, or recommendations.
    - The system returns answers to user questions, including source citations where applicable.
  * Uncertainty or confidence measures, if applicable.
    - [Information not available]
* **System Architecture Overview**:
  * Functional description and architecture of the system.
    - Esercizio Esteso is built on a multi-agent architecture using CrewAI. It features intelligent routing of tasks to specialized crews (documentation, web search, math problem-solving), each comprising individual AI agents and custom tools/modules.
  * Describe the key components of the system (including datasets, algorithms, models, etc.)
    - Key components include specialized crews, AI agents, custom tools (vision_tools, custom_tool), and dynamic import support for RAG functions. The system is organized into esercizio_esteso and genericflow packages.

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
  * [Information not available]
* **APIs**:
  * [Information not available]

## Integration with External Systems

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a> ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 1 (b, c, d, g, h), 2 (a)
  <p></p>
</div>

* **Systems**:
  * List dependencies 
    - esercizio_esteso and genericflow Python packages, Python virtual environment, Sphinx for documentation.
  * Data flow diagrams showing interactions.
    - [Information not available]
  * Error-handling mechanisms for APIs or webhooks
    - [Information not available]

## Deployment Plan

* **Infrastructure**:
  * List environments: development, staging, production.
    - [Information not available]
  * Resource scaling policies (e.g., autoscaling, redundancy).
    - [Information not available]
  * Backup and recovery processes.
    - [Information not available]
* **Integration Steps**:
  * Order of deployment (e.g., database migrations, model upload, service launch).
    - [Information not available]
  * Dependencies like libraries, frameworks, or APIs.
    - esercizio_esteso, genericflow, Sphinx, Python 3.x
  * Rollback strategies for each component.
    - [Information not available]
* **User Information**: where is this under deployment?
    - [Information not available]

## Lifecycle Management

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 6
  <p></p>
</div>
    
* Monitoring procedures for performance and ethical compliance.
  - [Information not available]
* Versioning and change logs for model updates.
  - [Information not available]
* **Metrics**:
  * Application performance: response time, error rate.
    - [Information not available]
  * Model performance: accuracy, precision, recall.
    - [Information not available]
  * Infrastructure: CPU, memory, network usage.
    - [Information not available]
* **Key Activities**:
  * Monitor performance in real-world usage.
    - [Information not available]
  * Identify and fix drifts, bugs, or failures.
    - [Information not available]
  * Update the model periodically.
    - [Information not available]
* **Documentation Needs**:
  * **Monitoring Logs**: Real-time data on accuracy, latency, and uptime.
    - [Information not available]
  * **Incident Reports**: Record of failures, impacts, and resolutions.
    - [Information not available]
  * **Retraining Logs**: Data updates and changes in performance.
    - [Information not available]
  * **Audit Trails**: Comprehensive history of changes to ensure compliance.
    - [Information not available]
-**Manteinance of change logs**: 
* new features added
* updates to existing functionality
* deprecated features
* removed features
* bug fixes
* security and vulnerability fixes

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

**Potential Harmful Outcomes:** List possible negative effects, such as biased decisions, privacy breaches, or safety hazards.
[Information not available]

**Likelihood and Severity:** Assess how likely each risk is to occur and the potential impact on users or society.
[Information not available]

#### Risk Mitigation Measures

**Preventive Measures:** Detail actions taken to prevent risks, like implementing data validation checks or bias reduction techniques.
[Information not available]

**Protective Measures:** Describe contingency plans and safeguards in place to minimize the impact if a risk materializes.
[Information not available]

## Testing and Validation (Accuracy, Robustness, Cybersecurity)

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/15/" style="color:blue; text-decoration:underline">Article 15</a>
  <p></p>
</div>

**Testing and Validation Procedures (Accuracy):**
[Information not available]

**Performance Metrics:** List the metrics used to evaluate the AI system, such as accuracy, precision, recall, F1 score, or mean squared error.
[Information not available]

**Validation Results:** Summarize the outcomes of testing, including any benchmarks or thresholds met or exceeded.
[Information not available]

**Measures for Accuracy:** High-quality data, algorithm optimisation, evaluation metrics, and real-time performance tracking.
[Information not available]
  
### Accuracy throughout the lifecycle

**Data Quality and Management:** High-Quality Training Data: Data Preprocessing, techniques like normalisation, outlier removal, and feature scaling to improve data consistency, Data Augmentation, Data Validation
[Information not available]

**Model Selection and Optimisation:** Algorithm selection suited for the problem, Hyperparameter Tuning (grid search, random search, Bayesian optimization), Performance Validation( cross-validation by splitting data into training and testing sets, using k-fold or stratified cross-validation), Evaluation Metrics (precision,recall, F1 score, accuracy, mean squared error (MSE), or area under the curve (AUC).
[Information not available]

**Feedback Mechanisms:** Real-Time Error Tracking, Incorporate mechanisms to iteratively label and include challenging or misclassified examples for retraining.
[Information not available]

### Robustness 

<-- Add outlier detection and all possible post analysis, what are the criticalities -->

**Robustness Measures:**
[Information not available]

* Adversarial training, stress testing, redundancy, error handling, and domain adaptation.
[Information not available]

**Scenario-Based Testing:**
[Information not available]

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
[Information not available]

**Access Control:**
[Information not available]

**Incident Response :**
[Information not available]

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

**Limitations and Constraints of the System:** Clearly state what the AI system cannot do, including any known weaknesses or scenarios where performance may degrade.
- The system's limitations include lack of detailed input/output requirements, unspecified agent names, and potential gaps in human oversight and risk management documentation.

## Incident Management
<!-- what happens when things go wrong. This part is particularly important to provide information on how incidents were dealth with and the processes put in place to minimize damage when things go wrong. -->
* **Common Issues**:
  * List common errors and their solutions.
    - [Information not available]
  * Logs or debugging tips for advanced troubleshooting.
    - [Information not available]
* **Support Contact**:
  * How to reach technical support or community forums.
    - [Information not available]

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

* **Name, Team:** (Owner / Contributor / Manager) [Information not available]
* **Name, Team:** (Owner / Contributor / Manager) [Information not available]
* **Name, Team:** (Owner / Contributor / Manager) [Information not available]
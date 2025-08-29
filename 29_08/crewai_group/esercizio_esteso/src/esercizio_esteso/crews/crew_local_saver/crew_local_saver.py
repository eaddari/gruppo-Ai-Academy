from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from tools.web_content_saver import WebContentSaver
from crewai.llm import LLM
import os

# Configure the LLM for the crew
crew_llm = LLM(
    model=f"azure/{os.getenv('MODEL', 'gpt-4')}",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
    temperature=0.1
)

# Initialize tools  
web_saver_tool = WebContentSaver()

@CrewBase
class CrewLocalSaver():
    """CrewLocalSaver crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def content_processor(self) -> Agent:
        return Agent(
            config=self.agents_config['content_processor'],
            verbose=True,
            llm=crew_llm
        )

    @agent
    def knowledge_indexer(self) -> Agent:
        return Agent(
            config=self.agents_config['knowledge_indexer'],
            verbose=True,
            tools=[web_saver_tool],
            llm=crew_llm
        )

    @agent
    def quality_validator(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_validator'],
            verbose=True,
            llm=crew_llm
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def content_processing_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_processing_task'],
        )
        
    @task
    def indexing_task(self) -> Task:
        return Task(
            config=self.tasks_config['indexing_task'],
        )
        
    @task
    def validation_task(self) -> Task:
        return Task(
            config=self.tasks_config['validation_task'],
            output_file='indexing_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewLocalSaver crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from langchain_openai import AzureChatOpenAI
import os
import ssl
import httpx

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

azure_llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
    azure_deployment=os.getenv("MODEL", "gpt-4"),
    temperature=0.1,
    http_client=httpx.Client(verify=False)
)

from crewai.llm import LLM

crew_llm = LLM(
    model=f"azure/{os.getenv('MODEL', 'gpt-4')}",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
    temperature=0.1)

@CrewBase
class Docgen():
    """Document Generation crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def generation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['generation_agent'],
            verbose=True,
            tools=[],
            llm=crew_llm
        )

    @task
    def document_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['document_generation_task'],
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Document Generation crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
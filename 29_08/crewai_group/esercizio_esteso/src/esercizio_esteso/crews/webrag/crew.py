from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from src.esercizio_esteso.tools.custom_tool import LocalRag
import ssl
import httpx

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

@CrewBase
class Webrag():
    """Webrag crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def rag_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['rag_researcher'], # type: ignore[index]
            verbose=True,
            tools=[LocalRag()]
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True
        )

    @task
    def rag_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['rag_research_task'] # type: ignore[index]
        )
        
    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file='report.md'
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Webrag crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

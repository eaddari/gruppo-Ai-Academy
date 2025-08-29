from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from src.esercizio_esteso.tools.vision_tools import DallETool
import os
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

from crewai.llm import LLM

crew_llm = LLM(
    model=f"azure/{os.getenv('MODEL', 'gpt-4')}",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
    temperature=0.1)


@CrewBase
class ExplanationCrew():
    """Explanation crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def input_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['input_agent'],
            verbose=True,
            llm=crew_llm
        )
    @agent
    def dalle_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['dalle_agent'],
            verbose=True,
            llm=crew_llm,
            tools=[DallETool()],
        )
    @task
    def input_task(self) -> Task:
        return Task(
            config=self.tasks_config['input_task']
        )
    @task
    def dalle_task(self) -> Task:
        return Task(
            config=self.tasks_config['dalle_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Explanation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

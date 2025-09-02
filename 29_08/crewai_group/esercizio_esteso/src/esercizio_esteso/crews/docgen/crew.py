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

@CrewBase
class Docgen():
    """Document Generation crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def generation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['generation_agent'], # type: ignore[index]
            verbose=True,
            # tools=[SerperDevTool()] possibilità di usare tool al momento disattivata
        )
    
    @task
    def document_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['document_generation_task'] # type: ignore[index]
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
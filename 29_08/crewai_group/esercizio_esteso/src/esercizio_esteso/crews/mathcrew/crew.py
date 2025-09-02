from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from tools.custom_tool import MathEquationsTool
import ssl
import httpx

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

@CrewBase
class Math():
    """Math crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def math_tool_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['math_tool_agent'], # type: ignore[index]
            verbose=True,
            tools=[MathEquationsTool()]
        )

    @task
    def math_task(self) -> Task:
        return Task(
            config=self.tasks_config['math_task'] # type: ignore[index]
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Math crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import sys
import os
from dotenv import load_dotenv
from pathlib import Path
from openai import AzureOpenAI
from crewai_tools import DallETool

dalle_tool = DallETool()

load_dotenv()

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    question: str = Field(..., description="Question to ask the tool.")

class DallETool(BaseTool):
    name: str = "Dall-E Tool"
    description: str = (
        "This tool generates images from textual descriptions using DALL-E. "
        "Provide a detailed description of the image you want to create, and get a high-quality image in response."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def generate_image(self, description: str) -> str:
        """Generate an image from the provided description using DALL-E."""
        try:
            response = dalle_tool.generate_image(description)
            return response
        except Exception as e:
            return f"Error generating image: {str(e)}"


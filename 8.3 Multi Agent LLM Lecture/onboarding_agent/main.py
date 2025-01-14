from assistants import (
    welcome_assistant,
    hr_assistant,
    background_check_assistant,
    it_assistant,
)
from workflow import OnboardingWorkflow, route_message
from autogen import UserProxyAgent
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create a user proxy agent with Docker disabled
user_proxy = UserProxyAgent(
    name="user_proxy", code_execution_config={"use_docker": False}
)

# Initialize the workflow
workflow = OnboardingWorkflow()

# Start the conversation
while True:
    user_input = input("You: ")
    assistant = route_message(user_input, workflow, client)
    assistant_response = assistant.handle_message(user_input)
    print(f"{assistant.name} (to user_proxy):\n\n{assistant_response['content']}\n")

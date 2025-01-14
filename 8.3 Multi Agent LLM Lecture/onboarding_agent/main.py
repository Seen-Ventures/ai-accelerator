from autogen import AssistantAgent, UserProxyAgent
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class AssistantAgent:
    def __init__(self, name, system_message):
        self.name = name
        self.system_message = system_message

    def handle_message(self, message):
        # Define how the assistant should handle the message
        response = f"{self.name} received the message: {message}"
        return {"content": response}


# Initialize assistant agents
welcome_assistant = AssistantAgent(
    name="welcome_assistant",
    system_message="Welcome Assistant: Welcomes new recruits, gathers essential info (full name, contact details, email, address, mobile number), gives a quick overview of Seen Ventures.",
)
hr_assistant = AssistantAgent(
    name="hr_assistant",
    system_message="HR Assistant: Expert on NZ employment rules for unpaid 12-week internships. Explains the basics, including working hours and health & safety, clarifies that minimum wage and holiday pay don't apply, and outlines relevant company policies, considering the remote work setup.",
)
background_check_assistant = AssistantAgent(
    name="background_check_assistant",
    system_message="Background Check Assistant: Discreetly conducts background checks and only raises concerns if needed.",
)
it_assistant = AssistantAgent(
    name="it_assistant",
    system_message="IT Assistant: Provides IT login details (email and password), explains IT policies, and helps with any tech issues.",
)

# Create a user proxy agent with Docker disabled
user_proxy = UserProxyAgent(
    name="user_proxy", code_execution_config={"use_docker": False}
)


def route_message(message):
    # Use OpenAI's API for intent classification
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",  # Or a suitable model like "gpt-4" or "gpt-4-1106-preview"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Based on this user message: '{message}', which assistant should handle it?\n- welcome_assistant\n- hr_assistant\n- background_check_assistant\n- it_assistant",
            },
        ],
    )

    # Extract the assistant name from the response
    assistant_name = response.choices[0].message.content.strip().lower()
    print(f"Assistant Name: {assistant_name}")

    # Map assistant name to the corresponding agent
    if "welcome" in assistant_name:
        return welcome_assistant
    elif "hr" in assistant_name:
        return hr_assistant
    elif "background" in assistant_name:
        return background_check_assistant
    elif "it" in assistant_name:
        return it_assistant
    else:
        return welcome_assistant  # Default to welcome assistant


# Start the conversation
while True:
    user_input = input("You: ")
    assistant = route_message(user_input)
    # Simulate sending the message to the appropriate assistant
    print(f"user_proxy (to {assistant.name}):\n\n{user_input}\n")
    assistant_response = assistant.handle_message(user_input)
    print(f"{assistant.name} (to user_proxy):\n\n{assistant_response['content']}\n")

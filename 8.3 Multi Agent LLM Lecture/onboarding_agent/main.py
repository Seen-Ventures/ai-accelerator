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
        self.conversation_state = {}

    def handle_message(self, message):
        if self.name == "welcome_assistant":
            return self.welcome_assistant_response(message)
        elif self.name == "hr_assistant":
            return self.hr_assistant_response(message)
        elif self.name == "background_check_assistant":
            return self.background_check_response(message)
        elif self.name == "it_assistant":
            return self.it_assistant_response(message)
        else:
            return {"content": "I'm not sure how to help with that."}

    def welcome_assistant_response(self, message):
        if "hello" in message.lower():
            return {
                "content": "Hello! Welcome to Seen Ventures. How can I assist you today? Are you looking for help with onboarding, company policies, or something else?"
            }
        elif "onboard" in message.lower():
            return {
                "content": "Great! Let's get you started with the onboarding process. First, I'll need some information from you. Can you please provide your full name, contact details, email, address, and mobile number?"
            }
        else:
            return {"content": "Welcome! How can I help you today?"}

    def hr_assistant_response(self, message):
        # Simulate HR-related responses
        if "employment rules" in message.lower():
            return {
                "content": "In New Zealand, unpaid 12-week internships have certain rules. Working hours should be reasonable, and health & safety regulations must be followed. Minimum wage and holiday pay don't apply. Do you have any specific questions?"
            }
        else:
            return {
                "content": "HR Assistant here! How can I help you with your employment or HR-related questions?"
            }

    def background_check_response(self, message):
        # Simulate background check responses
        return {
            "content": "Background Check Assistant here! I can help you with questions about background checks. Please provide the details you need assistance with."
        }

    def it_assistant_response(self, message):
        # Simulate IT-related responses
        if "login details" in message.lower():
            return {
                "content": "I can help you with your IT login details. Please provide your email address and I'll get the necessary information for you."
            }
        else:
            return {
                "content": "IT Assistant here! How can I assist you with your technical issues or questions?"
            }


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
        model="gpt-4-1106-preview",
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

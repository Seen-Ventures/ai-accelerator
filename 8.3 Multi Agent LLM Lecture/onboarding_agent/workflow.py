from assistants import (
    welcome_assistant,
    hr_assistant,
    background_check_assistant,
    it_assistant,
)


# Define the onboarding workflow
class OnboardingWorkflow:
    def __init__(self):
        self.steps = [
            {"step": "welcome", "agent": "welcome_assistant"},
            {"step": "collect_details", "agent": "hr_assistant"},
            {"step": "background_check", "agent": "background_check_assistant"},
            {"step": "provide_login", "agent": "it_assistant"},
        ]
        self.current_step = 0

    def next_step(self):
        # Move to the next step in the workflow
        if self.current_step < len(self.steps):
            step = self.steps[self.current_step]
            self.current_step += 1
            return step
        return None


# Route messages to the appropriate assistant based on the workflow
def route_message(message, workflow, client):
    if "hello" in message.lower() or "welcome" in message.lower():
        return welcome_assistant
    elif (
        "onboard" in message.lower()
        or "join" in message.lower()
        or "company policies" in message.lower()
    ):
        return hr_assistant
    elif "background check" in message.lower():
        return background_check_assistant
    elif "login details" in message.lower() or "tech issue" in message.lower():
        return it_assistant
    else:
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
            step = workflow.next_step()
            if step:
                agent_name = step["agent"]
                if agent_name == "welcome_assistant":
                    return welcome_assistant
                elif agent_name == "hr_assistant":
                    return hr_assistant
                elif agent_name == "background_check_assistant":
                    return background_check_assistant
                elif agent_name == "it_assistant":
                    return it_assistant
    return welcome_assistant  # Default to welcome assistant

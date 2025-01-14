from skills import StoreInformationSkill, ValidateDataSkill, BackgroundCheckSkill


# Define the AssistantAgent class with methods to handle different types of responses
class AssistantAgent:
    def __init__(self, name, system_message):
        self.name = name
        self.system_message = system_message
        self.conversation_state = {}
        self.store_information_skill = StoreInformationSkill()
        self.validate_data_skill = ValidateDataSkill()
        self.background_check_skill = BackgroundCheckSkill()

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
        elif "onboard" in message.lower() or "join" in message.lower():
            self.conversation_state["context"] = "onboarding"
            return {
                "content": "Great! Let's get you started with the onboarding process. I'll transfer you to our HR assistant to collect the necessary information."
            }
        elif "company policies" in message.lower():
            self.conversation_state["context"] = "company policies"
            return {
                "content": "Sure, I can help with company policies. I'll transfer you to our HR assistant to provide the details."
            }
        else:
            return {"content": "Welcome! How can I help you today?"}

    def hr_assistant_response(self, message):
        if "work remotely" in message.lower():
            return {
                "content": "Yes, you can work remotely. Our company offers flexible working arrangements, including remote work options. Do you have any other questions about your employment?"
            }
        elif self.conversation_state.get("context") == "onboarding":
            if "name is " not in self.conversation_state:
                self.conversation_state["name"] = message
                return {
                    "content": "To get started with your onboarding, please provide your full name."
                }
            elif "address is " not in self.conversation_state:
                self.conversation_state["address"] = message
                return {"content": "Thank you! Now, please provide your address."}
            elif "email is " not in self.conversation_state:
                self.conversation_state["email"] = message
                return {"content": "Thank you! Now, please provide your email address."}
            elif "mobile number is " not in self.conversation_state:
                self.conversation_state["mobile_number"] = message
                return {"content": "Thank you! Now, please provide your mobile number."}
            elif "documentation is " not in self.conversation_state:
                self.conversation_state["documentation"] = message
                return {
                    "content": "Thank you! Finally, please provide any necessary documentation for the background check."
                }
            else:
                self.conversation_state["documentation"] = message
                self.store_information_skill.execute(self.conversation_state)
                return {
                    "content": "Thank you for providing the documentation. I'll transfer you to our Background Check Assistant for further verification."
                }
        elif self.conversation_state.get("context") == "company policies":
            return {
                "content": "HR Assistant here! We have various policies related to work hours, leave, and conduct. Can you specify which policy you are interested in?"
            }
        else:
            return {
                "content": "HR Assistant here! How can I help you with your employment or HR-related questions?"
            }

    def background_check_response(self, message):
        if "background check" in message.lower() or "documentation" in message.lower():
            return {
                "content": "For the background check, please provide your passport and police clearance certificate."
            }
        else:
            if (
                "passport" not in self.conversation_state
                or "police_clearance" not in self.conversation_state
            ):
                self.conversation_state["passport"] = message
                return {
                    "content": "Background Check Assistant here! We need your passport and police clearance certificate to proceed with the onboarding."
                }
            else:
                return {
                    "content": "Background Check Assistant here! Please provide the details you need assistance with."
                }

    def it_assistant_response(self, message):
        if "login details" in message.lower():
            if (
                "passport" not in self.conversation_state
                or "police_clearance" not in self.conversation_state
            ):
                return {
                    "content": "We cannot provide the login credentials until the background check is complete. Please provide your passport and police clearance certificate."
                }
            return {
                "content": "I can help you with your IT login details. Please provide your email address, and I'll get the necessary information for you."
            }
        elif "tech issue" in message.lower():
            return {
                "content": "Please describe the tech issue you're experiencing, and I'll assist you in resolving it."
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

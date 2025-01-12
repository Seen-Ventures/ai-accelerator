# AutoGen Studio: A Deep Dive into Multi-Agent Workflow Design

This README serves as a comprehensive guide to AutoGen Studio, a user-friendly interface built upon the AutoGen framework for prototyping and testing multi-agent applications. AutoGen Studio empowers you to design, manage, and interact with agents, enabling rapid experimentation with complex workflows.

## Getting Started

### 1. LLM Provider Setup

Before diving into AutoGen Studio, you need an LLM provider. This example uses OpenAI's `gpt-4-1106-preview` model, but the process is adaptable to other compatible LLMs.

- **Obtain API Key:** Retrieve your OpenAI API key from your OpenAI account.

- **Environment Variable (or Direct Specification):**

  You can set your API key as an environment variable:

  ```bash
  export OPENAI_API_KEY=<your_openai_api_key>
  ```

  Alternatively, specify the model details directly within the AutoGen Studio interface:

  **Image 1:** !["Model Specification" window showing the `gpt-4-1106-preview` model selected, the API key field filled (obfuscated), and the "Test Model" button.](https://drive.google.com/uc?export=view&id=1FkxeuuxzIZ7Jv3KP8nFjkZWCp37k5Kbg)

- **Important Note:** Ensure your API key is kept secure and never exposed publicly.

### 2. Installation

There are two primary installation methods:

- **pip (Recommended):** This is the simplest approach for most users.

  ```bash
  pip install autogenstudio
  ```

- **From Source (Developers):** This method is suitable if you intend to contribute to the AutoGen Studio codebase. It requires familiarity with React and Node.js (version 14.15.0 or later).

  1. Clone the repository: `git clone <repository_url>`
  2. Install Python dependencies: `pip install -e .`
  3. Navigate to the frontend directory: `cd samples/apps/autogen-studio/frontend`
  4. Install Node.js dependencies: `yarn install`
  5. Build the UI: `yarn build` (Windows users may need to consult the project's README for platform-specific instructions).

### 3. Launching the Application

Once installed, start AutoGen Studio using:

```bash
autogenstudio ui --port 8081
```

Access the UI in your browser at `http://localhost:8081/`.

**Image 2:** ![AutoGen Studio application running in a browser, showing the "Build" and "Playground" tabs.](https://drive.google.com/uc?export=view&id=1nl_8d9sERoj3d6vjCvco1caVSiW1WHMp)

## AutoGen Studio Interface: Building and Running Workflows

AutoGen Studio's interface comprises three main sections: **Build**, **Playground**, and **Gallery** (which will be explained later in a more advanced section). Let's focus on "Build" and "Playground" for now.

### Build Section: Defining Agents and Workflows

The **Build** section is where you define the core components of your multi-agent system:

- **Skills:** These represent reusable functions that agents can leverage to perform tasks. AutoGen Studio includes several pre-built skills; you can add your own as needed.

  **Image 3:** !["Skills" tab, highlighting one of the pre-built skills.](https://drive.google.com/uc?export=view&id=1fYlezietxr5hq9Iz-DLlE22jMSB5J-Ha)

- **Agents:** Create and configure your agents here. You specify agent names, descriptions, system messages (initial instructions), and importantly, the LLM they use (configured earlier or by choosing the model).

  **Image 4:** !["Agent Configuration" window, displaying the configuration options and an example like `welcome_assistant` with its description. Ensure that the fields `Agent Name`, `Agent Description`, `Max Consecutive Auto Reply`, `Human Input Mode`, and `System Message` are visible.](https://drive.google.com/uc?export=view&id=1LKgHE0GsBG00mLLwQrddyawQSIlaOW9P)

- **Workflows:** Define the interaction patterns between agents.

  - **Autonomous (Chat):** A simple initiator/receiver structure, common for chat-based interactions.
  - **Sequential:** Agents execute actions in a defined sequence.

  **Image 5:** ![Workflow configuration options ("Autonomous (Chat)" and "Sequential").](https://drive.google.com/uc?export=view&id=1P2HCJQ4hL34fNeNjavr0gTTh4a0mKWc2)

  For our example we will use the pre-built workflow "Onboarding Workflow" with "user_proxy" as the initiator and "group_onboarding_assistant" as the receiver.

  **Image 6:** !["Onboarding Workflow" Agent configuration showing "user_proxy" and "group_onboarding_assistant" selected as Initiator and Receiver respectively.](https://drive.google.com/uc?export=view&id=1Fxwhq3CmmfBkbjXwnbpssOwEuPTdEcYZ)

### Playground Section: Running Sessions and Monitoring Interactions

The **Playground** is where you run and interact with your defined workflows:

- **Sessions:** Launch new sessions by selecting a workflow, and optionally naming your session.

  **Image 7:** !["New Session" popup showing the selection of a workflow (like "Onboarding Workflow") and a text field for the session name.](https://drive.google.com/uc?export=view&id=1qg-APq4AUIjNZqZOZQAyAu3P3EplMlbj)

- **Chat View:** Monitor the conversations between agents in real-time. Observe the flow of messages and the output generated by each agent.

## Next Steps and Advanced Features

This overview covers the core functionalities of AutoGen Studio. Future sections will explore:

- **Gallery:** Managing and sharing your workflow configurations, skills, and agents.
- **Complex Workflows:** Implementing more sophisticated interactions, such as `GroupChat` for simultaneous multi-agent conversations.
- **Custom Skill Development:** Creating and integrating your own custom skills using Python.
- **Advanced Agent Configuration:** Deep dive into configuration options and utilizing advanced features.

Furthermore, the AutoGen Studio project welcomes contributions. Refer to the project's contribution guidelines for more information.

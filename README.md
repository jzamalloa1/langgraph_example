# Simple LangGraph Agent Example

This is a simple implementation of an agent using [LangGraph](https://github.com/langchain-ai/langgraph), a library for building stateful applications with LLMs. This example demonstrates how to create a basic agent that can process queries and execute actions in a structured way.

![Graph view in LangGraph studio UI](./static/studio_ui.png)

The agent's logic is implemented in `src/react_agent/graph.py`, showcasing a simple yet effective approach to building an AI agent that can process queries and perform actions.

## How it Works

This simple agent follows a straightforward process:

1. Receives a user **query** as input
2. Analyzes the query and determines what action to take
3. Executes the appropriate action using its available tools
4. Reviews the results of the action
5. Continues this cycle until it reaches a solution

The agent is intentionally kept simple while demonstrating the core concepts of LangGraph's state management and action execution capabilities.

## Setup

To get started with this example:

1. Create a `.env` file:
```bash
cp .env.example .env
```

2. Add your API keys to the `.env` file. You'll need one of the following:

For Anthropic Claude (default):
```
ANTHROPIC_API_KEY=your-api-key
```

For OpenAI:
```
OPENAI_API_KEY=your-api-key
```

3. Install dependencies and start exploring!

## Customization

This example can be easily modified to suit your needs:

1. **Add tools**: Create new tools in [tools.py](./src/react_agent/tools.py) to expand the agent's capabilities
2. **Change the model**: Switch between Anthropic's Claude or OpenAI's models by updating your environment variables
3. **Modify the prompt**: Adjust the agent's behavior by updating the prompt in [prompts.py](./src/react_agent/prompts.py)

## Further Development

The agent's core logic in [graph.py](./src/react_agent/graph.py) can be modified to:
- Add new steps to the decision-making process
- Implement different types of reasoning patterns
- Integrate additional tools and capabilities

For more information, check out the [LangGraph documentation](https://github.com/langchain-ai/langgraph) to learn about building more complex applications with this framework.

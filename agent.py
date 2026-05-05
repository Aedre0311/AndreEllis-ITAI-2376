from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from src.tools import get_weather, analyze_risk

def run_agent(user_input):

    tools = [
        Tool(
            name="Weather Tool",
            func=lambda x: get_weather("current location"),
            description="Provides weather conditions"
        ),
        Tool(
            name="Risk Analyzer",
            func=analyze_risk,
            description="Analyzes risk level"
        )
    ]

    llm = ChatOpenAI(temperature=0)

    memory = ConversationBufferMemory(memory_key="chat_history")

    agent = initialize_agent(
        tools,
        llm,
        agent="conversational-react-description",
        memory=memory,
        verbose=False
    )

    return agent.run(user_input)

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.agents import create_agent
from web_search import web_search

def main(topic: str) -> str:
    load_dotenv()
    model = ChatGroq(model="qwen/qwen3-32b", temperature=0)
    agent = create_agent(
    model=model,
    tools=[web_search],
    system_prompt="You are a helpful assistant who performs web searches to provide accurate information.",
    )
    response = agent.invoke(
    {"messages": [{"role": "user", "content": f"Perform web search and give information about {topic}"}]}
    )
    return response['messages'][-1].content
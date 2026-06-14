import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GEMINI_API_KEY")
)

async def main():
    print("Hello MCP Client")
    response = llm.invoke("Explain recursion in one paragraph.")
    print(response.content)

if __name__ == "__main__":
    asyncio.run(main())


import asyncio
from dotenv import load_dotenv
import os


# This provides the framework for a python application as an mcp client
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GEMINI_API_KEY")
)

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/Z005566R/Desktop/AI Projects/MCP/servers/math_server.py"]
)


async def main():
    print("Hello from mcp!")


if __name__ == "__main__":
    asyncio.run(main())

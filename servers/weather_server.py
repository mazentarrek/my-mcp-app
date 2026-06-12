from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location"""
    return "The weather is very sunny right here in Cairo"

if __name__ == "__main__":
    mcp.run(transport="sse")
"""
MCP Tools : Connect to composio MCP server for google calendar
"""
import os
from dotenv import load_dotenv  
load_dotenv()
from langchain_mcp_adapters.client import MultiServerMCPClient  

COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY","")
COMPOSIO_MCP_URL = os.getenv("COMPOSIO_MCP_URL","")
def get_mcp_client():
    """
    Get MCP client for composio mcp server
    """
    client = MultiServerMCPClient({
        
         "composio": {
            
            "url": COMPOSIO_MCP_URL,
            "transport": "streamable_http",
            "headers": {
                "x-api-key": COMPOSIO_API_KEY,
            },
        }
    })
    return client

async def get_calendar_tools(client: MultiServerMCPClient):
    """
    Get calendar tools for composio mcp server
    """
    tools = await client.get_tools()

    return [t for t in tools if "calendar" in t.name.lower()]

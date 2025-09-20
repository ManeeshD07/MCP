from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

def convert_to_llm_tool(tool):
    tool_schema = {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "type": "function",
            "parameters": {
                "type": "object",
                "properties": tool.inputSchema["properties"]
            }
        }
    }

    return tool_schema

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()
            # List available resources
            resources = await session.list_resources()
            print("LISTING RESOURCES")
            for resource in resources:
                print("Resource: ", resource)

            # List available tools
            tools = await session.list_tools()
            print("LISTING TOOLS")
            for tool in tools.tools:
                print("Tool: ", tool.name)
                print("Tool", tool.inputSchema["properties"])


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())


# from mcp import ClientSession, StdioServerParameters, types
# from mcp.client.stdio import stdio_client

# server_params = StdioServerParameters(
#     command= "mcp",
#     args=["run", "main.py"],
#     env = None,
# )

# async def run():
#     async with stdio_client(server_params) as (read, write):
#         async with ClientSession(read, write) as session: 
#             await session.initialize()

#             resources = await session.list_resources()
#             print("Listing Resources:")
#             for res in resources:
#                 print(" Resource - ", res)

#             tools = await session.list_tools()
#             print("Listing Tools:")
#             for tool in tools:
#                 print("Tool - ", tool)

#             # Read a resource
#             print("READING RESOURCE")
#             content = await session.read_resource("greeting://Maneesh")
#             for con in content:
#                 print("Content:", con)
#             # print("MIME Type:", mime_type)

#             # Call a tool
#             print("CALL TOOL")
#             result = await session.call_tool("add", arguments={"a": 1, "b": 7})
#             print(result.content)


# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(run())
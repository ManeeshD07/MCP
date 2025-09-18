from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command= "mcp",
    args=["run", "main.py"],
    env = None,
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session: 
            await session.initialize()

            resources = await session.list_resources()
            print("Listing Resources:")
            for res in resources:
                print(" Resource - ", res)

            tools = await session.list_tools()
            print("Listing Tools:")
            for tool in tools:
                print("Tool - ", tool)

            # Read a resource
            print("READING RESOURCE")
            content = await session.read_resource("greeting://Maneesh")
            for con in content:
                print("Content:", con)
            # print("MIME Type:", mime_type)

            # Call a tool
            print("CALL TOOL")
            result = await session.call_tool("add", arguments={"a": 1, "b": 7})
            print(result.content)


if __name__ == "__main__":
    import asyncio
    asyncio.run(run())
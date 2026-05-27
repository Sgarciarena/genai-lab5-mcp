import argparse
import asyncio

from fastmcp import FastMCP

mcp = FastMCP("Hello Server")


@mcp.tool(name="say_hello", description="Return a personalized greeting for the given name.")
def say_hello(name: str) -> str:
    return f"Hello, {name}!"


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    asyncio.run(mcp.run_http_async(host=host, port=port))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FastMCP hello server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    run_server(args.host, args.port)

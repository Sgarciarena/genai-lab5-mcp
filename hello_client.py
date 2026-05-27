import argparse
import asyncio

from fastmcp.client import Client


async def run_client_async(host: str = "127.0.0.1", port: int = 8000, name: str = "World") -> None:
    url = f"http://{host}:{port}/mcp"
    async with Client(url) as client:
        result = await client.call_tool("say_hello", {"name": name})

        if getattr(result, "content", None) is not None:
            texts = []
            for item in result.content:
                if getattr(item, "type", None) == "text":
                    texts.append(getattr(item, "text", ""))
                else:
                    texts.append(str(item))
            print("".join(texts))
        else:
            print(result)


def run_client(host: str = "127.0.0.1", port: int = 8000, name: str = "World") -> None:
    asyncio.run(run_client_async(host, port, name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FastMCP hello client.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--name", default="World",
                        help="Name to send to say_hello.")
    args = parser.parse_args()

    run_client(args.host, args.port, args.name)

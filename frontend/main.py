# for mcp
from langchain_mcp_adapters.client import MultiServerMCPClient

# for agent
from langchain_openai import ChatOpenAI
from langchain.schema.runnable.config import RunnableConfig
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

# for ui
import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    client = MultiServerMCPClient(
        {
            "weather": {
                "url": "http://weather-tool:5000/mcp/",
                "transport": "streamable_http"
            }
        }
    )

    tools = await client.get_tools()
    print(f"Available tools: {tools}")

    model = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=""
    )

    graph = create_react_agent(model, tools)

    cl.user_session.set("graph", graph)


@cl.on_message
async def on_message(msg: cl.Message):
    config = {"configurable": {"thread_id": cl.context.session.id}}
    cb = cl.LangchainCallbackHandler()
    final_answer = cl.Message(content="")
    graph = cl.user_session.get("graph")

    async for msg, metadata in graph.astream(
        {"messages": [HumanMessage(content=msg.content)]},
        stream_mode="messages",
        config=RunnableConfig(callbacks=[cb], **config)
    ):
        if (
            msg.content
            and not isinstance(msg, HumanMessage)
            # and metadata["langgraph_node"] == "final"
        ):
            await final_answer.stream_token(msg.content)

    await final_answer.send()
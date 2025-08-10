# Weather Forecasting Agent using Chainlit, Langgraph and MCP

## Overview
The Weather Forecasting Agent is an application that leverages a **AI agent** to forecast the upcoming weather for a specific town in the US. The application demonstrates how the **Agent** leverages the use of a tool using **Model Context Protocol** (MCP) to communicate with a weather API.

## High-Level Architecture
The architecture is designed to be modular:

- All application components are containerized using **Docker**
- The agent tool for weather forecasting is available as MCP ([Model Context Protocol](https://github.com/modelcontextprotocol)) server and is called using a MCP client
- The MCP server is implemented in **Python** using the **FastMCP** framework.
- The agent workflow is generated using the prebuilt [**Langgraph ReAct**](https://github.com/langchain-ai/react-agent) framework
- The interface is provided using [**Chainlit**](https://github.com/Chainlit/chainlit)

## Features
- One AI agent
- Chainlit interface
- Weather MCP tool

## One script setup
> [!IMPORTANT]
> You need an valid OpenAI API key to use this repository

In order to run the application locally, ensure you have the following installed:
- **[Git](https://git-scm.com/downloads)**
- **[Docker](https://www.docker.com/)**

Go into the directory and run **docker compose up**:
- It will build two containers (one for the frontend, one for the MCP tool)
- uv manages the python requirements for the container
- The frontend should be exposed to port 8000

## Contributing
I welcome contributions to this repository in any way! :)

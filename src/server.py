## Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
## SPDX-License-Identifier: Apache-2.0

import argparse
import os
import sys

from fastmcp import FastMCP
from loguru import logger

from .constant import MCP_SERVER_VERSION
from .rabbitmq.module import RabbitMQModule


class RabbitMQMCPServer:
    def __init__(self, allow_mutative_tools: bool, management_port: int | None = None):
        # Setup logger
        logger.remove()
        logger.add(sys.stderr, level=os.getenv("FASTMCP_LOG_LEVEL", "WARNING"))
        self.logger = logger

        # Initialize FastMCP
        self.mcp = FastMCP(
            "mcp-server-rabbitmq",
            instructions="""Manage RabbitMQ message brokers and interact with queues and exchanges.""",
        )

        rmq_module = RabbitMQModule(self.mcp)
        rmq_module.default_management_port = management_port
        rmq_module.register_rabbitmq_management_tools(allow_mutative_tools)

        # Try to auto-connect on startup (will fail gracefully if port-forward is not active yet)
        rmq_module.try_auto_connect()

    def run(self):
        """Run the MCP server."""
        self.logger.warning(f"Starting RabbitMQ MCP Server v{MCP_SERVER_VERSION}")
        self.mcp.run()


def main():
    """Run the MCP server with CLI argument support."""
    parser = argparse.ArgumentParser(
        description="A Model Context Protocol (MCP) server for RabbitMQ"
    )
    parser.add_argument(
        "--allow-mutative-tools",
        action="store_true",
        help="Enable tools that can mutate the states of RabbitMQ",
    )
    
    # Get default management port from env if available
    default_mgmt_port = os.getenv("RABBITMQ_MANAGEMENT_PORT") or os.getenv("RMQ_MANAGEMENT_PORT")
    default_mgmt_port_val = int(default_mgmt_port) if default_mgmt_port else None

    parser.add_argument(
        "--management-port",
        type=int,
        default=default_mgmt_port_val,
        help="Default RabbitMQ Management API port (default: 443 for TLS, 15672 for non-TLS)",
    )

    args = parser.parse_args()

    # Create server with connection parameters from args
    server = RabbitMQMCPServer(args.allow_mutative_tools, args.management_port)

    # Run the server
    server.run()


if __name__ == "__main__":
    main()


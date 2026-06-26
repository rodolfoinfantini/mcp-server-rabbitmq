# RabbitMQ MCP Server
A [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) server implementation for RabbitMQ operation.

## Features

### Manage your RabbitMQ message brokers using AI agent
This MCP server wraps admin APIs of a RabbitMQ broker as MCP tools.

### Connect to multiple brokers in one session
Supports connecting to multiple RabbitMQ brokers within a single session, allowing you to manage multiple clusters simultaneously.

### Automatic & Resilient Environment-based Connection
Automatically connects to your default RabbitMQ broker on startup or dynamically on-demand using environment variables. Gracefully handles delayed or intermittent broker availability with lazy auto-reconnection.

### Seamless integration with MCP clients
Quickly launch using uv/uvx with zero manual configuration.


## Installation

### From source (Fork)
1. Clone this repository:
```bash
git clone git@github.com:rodolfoinfantini/mcp-server-rabbitmq.git
cd mcp-server-rabbitmq
```

2. Add it to your MCP client config (e.g. `claude_desktop_config.json`):

```json
{
    "mcpServers": {
      "rabbitmq": {
        "command": "uv",
        "args": [
            "--directory",
            "/absolute/path/to/mcp-server-rabbitmq",
            "run",
            "amq-mcp-server-rabbitmq",
            "--allow-mutative-tools"
        ],
        "env": {
            "RMQ_HOST": "localhost",
            "RMQ_PORT": "5673",
            "RMQ_USER": "your-user",
            "RMQ_PASS": "your-password",
            "RMQ_USE_TLS": "false",
            "RMQ_MANAGEMENT_PORT": "15673"
        }
      }
    }
}
```

## Configuration

### Environment Variables

You can configure the default automatic connection by defining the following environment variables:

- `RABBITMQ_HOST` or `RMQ_HOST`: RabbitMQ broker host/IP (e.g., `localhost` or `rabbitmq.prod.svc`).
- `RABBITMQ_USER` or `RMQ_USER`: Username for broker authentication.
- `RABBITMQ_PASS` or `RMQ_PASS`: Password for broker authentication.
- `RABBITMQ_PORT` or `RMQ_PORT`: AMQP port (default: `5671` for TLS, `5672` for non-TLS).
- `RABBITMQ_USE_TLS` or `RMQ_USE_TLS`: Enable/disable TLS (`true` or `false`, default: `false`).
- `RABBITMQ_MANAGEMENT_PORT` or `RMQ_MANAGEMENT_PORT`: Management HTTP API port (default: `443` for TLS, `15672` for non-TLS).

### CLI Arguments

- `--allow-mutative-tools`: Enable tools that can mutate the states of RabbitMQ (creating/deleting queues, publishing/purging messages, etc.). Default is `false`.
- `--management-port`: Overrides the default Management HTTP port.


## Development

### Setup Development Environment

```bash
# Clone the repository
git clone git@github.com:rodolfoinfantini/mcp-server-rabbitmq.git
cd mcp-server-rabbitmq

# Install package in editable mode
uv pip install -e .
```

### Running Tests

```bash
pytest
```

### Code Quality

This project uses ruff for linting and formatting:

```bash
# Run linter
ruff check .

# Run formatter
ruff format .
```

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.


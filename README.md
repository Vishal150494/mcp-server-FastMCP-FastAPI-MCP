# MCP Servers - FastMCP & FastAPI-MCP

A comprehensive project demonstrating **Model Context Protocol (MCP)** server implementations using **FastMCP** and **FastAPI-MCP**. This repository showcases different transport protocols (STDIO, HTTP) and practical use cases for building MCP-enabled tools.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Scenario 1: Calculator (STDIO)](#scenario-1-calculator-stdio)
  - [Scenario 2: Calculator (HTTP/FastAPI)](#scenario-2-calculator-httpfastapi)
  - [Scenario 3: FreeCodeCamp Feed (STDIO)](#scenario-3-freecodecamp-feed-stdio)
  - [Deployment: FreeCodeCamp Feed (HTTP)](#deployment-freecodecamp-feed-http)
- [VS Code Integration](#vs-code-integration)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project serves as a learning resource and reference implementation for building MCP servers. It demonstrates:

- **FastMCP**: Lightweight MCP server framework with STDIO and HTTP transport
- **FastAPI-MCP**: Integration of MCP with FastAPI for HTTP-based tools
- **Multiple Scenarios**: Real-world examples from basic arithmetic to RSS feed searching

## ✨ Features

### 🧮 Calculator MCP Servers
- **STDIO Transport** (Scenario 1): Direct process communication
- **HTTP Transport** (Scenario 2): RESTful API with FastAPI integration
- Operations: Add, Subtract, Multiply, Divide

### 📰 FreeCodeCamp Feed Searcher
- **STDIO Transport** (Scenario 3): Development version
- **HTTP Transport** (Deployment): Production-ready server
- Search FreeCodeCamp news articles by title/description
- Search FreeCodeCamp YouTube videos by title
- RSS-based feed parsing with configurable results

## 📁 Project Structure

```
mcp-servers/
├── .vscode/
│   ├── mcp.json              # VS Code MCP server configurations
│   └── settings.json         # VS Code workspace settings
├── Scenario1/
│   └── calculator.py         # Calculator MCP (STDIO)
├── Scenario2/
│   └── calculator_api.py     # Calculator MCP (HTTP/FastAPI)
├── Scenario3/
│   └── feed_mcp.py           # FreeCodeCamp Feed MCP (STDIO)
├── deployment/
│   ├── feed.py               # Production FreeCodeCamp Feed MCP (HTTP)
│   └── requirements_deploy.txt
├── tests/                    # Test files
├── .env                      # Environment variables (not tracked)
├── .gitignore
├── pyproject.toml            # Poetry dependencies
├── poetry.lock
└── README.md
```

## 🔧 Prerequisites

- **Python**: 3.13 or higher
- **Poetry**: For dependency management
- **Git**: For version control

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Vishal150494/mcp-server-FastMCP-FastAPI-MCP.git
cd mcp-servers
```

### 2. Install Dependencies

Using Poetry (recommended):

```bash
poetry install
```

Or using pip:

```bash
pip install -r deployment/requirements_deploy.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root:

```env
RSS_URL=https://www.freecodecamp.org/news/rss/
YOUTUBE_DEFAULT_URL=https://www.youtube.com/feeds/videos.xml?channel_id=
YOUTUBE_CHANNEL_ID=UC8butISFwT-Wl7EV0hUK0BQ
```

## ⚙️ Configuration

### VS Code MCP Configuration

The project includes `.vscode/mcp.json` for seamless integration with VS Code:

```json
{
    "servers": {
        "Calculator-STDIO": {
            "command": "path/to/.venv/Scripts/python.exe",
            "args": ["Scenario1/calculator.py"]
        },
        "Calculator-HTTP": {
            "command": "path/to/.venv/Scripts/python.exe",
            "args": ["-m", "uvicorn", "Scenario2.calculator_api:app", 
                     "--host", "localhost", "--port", "8080"]
        },
        "FreeCodeCamp-Feed-STDIO": {
            "command": "path/to/.venv/Scripts/python.exe",
            "args": ["Scenario3/feed_mcp.py"]
        }
    }
}
```

## 🚀 Usage

### Scenario 1: Calculator (STDIO)

Run the calculator MCP server with STDIO transport:

```bash
python Scenario1/calculator.py
```

**Available Tools:**
- `multiply(x: float, y: float)` - Multiply two numbers
- `add(x: float, y: float)` - Add two numbers
- `subtract(x: float, y: float)` - Subtract two numbers
- `divide(x: float, y: float)` - Divide two numbers

### Scenario 2: Calculator (HTTP/FastAPI)

Run the calculator as an HTTP API:

```bash
python -m uvicorn Scenario2.calculator_api:app --host localhost --port 8080
```

**API Endpoints:**
- `POST /multiply?x=123&y=456` - Returns: `{"Result": 56088.0}`
- `POST /add?x=10&y=20` - Returns: `{"Result": 30.0}`
- `POST /subtract?x=50&y=20` - Returns: `{"Result": 30.0}`
- `POST /divide?x=100&y=5` - Returns: `{"Result": 20.0}`

**Interactive Documentation:**
- Swagger UI: `http://localhost:8080/docs`
- ReDoc: `http://localhost:8080/redoc`

### Scenario 3: FreeCodeCamp Feed (STDIO)

Run the FreeCodeCamp feed searcher with STDIO:

```bash
python Scenario3/feed_mcp.py
```

**Available Tools:**
- `fcc_news_search(query: str, max_results: int = 5)` - Search FCC news articles
- `fcc_youtube_search(query: str, max_results: int = 5)` - Search FCC YouTube videos

### Deployment: FreeCodeCamp Feed (HTTP)

Run the production-ready HTTP version:

```bash
python deployment/feed.py
```

Server runs on `http://localhost:8003`

**Example Usage:**

```bash
# Search for Python-related articles
curl -X POST "http://localhost:8003/fcc_news_search?query=python&max_results=3"

# Search for JavaScript videos
curl -X POST "http://localhost:8003/fcc_youtube_search?query=javascript&max_results=5"
```

## 🔌 VS Code Integration

This project is configured for seamless integration with VS Code's MCP support:

1. Open the project in VS Code
2. The `.vscode/mcp.json` configuration will be automatically detected
3. MCP servers will be available in the VS Code MCP panel
4. Start/stop servers directly from the IDE

## 🛠️ Development

### Running Tests

```bash
poetry run pytest tests/
```

### Code Quality

The project uses:
- **Type hints** for better code clarity
- **Docstrings** for all public functions
- **Error handling** for robust operation

### Adding New MCP Servers

1. Create a new scenario folder (e.g., `Scenario4/`)
2. Implement your MCP server using FastMCP or FastAPI-MCP
3. Add configuration to `.vscode/mcp.json`
4. Update this README with usage instructions

## 📚 Dependencies

### Core Dependencies
- `fastmcp` (^2.13.1) - FastMCP framework
- `fastapi` (^0.123.0) - FastAPI web framework
- `fastapi-mcp` (^0.4.0) - FastAPI-MCP integration
- `uvicorn` (^0.38.0) - ASGI server
- `feedparser` (^6.0.12) - RSS feed parsing
- `python-dotenv` (^1.2.1) - Environment variable management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Vishal Hegde**
- GitHub: [@Vishal150494](https://github.com/Vishal150494)
- Email: vchegde.hegde@gmail.com

## 🙏 Acknowledgments

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - Protocol specification
- [FastMCP](https://github.com/jlowin/fastmcp) - FastMCP framework
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [FreeCodeCamp](https://www.freecodecamp.org/) - Educational content source

---

**Happy Coding! 🚀**

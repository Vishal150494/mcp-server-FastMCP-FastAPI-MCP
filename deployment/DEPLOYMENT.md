# FastMCP Cloud Deployment Guide

This guide will help you deploy your FreeCodeCamp Feed MCP server to FastMCP Cloud.

## Prerequisites

- FastMCP installed (`pip install fastmcp`)
- A FastMCP Cloud account (sign up at https://fastmcp.cloud)

## Deployment Steps

### 1. Prepare Your Environment

Create a `.env` file in the `deployment` folder (copy from `.env.example`):

```bash
cp .env.example .env
```

The `.env` file should contain:
```
RSS_URL=https://www.freecodecamp.org/news/rss/
YOUTUBE_DEFAULT_URL=https://www.youtube.com/feeds/videos.xml?channel_id=
YOUTUBE_CHANNEL_ID=UC8butISFwT-Wl7EV0hUK0BQ
```

### 2. Test Locally (Optional but Recommended)

Before deploying, test your server locally:

```bash
cd deployment
python feed.py
```

Your server should start on `http://localhost:8003`

### 3. Deploy to FastMCP Cloud

#### Option A: Using FastMCP CLI

```bash
# Navigate to deployment folder
cd deployment

# Login to FastMCP Cloud
fastmcp login

# Deploy your server
fastmcp deploy feed.py --name "FreeCodeCamp Feed Searcher"
```

#### Option B: Using the FastMCP Cloud Web Interface

1. Go to https://fastmcp.cloud
2. Sign in to your account
3. Click "New Server" or "Deploy"
4. Upload your `feed.py` file
5. Upload your `requirements_deploy.txt` file
6. Set environment variables:
   - `RSS_URL`: `https://www.freecodecamp.org/news/rss/`
   - `YOUTUBE_DEFAULT_URL`: `https://www.youtube.com/feeds/videos.xml?channel_id=`
   - `YOUTUBE_CHANNEL_ID`: `UC8butISFwT-Wl7EV0hUK0BQ`
7. Click "Deploy"

### 4. Get Your Deployment URL

After deployment, FastMCP Cloud will provide you with:
- A unique URL for your MCP server (e.g., `https://your-server.fastmcp.cloud`)
- An API key for authentication (if required)

### 5. Connect to Your Deployed Server

Update your local `mcp_config.json` to use the deployed server:

```json
{
  "mcpServers": {
    "FreeCodeCamp-Feed-Cloud": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://your-server.fastmcp.cloud"
      ]
    }
  }
}
```

## Files in This Deployment

- `feed.py` - Your MCP server code
- `requirements_deploy.txt` - Python dependencies
- `.env.example` - Environment variable template
- `.env` - Your actual environment variables (gitignored)

## Troubleshooting

### Server won't start
- Check that all environment variables are set correctly
- Verify that `requirements_deploy.txt` includes all dependencies
- Check the FastMCP Cloud logs for error messages

### Tools not working
- Ensure the RSS feeds are accessible from the cloud
- Check that the environment variables are properly loaded
- Verify the tool definitions in `feed.py`

## Available Tools

Your deployed server provides two tools:

1. **fcc_news_search** - Search FreeCodeCamp news articles
   - Parameters: `query` (str), `max_results` (int, default=5)
   
2. **fcc_youtube_search** - Search FreeCodeCamp YouTube videos
   - Parameters: `query` (str), `max_results` (int, default=5)

## Next Steps

- Monitor your server usage on the FastMCP Cloud dashboard
- Set up alerts for server downtime
- Consider adding more tools or features
- Share your MCP server URL with team members

## Support

- FastMCP Documentation: https://gofastmcp.com
- FastMCP Cloud: https://fastmcp.cloud
- GitHub Issues: https://github.com/jlowin/fastmcp

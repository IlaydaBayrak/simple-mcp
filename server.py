# server.py
from mcp.server.fastmcp import FastMCP
from app import reverse_text

# MCP örneğini “simple-mcp” adıyla oluştur
mcp = FastMCP("simple-mcp")

@mcp.tool()
async def reverse_text_tool(text: str) -> str:
    """
    MCP aracı: gelen metni ters çevirir.
    """
    return reverse_text(text)

if __name__ == "__main__":
    # stdio üzerinden MCP mesajlaşmasını başlat
    mcp.run(transport="stdio")

from mcp.server.fastmcp import FastMCP
#from mcp.server.fastmcp import mcptool
import os 

# Create an MCP server
mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "note.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.wite("")

# Make an MCP tool 
@mcp.tool() # decorator in Python
def add_note(message: str) -> str: # -> it will return some string 
    
    # Doc String
    """
    Append a new note to the sticky note file. 

    Arg:
        message (str): The note content to be added.

    Return: 
        str: Confirmation message indicating the note was saved. 

    """

    ensure_file()
    with open(NOTES_FILE, "a") as f: 
        f.write(message + "\n")
    return "Note saved!"


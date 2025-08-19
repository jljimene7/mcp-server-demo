from mcp.server.fastmcp import FastMCP
#from mcp.server.fastmcp import mcptool
import os 

# Create an MCP server
mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "note.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

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

@mcp.tool()
def read_notes() -> str:
    # Doc String
    """
    Read and return all notes from the sticky note file

    Return: 
        str: All notes as a single string separated by line breaks. 
            If no notes exist, a default messahe is return 

    """
    ensure_file()
    with open(NOTES_FILE, "r") as f: 
        content = f.read().strip() # strip removes any new line characters or white spaces at the end 
    return content or "No notes yet."

@mcp.resource("notes://latest")
def get_latest_note() -> str: 
    """
    Get the most recently added note from the sticky note file.

    Returns:
        str: The last note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f: 
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet"

@mcp.prompt()
def note_summary_prompt() -> str: 
    """
    Generate a prompt asking the AI to summarize all current notes.

    Returns:
        str: A prompt string that includes all notes and asks for a summary.
             If no notes exist, a message will be shown indicating that.
    """
       
    ensure_file()
    with open(NOTES_FILE, "r") as f: 
        content = f.read().strip()
    if not content: 
        return "There are no notes yet"
    
    return f"Summarize the current note: {content}"


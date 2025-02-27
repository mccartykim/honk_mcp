#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#     "mcp",
# ]
# ///

from mcp.server.fastmcp import FastMCP
import subprocess

mcp = FastMCP("Honk TTS")

@mcp.tool()
def say_message(message: str) -> dict:
    """Use the MacOS text-to-speech with the default voice to say the provided message"""
    subprocess.run(["say", message])
    return {'message': message, 'status': 'spoken'}

@mcp.tool()
def say_message_eddy(message: str) -> dict:
    """Use the MacOS text-to-speech with Eddy's voice to say the provided message.
    Eddy has a friendly, casual male voice."""
    subprocess.run(["say", "-v", "Eddy", message])
    return {'message': message, 'voice': 'Eddy', 'status': 'spoken'}

@mcp.tool()
def say_message_flo(message: str) -> dict:
    """Use the MacOS text-to-speech with Flo's voice to say the provided message.
    Flo has a cheerful, energetic female voice."""
    subprocess.run(["say", "-v", "Flo", message])
    return {'message': message, 'voice': 'Flo', 'status': 'spoken'}

@mcp.tool()
def say_message_grandma(message: str) -> dict:
    """Use the MacOS text-to-speech with Grandma's voice to say the provided message.
    Grandma has an elderly, warm female voice with a gentle pace."""
    subprocess.run(["say", "-v", "Grandma", message])
    return {'message': message, 'voice': 'Grandma', 'status': 'spoken'}

@mcp.tool()
def say_message_grandpa(message: str) -> dict:
    """Use the MacOS text-to-speech with Grandpa's voice to say the provided message.
    Grandpa has an elderly, wise-sounding male voice with a slower pace."""
    subprocess.run(["say", "-v", "Grandpa", message])
    return {'message': message, 'voice': 'Grandpa', 'status': 'spoken'}

@mcp.tool()
def say_message_reed(message: str) -> dict:
    """Use the MacOS text-to-speech with Reed's voice to say the provided message.
    Reed has a clear, neutral male voice suitable for narration."""
    subprocess.run(["say", "-v", "Reed", message])
    return {'message': message, 'voice': 'Reed', 'status': 'spoken'}

@mcp.tool()
def say_message_rocko(message: str) -> dict:
    """Use the MacOS text-to-speech with Rocko's voice to say the provided message.
    Rocko has a bold, gruff male voice with character."""
    subprocess.run(["say", "-v", "Rocko", message])
    return {'message': message, 'voice': 'Rocko', 'status': 'spoken'}

@mcp.tool()
def say_message_sandy(message: str) -> dict:
    """Use the MacOS text-to-speech with Sandy's voice to say the provided message.
    Sandy has a friendly, approachable female voice."""
    subprocess.run(["say", "-v", "Sandy", message])
    return {'message': message, 'voice': 'Sandy', 'status': 'spoken'}

@mcp.tool()
def say_message_shelley(message: str) -> dict:
    """Use the MacOS text-to-speech with Shelley's voice to say the provided message.
    Shelley has a smooth, articulate female voice."""
    subprocess.run(["say", "-v", "Shelley", message])
    return {'message': message, 'voice': 'Shelley', 'status': 'spoken'}

@mcp.tool()
def say_message_fred(message: str) -> dict:
    """Use the MacOS text-to-speech with Fred's voice to say the provided message.
    Fred has a deep, authoritative male voice."""
    subprocess.run(["say", "-v", "Fred", message])
    return {'message': message, 'voice': 'Fred', 'status': 'spoken'}

@mcp.tool()
def say_message_junior(message: str) -> dict:
    """Use the MacOS text-to-speech with Junior's voice to say the provided message.
    Junior has a young male voice with childlike qualities."""
    subprocess.run(["say", "-v", "Junior", message])
    return {'message': message, 'voice': 'Junior', 'status': 'spoken'}

@mcp.tool()
def say_message_kathy(message: str) -> dict:
    """Use the MacOS text-to-speech with Kathy's voice to say the provided message.
    Kathy has a clear, professional female voice."""
    subprocess.run(["say", "-v", "Kathy", message])
    return {'message': message, 'voice': 'Kathy', 'status': 'spoken'}

@mcp.tool()
def say_message_superstar(message: str) -> dict:
    """Use the MacOS text-to-speech with Superstar voice to say the provided message.
    Superstar has a dramatic, exaggerated voice with a theatrical quality."""
    subprocess.run(["say", "-v", "Superstar", message])
    return {'message': message, 'voice': 'Superstar', 'status': 'spoken'}

@mcp.tool()
def say_message_trinoids(message: str) -> dict:
    """Use the MacOS text-to-speech with Trinoids voice to say the provided message.
    Trinoids has a robotic, alien-like voice effect."""
    subprocess.run(["say", "-v", "Trinoids", message])
    return {'message': message, 'voice': 'Trinoids', 'status': 'spoken'}

@mcp.tool()
def say_message_bells(message: str) -> dict:
    """Use the MacOS text-to-speech with Bells voice to say the provided message.
    Bells has a melodic, musical quality with bell-like tones mixed with speech."""
    subprocess.run(["say", "-v", "Bells", message])
    return {'message': message, 'voice': 'Bells', 'status': 'spoken'}

def main():
    mcp.run()

if __name__ == "__main__":
    main()

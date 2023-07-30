import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "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"
models.HuggingFace.api_key = "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"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """you are and expert in large language model (llm) field and you will answer accordingly"""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.HuggingFace.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        max_tokens=1000,
        model="zelalt/Chatbot_T5-Prmtrs"
    )

    return bot_response, state

"""Utility & helper functions."""

from langchain.chat_models import init_chat_model
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI

def load_chat_model() -> BaseChatModel:
    """Load a chat model from a fully specified name.

    Args:
        fully_specified_name (str): String in the format 'provider/model'.
    """

    model = ChatOpenAI(
        model_name="gpt-4o",
        temperature=0.2
    )

    return model
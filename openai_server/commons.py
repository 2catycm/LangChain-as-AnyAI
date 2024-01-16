from pydantic import BaseModel, Field
from typing import List, Union


class Message(BaseModel):
    role: str = Field(
        description="The role of the messages author."
    )
    content: str | List[str] | None = Field(
        None,
        description="The contents of the message."
    )
    name: str | None = Field(
        None,
        description="An optional name for the participant. Provides the model information to differentiate between participants of the same role."
    )

class SystemMessage(Message):
    role: str = "system"

class UserMessage(Message):
    role: str = "user"

class AssistantMessage(Message):
    role: str = "assistant"
    tool_calls: List[dict] | None = Field(
        None,
        description="The tool calls generated by the model, such as function calls."
    )
    function_call: dict | None = Field(
        None,
        description="Deprecated and replaced by tool_calls. The name and arguments of a function that should be called, as generated by the model."
    )

class ToolMessage(Message):
    role: str = "tool"
    tool_call_id: str = Field(
        description="Tool call that this message is responding to."
    )

class FunctionMessage(Message):
    role: str = "function"

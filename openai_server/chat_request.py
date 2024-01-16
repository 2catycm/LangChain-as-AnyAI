from commons import *
class Message: pass 
class ResponseFormat: pass 
class Tool: pass 
class ToolChoice: pass 
class FunctionCall: pass 
class Function: pass 
class ChatRequest(BaseModel):
    messages: list[Message] = Field(
        description="A list of messages comprising the conversation so far.",
    )
    model: str = Field(
        description="ID of the model to use. See the model endpoint compatibility table for details on which models work with the Chat API."
    )
    frequency_penalty: float | None = Field(
        0,
        description="Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.",
    )
    logit_bias: dict | None = Field(
        None,
        description="Modify the likelihood of specified tokens appearing in the completion.",
    )
    logprobs: bool | None = Field(
        False,
        description="Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the content of message. This option is currently not available on the gpt-4-vision-preview model.",
    )
    top_logprobs: int | None = Field(
        None,
        description="An integer between 0 and 5 specifying the number of most likely tokens to return at each token position, each with an associated log probability. logprobs must be set to true if this parameter is used.",
    )
    max_tokens: int | None = Field(
        None,
        description="The maximum number of tokens that can be generated in the chat completion."
    )
    n: int | None = Field(
        1,
        description="How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep n as 1 to minimize costs.",
    )
    presence_penalty: float | None = Field(
        0,
        description="Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.",
    )
    response_format: dict | None = Field(
        None,
        description="An object specifying the format that the model must output. Compatible with gpt-4-1106-preview and gpt-3.5-turbo-1106."
    )
    seed: int | None = Field(
        None,
        description="This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed, and you should refer to the system_fingerprint response parameter to monitor changes in the backend.",
    )
    stop: str | list | None = Field(
        None,
        description="Up to 4 sequences where the API will stop generating further tokens."
    )
    stream: bool | None = Field(
        False,
        description="If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a data: [DONE] message."
    )
    temperature: float | None = Field(
        1,
        description="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic."
    )
    top_p: float | None = Field(
        1,
        description="An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered."
    )
    tools: list[Tool] | None = Field(
        None,
        description="A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for.",
    )
    tool_choice: str | dict | None = Field(
        None,
        description="Controls which (if any) function is called by the model. none means the model will not call a function and instead generates a message. auto means the model can pick between generating a message or calling a function. Specifying a particular function via {'type': 'function', 'function': {'name': 'my_function'}} forces the model to call that function."
    )
    user: str | None = Field(
        None,
        description="A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. Learn more.",
    )
    function_call: str | dict | None = Field(
        None,
        description="Deprecated in favor of tool_choice. Controls which (if any) function is called by the model. none means the model will not call a function and instead generates a message. auto means the model can pick between generating a message or calling a function. Specifying a particular function via {'name': 'my_function'} forces the model to call that function.",
    )
    functions: list[Function] | None = Field(
        None,
        description="Deprecated in favor of tools. A list of functions the model may generate JSON inputs for.",
    )
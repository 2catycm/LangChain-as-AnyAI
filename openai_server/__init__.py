from fastapi import FastAPI, HTTPException, Body
from chat_completion import ChatCompletion
from chat_request import ChatRequest

app = FastAPI()
@app.post("/v1/chat/completions")
async def chat_completions(request: ChatRequest):
    try:
        openai_url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {YOUR_OPENAI_API_KEY}",
        }

        response = requests.post(openai_url, json=request.dict(), headers=headers)
        response.raise_for_status()
        chat_response = response.json()

        if request.stream:
            # Streaming response
            chat_completion_chunk = ChatCompletionChunk(**chat_response)
            return chat_completion_chunk
        else:
            # Regular response
            chat_response_object = ChatCompletion(**chat_response)
            return chat_response_object

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
import pytest

from openai import OpenAI

from openai_server import ChatCompletion

# 测试模式，如果为True，测试官方 OpenAI 服务器
# 否则则是测试本项目产生的兼容服务器
official = True
project_name = "LangChain-as-AnyAI"
client = None


def setup_module():
    global client
    if official:
        # 从环境变量读取
        # api_key from OPENAI_API_KEY
        # organization from OPENAI_ORG_ID
        client = OpenAI()
        return
    # 测试我们项目的server
    # 1. 首先要启动一个server

    base_url = "http://"  # TODO
    # 2. 然后根据server的url，创建client
    client = OpenAI(
        base_url=base_url,
        api_key=f"sk-{project_name}",
        organization=f"org-{project_name}",
    )  # 这是特殊的key和特殊的org，当接收到这个key和org的时候，我们的client应当返回项目名称。


# def test_chat_stream():
#     stream = client.chat.completions.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": "Say this is a test"}],
#         stream=True,
#     )
#     for chunk in stream:
#         if chunk.choices[0].delta.content is not None:
#             print(chunk.choices[0].delta.content, end="")


class TestCreateChatCompletion:
    def test_default(self):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"},
            ],
        )
        print(response) # ChatCompletion 对象，同时也类似于字典
        print(response.choices[0].message)
        completion = ChatCompletion(**response.dict())
        print(completion)

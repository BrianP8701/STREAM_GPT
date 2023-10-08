from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# llm = OpenAI(openai_api_key="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")

llm = OpenAI()
chat_model = ChatOpenAI()

print(type(llm))

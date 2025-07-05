import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model

# config
load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")

model = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")


# messages
messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]


# output
print(model.invoke(messages))
for token in model.stream(messages):
    print(token.content, end=" | ")
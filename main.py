import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from data.system_templates import system_prompts
from data.me import me


# config
load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
model = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")


# prompt
# system_template = system_prompts.get("translate")
system_template = str(me.items())

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), 
     ("user", "{text}")]
)

user_text = "give me life advice.  summarize in 2 sentences"
# prompt = prompt_template.invoke({"language": "French", "text": "hi!"})
prompt = prompt_template.invoke({"text": user_text})


# output

# print(prompt)
# print(prompt.to_messages())

response = model.invoke(prompt)
print(response.content)



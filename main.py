import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from data.me import me
from write_to_file import write_to_file


# config
load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
model = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")


# prompt
system_template = str(me.items())

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), 
     ("user", "{text}")]
)


# input
user_text = "give me life advice.  summarize in 2 sentences"
prompt = prompt_template.invoke({"text": user_text})


# output
response = model.invoke(prompt)
output_text = response.content

write_to_file(output_text)
print("wrote response to output.txt")
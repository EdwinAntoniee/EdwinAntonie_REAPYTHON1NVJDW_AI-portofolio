from config.openai_config import get_llm
from prompts.bidang_prompts import health_prompt

llm = get_llm(temperature=0) 

health_agent = health_prompt | llm

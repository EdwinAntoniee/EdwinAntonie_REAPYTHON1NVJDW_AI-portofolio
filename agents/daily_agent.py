from config.openai_config import get_llm
from prompts.bidang_prompts import daily_prompt

llm = get_llm(temperature=0.8) 

daily_agent = daily_prompt | llm
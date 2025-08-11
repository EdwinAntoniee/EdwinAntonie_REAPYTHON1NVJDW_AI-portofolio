from config.openai_config import get_llm
from prompts.bidang_prompts import finance_prompt

llm = get_llm(temperature=0.5)

finance_agent = finance_prompt | llm

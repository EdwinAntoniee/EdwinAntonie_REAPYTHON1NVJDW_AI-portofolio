from config.openai_config import get_llm
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from prompts.bidang_prompts import (
    education_prompt, finance_prompt, health_prompt, daily_prompt
)

PROMPT_MAP = {
    "education": education_prompt,
    "finance": finance_prompt,
    "health": health_prompt,
    "daily": daily_prompt,
}

def get_agent_for_sector(sector: str, thread_id: str, memory_store: dict):
    sector = sector.lower()
    if sector not in PROMPT_MAP:
        raise ValueError(f"Sektor tidak dikenali: {sector}")
    if thread_id not in memory_store:
        memory_store[thread_id] = ConversationBufferMemory(memory_key="history", return_messages=True)
    memory = memory_store[thread_id]
    llm = get_llm()
    prompt = PROMPT_MAP[sector]
    chain = LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=False)
    return chain

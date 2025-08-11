import json
import os
import uuid

MEMORY_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'chat_memory.json')

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            return {}
        except json.JSONDecodeError:
            return {}

def save_memory(memory):
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

def get_threads(sector):
    memory = load_memory()
    if sector not in memory or not isinstance(memory[sector], dict):
        return {}
    return memory[sector]

def create_thread(sector, title=None):
    memory = load_memory()
    if sector not in memory or not isinstance(memory[sector], dict):
        memory[sector] = {}
    thread_id = str(uuid.uuid4())
    memory[sector][thread_id] = {
        "title": title or f"Thread {len(memory[sector])+1}",
        "messages": []
    }
    save_memory(memory)
    return thread_id

def get_chat_history(sector, thread_id):
    memory = load_memory()
    if sector in memory and isinstance(memory[sector], dict):
        thread = memory[sector].get(thread_id)
        if thread:
            return thread["messages"]
    return []

def add_chat_history(sector, thread_id, sender, message, timestamp=None):
    memory = load_memory()
    if sector not in memory or not isinstance(memory[sector], dict):
        memory[sector] = {}
    if thread_id not in memory[sector]:
        memory[sector][thread_id] = {"title": f"Thread {len(memory[sector])+1}", "messages": []}
    msg = {"sender": sender, "message": message}
    if timestamp:
        msg["timestamp"] = timestamp
    memory[sector][thread_id]["messages"].append(msg)
    save_memory(memory)

def get_thread_title(sector, thread_id):
    memory = load_memory()
    if sector in memory and isinstance(memory[sector], dict):
        thread = memory[sector].get(thread_id)
        if thread:
            return thread.get("title", thread_id)
    return thread_id

def rename_thread(sector, thread_id, new_title):
    memory = load_memory()
    if sector in memory and isinstance(memory[sector], dict):
        if thread_id in memory[sector]:
            memory[sector][thread_id]["title"] = new_title
            save_memory(memory)
            return True
    return False

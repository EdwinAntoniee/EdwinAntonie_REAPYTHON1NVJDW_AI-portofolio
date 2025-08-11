import streamlit as st
from core.router import get_agent_for_sector
from core.memory_handler import (
    get_threads, create_thread, get_chat_history, add_chat_history, get_thread_title, rename_thread
)
from utils.formatter import get_timestamp, bubble_chat
import time

if "lc_memory_store" not in st.session_state:
    st.session_state["lc_memory_store"] = {}

AGENTS = {
    "education": "🎓 Education",
    "finance": "💰 Finance",
    "health": "🩺 Health",
    "daily": "🗓️ Daily"
}

SAPAAN = {
    "education": "Halo! Saya siap membantu pertanyaan seputar pendidikan.",
    "finance": "Hai! Saya penasihat keuangan Anda. Silakan tanya apa saja.",
    "health": "Halo! Saya siap membantu pertanyaan kesehatan umum.",
    "daily": "Hai! Saya asisten harian Anda. Ada yang bisa dibantu?"
}

def rerun():
    if hasattr(st, "rerun"):
        st.rerun()
    else:
        st.experimental_rerun()

def show_home():
    st.title("🤖 AI:O Chatbot")
    st.markdown("Selamat datang! Silakan pilih agent yang ingin Anda ajak bicara:")
    cols = st.columns(len(AGENTS))
    for i, (key, label) in enumerate(AGENTS.items()):
        if cols[i].button(label):
            st.session_state['current_agent'] = key
            st.session_state['page'] = 'chat'
            rerun()
    st.markdown("---")
    st.info("Pilih salah satu agent di atas untuk memulai chat.")

def show_sidebar(agent_key):
    st.sidebar.markdown("## Navigasi")
    if st.sidebar.button("🏠 Home"):
        st.session_state['page'] = 'home'
        rerun()
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Threads")
    threads = get_threads(agent_key)
    if st.sidebar.button("➕ Thread Baru"):
        thread_id = create_thread(agent_key)
        st.session_state['current_thread'] = thread_id
        rerun()
    for tid, thread in threads.items():
        label = thread.get("title", tid)
        if st.sidebar.button(label, key=f"thread_{tid}"):
            st.session_state['current_thread'] = tid
            rerun()
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Chat Room Lainnya")
    for key, label in AGENTS.items():
        if key != agent_key:
            if st.sidebar.button(label, key=f"sidebar_{key}"):
                st.session_state['current_agent'] = key
                threads = get_threads(key)
                st.session_state['current_thread'] = next(iter(threads), None)
                st.session_state['page'] = 'chat'
                rerun()

def show_chatroom(agent_key):
    show_sidebar(agent_key)
    st.title(f"{AGENTS[agent_key]}")
    st.markdown(f"_{SAPAAN[agent_key]}_")
    threads = get_threads(agent_key)
    thread_id = st.session_state.get('current_thread')
    if not thread_id or thread_id not in threads:
        if threads:
            thread_id = next(iter(threads))
            st.session_state['current_thread'] = thread_id
        else:
            st.info("Belum ada thread. Buat thread baru di sidebar.")
            return
    # --- Thread title with rename option ---
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        st.subheader(threads[thread_id].get("title", thread_id), anchor=False)
    with col2:
        if st.button("✏️", key="rename_thread_btn"):
            st.session_state['renaming_thread'] = True
    if st.session_state.get('renaming_thread', False):
        new_title = st.text_input("Ganti nama thread", value=threads[thread_id].get("title", thread_id), key="rename_thread_input")
        col_save, col_cancel = st.columns(2)
        with col_save:
            if st.button("Simpan", key="save_rename_thread"):
                if new_title.strip():
                    rename_thread(agent_key, thread_id, new_title.strip())
                st.session_state['renaming_thread'] = False
                rerun()
        with col_cancel:
            if st.button("Batal", key="cancel_rename_thread"):
                st.session_state['renaming_thread'] = False
                rerun()
    # --- End rename UI ---

    history = get_chat_history(agent_key, thread_id)
    chat_placeholder = st.container()
    with chat_placeholder:
        for item in history:
            timestamp = item.get("timestamp", "")
            st.markdown(
                bubble_chat(item["message"], item["sender"], timestamp),
                unsafe_allow_html=True
            )
    user_input = st.chat_input("Ketik pesan Anda di sini...")
    if user_input:
        ts = get_timestamp()
        add_chat_history(agent_key, thread_id, "User", user_input, ts)
        agent = get_agent_for_sector(agent_key, thread_id, st.session_state["lc_memory_store"])
        # --- Streaming response ---
        response = agent.run(user_input)
        ts_bot = get_timestamp()
        # Streaming effect
        bot_placeholder = st.empty()
        displayed = ""
        for word in response.split():
            displayed += word + " "
            bot_placeholder.markdown(
                bubble_chat(displayed.strip(), "Bot", ts_bot),
                unsafe_allow_html=True
            )
            time.sleep(0.04)  # Adjust speed as needed
        add_chat_history(agent_key, thread_id, "Bot", response, ts_bot)
        rerun()

def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'
    if 'current_agent' not in st.session_state:
        st.session_state['current_agent'] = None
    if 'current_thread' not in st.session_state:
        st.session_state['current_thread'] = None

    if st.session_state['page'] == 'home':
        show_home()
    elif st.session_state['page'] == 'chat' and st.session_state['current_agent']:
        show_chatroom(st.session_state['current_agent'])
    else:
        st.session_state['page'] = 'home'
        rerun()
if __name__ == "__main__":
    main()
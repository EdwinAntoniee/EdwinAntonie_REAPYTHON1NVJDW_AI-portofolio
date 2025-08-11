# 🤖 AI:O Chatbot

AI:O adalah aplikasi chatbot berbasis AI yang mampu membantu pengguna dalam berbagai bidang, seperti pendidikan, keuangan, kesehatan, dan kebutuhan harian. Dibangun menggunakan [Streamlit](https://streamlit.io/) dan [LangChain](https://python.langchain.com/), AI:O memanfaatkan teknologi GPT dari OpenAI untuk memberikan jawaban yang relevan, edukatif, dan mudah dipahami.

---

## ✨ Fitur Utama

- **Multi-Agent Chatbot:** Pilih agent sesuai kebutuhan: Education, Finance, Health, atau Daily Assistant.
- **Threaded Chat:** Simpan dan kelola percakapan dalam thread berbeda untuk setiap bidang.
- **UI Interaktif:** Tampilan modern dengan bubble chat dan sidebar navigasi.
- **Custom Prompt:** Setiap agent memiliki prompt khusus untuk hasil yang lebih relevan.
- **Memory Handler:** Riwayat chat tersimpan otomatis dan dapat diakses kembali.

---

## 🚀 Cara Menjalankan

1. **Clone repository ini**
2. **Install dependencies**  
   Jalankan perintah berikut di terminal:
   ```sh
   pip install -r requirements.txt
   ```
3. **Set API Key OpenAI**  
   Buat file `.env` di root folder dan tambahkan:
   ```
   OPENAI_API_KEY=sk-xxxxxx
   ```
4. **Jalankan aplikasi**
   ```sh
   streamlit run streamlit_app.py
   ```

---

## 🗂️ Struktur Folder

```
AI-O/
│
├── agents/           # Agent untuk tiap bidang (education, finance, dll)
├── config/           # Konfigurasi API dan model
├── core/             # Handler memory & router agent
├── data/             # Penyimpanan chat history
├── prompts/          # Prompt khusus tiap bidang
├── utils/            # Utility (formatter, dll)
├── streamlit_app.py  # Main app
├── requirements.txt
└── readme.md
```

---

## 🧑‍💻 Teknologi yang Digunakan

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [OpenAI GPT-3.5 Turbo](https://platform.openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📚 Cara Penggunaan

1. Pilih bidang (agent) yang ingin digunakan di halaman utama.
2. Buat thread baru atau lanjutkan percakapan yang sudah ada.
3. Ketik pertanyaan atau permintaan Anda di chat input.
4. Nikmati jawaban AI yang relevan sesuai bidang!

---

## 📦 Lisensi

Proyek ini dibuat untuk tujuan pembelajaran dan pengembangan. Silakan gunakan, modifikasi, dan kembangkan sesuai kebutuhan.

---

## 🙏 Kontribusi

Kontribusi sangat terbuka! Silakan buat pull request atau laporkan issue jika menemukan bug atau ingin menambah fitur.

---
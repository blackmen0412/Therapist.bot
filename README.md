# 🧠 AI Therapist Chatbot

An AI-powered therapist chatbot built using **Google Gemma 3 1B**, fine-tuned using **QLoRA (PEFT)** on a mental health conversation dataset. The project exposes the model through a **FastAPI REST API** for conversational inference.

> **Disclaimer:** This project is intended for educational and research purposes only. It is **not** a substitute for professional mental health care.

---

## ✨ Features

- 🤖 Fine-tuned Google Gemma 3 1B
- 🧠 QLoRA fine-tuning with PEFT
- 💬 Multi-turn conversation support
- ⚡ FastAPI REST API
- 🔄 Session-based chat history
- 🤗 Hugging Face model hosting

---

## 🛠️ Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- PEFT (QLoRA)
- FastAPI
- Uvicorn
- Hugging Face Hub

---

## 📂 Project Structure

```text
Therapist_Bot/
│
├── app.py
├── requirements.txt
├── README.md
└── ...
```

---

## 🤗 Model

The fine-tuned model is available on Hugging Face:

**https://huggingface.co/vivekkk999/therapist**

The API automatically downloads the model from Hugging Face during the first run.

---

## 📊 Dataset

Fine-tuned on the following Kaggle dataset:

**https://www.kaggle.com/datasets/zuhairhasanshaik/datacsv**

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/blackkite88/Therapist_Bot.git
cd Therapist_Bot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
uvicorn app:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST `/chat`

Request

```json
{
    "session_id": "user123",
    "message": "I've been feeling anxious lately."
}
```

Response

```json
{
    "response": "I'm sorry you're going through this. It sounds like you've been carrying a lot recently. Can you tell me what has been contributing to these feelings?"
}
```

---

## 🧠 Model Details

| Attribute | Value |
|-----------|--------|
| Base Model | Google Gemma 3 1B |
| Fine-tuning Method | QLoRA (PEFT) |
| Quantization | 4-bit NF4 |
| Framework | Hugging Face Transformers |
| API | FastAPI |
| Dataset | Mental Health Conversation Dataset |

---

## 🔮 Future Improvements

- Persistent conversation history (MongoDB/Redis)
- Retrieval-Augmented Generation (RAG)
- Conversation summarization for long chats
- Response streaming
- User authentication
- Cloud deployment with GPU acceleration

---

## ⚠️ Disclaimer

This chatbot is designed for supportive conversations and educational purposes only. It should not be used as a replacement for professional medical, psychiatric, or psychological advice, diagnosis, or treatment. If you or someone you know is experiencing a mental health crisis or is in immediate danger, seek help from local emergency services or a qualified mental health professional.

---

## 📄 License

This project is licensed under the MIT License.
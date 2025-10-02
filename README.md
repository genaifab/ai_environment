# AI Environment Setup Workshop

Welcome to **Workshop I: Setting Up Your AI Environment**.  
This is the first in a three-part workshop series designed to help non-technical people build the practical skills they need to become **AI leaders**.

---

## 📌 Workshop Overview

Being an AI leader doesn’t mean writing thousands of lines of code.  
It means having the confidence to:
- Understand how AI tools and systems fit together
- Guide projects that use AI
- Spot opportunities that others might miss

That confidence starts with knowing which tools your teams need to master for building AI apps.

In this first workshop, we’ll set up your AI environment, verify that everything is working, and take a short “test flight” to connect with an AI model.

By the end, you will:
- Have a fully working AI-ready environment
- Be able to run Python code inside VS Code with `uv` managing your environment
- Securely connect to an LLM API and send a simple request
- Launch and view a basic Streamlit web app
- Troubleshoot common setup issues
- Earn your **first badge** for a verified AI environment

---

## 🛠️ Workshop Stages

### **Stage 1: Installing and Verifying Tools**
- Install VS Code, `uv`, and Python  
- Learn the role each plays in your workflow  
- ✅ *Key Learning: A clean, working setup is the foundation of every AI project.*

### **Stage 2: Testing Your AI Connection**
- Add your API key with `.env`  
- Send a simple **“Hello, AI”** request and inspect the response  
- ✅ *Key Learning: Every AI project begins with a secure, working connection.*

### **Stage 3: Launching Your First App**
- Run a simple Streamlit app  
- Display an AI-generated response in your browser  
- ✅ *Key Learning: Even a minimal app shows how tools, APIs, and interfaces connect.*

---

## 📂 Repository Structure

```
├── stage1/
│   └── hello_world.py
├── stage2/
│   └── chat_connect.py
├── stage3/
│   └── app.py
├── .env.example
├── mac_setup_checklist.md
├── win_setup_checklist.md
├── setup_checklist_mac_win.md
├── pyproject.toml
└── README.md
```

---

## ⚡ Quick Start

1. Clone this repo  
   ```bash
   git clone https://github.com/your-username/ai-workshop.git
   cd ai-workshop
   ```

2. Sync dependencies with `uv`  
   ```bash
   uv sync
   ```

   This will:
   - Create a `.venv` (virtual environment)
   - Install all dependencies from `pyproject.toml`
   - Generate a `uv.lock` file with pinned versions

3. Copy `.env.example` → `.env` and add your API key  
   ```bash
   cp .env.example .env
   ```

4. Run Stage 1, 2, or 3 scripts as directed in the workshop. For example:  
   ```bash
   uv run python stage1/hello_world.py
   uv run python stage2/chat_connect.py
   uv run streamlit run stage3/app.py
   ```

---

## 🔄 Resetting Your Environment (Troubleshooting)

If your environment gets corrupted, you can reset it:

```bash
rm -rf .venv uv.lock
uv sync
```

Or force a reinstall:

```bash
uv sync --reinstall
```

---

## 🚀 Next Steps

After completing this workshop you are ready to move on to:
- **Workshop II**: Agentic coding with the latest tools  
- **Workshop III**: Building your first AI web app

---

## 🙏 Credits

Created as part of the **AI Essentials for Leaders** workshop series.  
Instructor: Alfred Essa, author of *AI: Shaping the Future of Innovation*.

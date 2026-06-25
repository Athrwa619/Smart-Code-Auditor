# 🤖 Smart Code Auditor

An industry-standard, multi-agent AI pipeline designed to automatically scan Python code for cybersecurity vulnerabilities and perform automated remediation.

## 🚀 The Problem
Developers often push code with hardcoded credentials or insecure command execution. Manually reviewing every line is slow and error-prone. This project solves that by using a multi-agent AI system to enforce security best practices.

## 🧠 How it Works (The Multi-Agent Workflow)
1. **Agent 1 (The Hacker):** Analyzes the raw code to identify specific cybersecurity threats (Command Injection, Hardcoded Secrets, etc.).
2. **Agent 2 (The Senior Dev):** Receives the audit report and automatically refactors the code to be production-ready and secure, using industry-standard libraries like `subprocess` and environment variables.

## 🛠️ Tech Stack
- **Backend:** FastAPI, Uvicorn
- **Frontend:** Streamlit
- **AI Engine:** LLaMA 3.1 via Groq API
- **Security Logic:** Multi-Agent Prompt Engineering

## ⚙️ How to Run
### Prerequisites
- Python 3.9+
- A [Groq API Key](https://console.groq.com/)

### Installation
1. Clone the repository: `git clone <your-repo-link>`
2. Create and activate your environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

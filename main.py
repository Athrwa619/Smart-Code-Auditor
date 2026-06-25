from fastapi import FastAPI, UploadFile, File
import uvicorn
import os
from dotenv import load_dotenv
from groq import Groq

# 1. Server Setup
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
app = FastAPI(title="Smart Code Auditor")

@app.get("/")
def home():
    return {"message": "Welcome to the Smart Code Auditor API!"}

@app.post("/upload-code/")
async def upload_code(file: UploadFile = File(...)):
    
    # A. Read the uploaded file
    code_bytes = await file.read()
    code_string = code_bytes.decode('utf-8')
    
    # ==========================================
    # 🕵️‍♂️ AGENT 1: THE HACKER
    # ==========================================
    hacker_prompt = f"You are a strict cybersecurity hacker. Find security flaws in this code and list them shortly:\n\n{code_string}"
    hacker_response = client.chat.completions.create(
        messages=[{"role": "user", "content": hacker_prompt}],
        model="llama-3.1-8b-instant",
    )
    hacker_report = hacker_response.choices[0].message.content

    # ==========================================
    # 👨‍💻 AGENT 2: THE SENIOR DEV (NEW!)
    # ==========================================
    dev_prompt = f"""You are an elite Senior Python Engineer. Read this hacker report:
{hacker_report}

Now, rewrite the original code to be 100% secure. 
CRITICAL RULES:
1. You MUST explicitly fix every single flaw listed by the hacker.
2. If the hacker suggests a safer alternative (like using subprocess.run instead of os.system), you MUST use it.
3. NEVER pass unsanitized user input directly to the operating system.

ONLY output the fixed python code, no talking:

{code_string}"""
    dev_response = client.chat.completions.create(
        messages=[{"role": "user", "content": dev_prompt}],
        model="llama-3.1-8b-instant",
    )
    fixed_code = dev_response.choices[0].message.content
    
    # ==========================================
    # Hand the complete package back to the user
    # ==========================================
    return {
        "filename": file.filename, 
        "audit_report": hacker_report,
        "fixed_code": fixed_code
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

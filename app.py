import streamlit as st
import requests
import os
# This tries to find the cloud address, or defaults to your computer if it can't find one
try:
    BACKEND_URL = st.secrets["BACKEND_URL"]
except:
    BACKEND_URL = "http://localhost:8501"
# 1. Decorate the Storefront
st.set_page_config(page_title="Smart Code Auditor", page_icon="🤖")
st.title("🤖 Smart AI Code Auditor")
st.markdown("Upload your Python script below. Our Multi-Agent AI will scan it for vulnerabilities and rewrite it securely.")

# 2. Add the Upload Box
uploaded_file = st.file_uploader("Choose a Python file", type=["py"])

# 3. What happens when the user clicks the button?
if uploaded_file is not None:
    if st.button("Run Security Audit"):
        
        # Show a loading spinner so the user knows it's working
        with st.spinner("The AI Assembly Line is processing your code..."):
            
            # Pack the file into the delivery truck
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            
            # Drive it to the FastAPI Factory
            # New line (using an f-string to combine your variable with the path)
            response = requests.post(f"{BACKEND_URL}/audit", files=files)
            
            # If the factory hands back a receipt successfully:
            if response.status_code == 200:
                data = response.json()
                
                st.success("Audit Complete!")
                
                # Print the Hacker's Report
                st.subheader("🕵️‍♂️ Agent 1: Hacker Report")
                st.markdown(data["audit_report"])
                
                # Print the Senior Dev's fixed code
                st.subheader("👨‍💻 Agent 2: Secured Code")
                st.code(data["fixed_code"], language="python")
            else:
                st.error("Oops! The delivery truck couldn't reach the backend factory.")

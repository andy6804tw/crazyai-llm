import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 設定 OpenAI API 金鑰與模型端點
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(base_url=endpoint, api_key=token)

# 單輪對話初始化的 system prompt
SYSTEM_PROMPT = {"role": "system", "content": "你是一個有用的助手。且會根據使用者輸入的語言做回應。"}

# 初始化對話歷史，僅用於顯示（不保存上下文）
if "display_messages" not in st.session_state:
    st.session_state.display_messages = []

# 顯示對話歷史
for message in st.session_state.display_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 接收使用者輸入
if user_input := st.chat_input("請輸入您的訊息..."):
    # 顯示使用者訊息
    st.session_state.display_messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 組合單輪對話訊息
    messages = [SYSTEM_PROMPT, {"role": "user", "content": user_input}]
    
    # 調用 OpenAI API 獲取回應
    response = client.chat.completions.create(
        messages=messages,
        model=model_name,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        streaming=True
    )

    # 獲取助理回應內容
    assistant_response = response.choices[0].message.content

    # 顯示助理回應
    st.session_state.display_messages.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

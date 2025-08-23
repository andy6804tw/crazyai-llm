import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# 載入 .env 文件中的環境變數
load_dotenv()

# 設定 OpenAI API 金鑰與模型端點
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# 最大餵入 GPT 的對話歷史長度
MAX_GPT_HISTORY = 3

# 定義系統指令內容
SYSTEM_PROMPT = """你是一個有用的助手。且會根據使用者輸入的語言做回應。"""

# 初始化對話歷史
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# 顯示對話歷史（保留所有歷史）
for message in st.session_state.messages:
    if message["role"] != "system":  # 系統訊息不顯示
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 接收使用者輸入
if user_input := st.chat_input("請輸入您的訊息..."):
    # 顯示使用者訊息
    with st.chat_message("user"):
        st.markdown(user_input)
    # 將使用者訊息添加到完整的顯示歷史
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 選擇最近 N 比歷史對話餵入 GPT
    gpt_messages = (
        [st.session_state.messages[0]]  # 保留 system prompt
        + st.session_state.messages[-MAX_GPT_HISTORY * 2:]  # 保留最近 N 比對話（每比對話包含 user 和 assistant 各一條）
    )
    print(f'Chat: {gpt_messages}')
    # 調用 OpenAI API 獲取回應
    response = client.chat.completions.create(
        messages=gpt_messages,
        model=model_name,
    )

    # 獲取助理回應內容
    assistant_response = response.choices[0].message.content

    # 顯示助理訊息
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    # 將助理訊息添加到完整的顯示歷史
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

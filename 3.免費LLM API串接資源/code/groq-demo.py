"""
【程式介紹】
這是一個以 Streamlit 為基礎的聊天機器人應用程式範例，透過整合 Groq 的 API 來進行對話。
1. 透過 Streamlit 建立網頁介面，顯示對話紀錄並提供使用者輸入框。
2. 程式會記錄並維持對話上下文，讓對話更連貫。
3. 特殊處理 <think> 區塊：將 AI 的思考過程與最終回應分開顯示。

【如何啟動這個應用程式】
1. 確認已經安裝 Streamlit 與 groq：
   pip install streamlit groq

2. 在 Groq 中申請自己的 API_KEY：
   API_KEY=你的_Groq_API_Key

3. 在終端機或命令提示字元中，進入此程式碼所在的資料夾，執行：
   streamlit run groq-demo.py

4. 瀏覽器將自動開啟 http://localhost:8501 顯示應用程式介面。
"""

import streamlit as st
from groq import Groq

# 初始化 Groq API
API_KEY = "你的API_KEY"
model_name = "deepseek-r1-distill-llama-70b"

# 建立 Streamlit 應用程式
st.title("💬 Groq Streamlit Chatbot")

# 建立聊天歷史紀錄
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "請使用繁體中文思考與回答user問題"},
    ]

# 顯示對話記錄
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        content = message["content"]

        # **確保 `<think>` 的內容不嵌套在 `st.chat_message` 內**
        if "<think>" in content and "</think>" in content:
            think_start = content.find("<think>") + len("<think>")
            think_end = content.find("</think>")
            think_text = content[think_start:think_end].strip()
            answer_text = content[think_end + len("</think>"):].strip()

            # **1️⃣ 顯示 AI 思考過程（不嵌套）**
            with st.expander("🤔 AI 思考過程", expanded=False):
                st.write(think_text)

            # **2️⃣ 顯示 AI 的最終回應**
            with st.chat_message("assistant"):
                st.write(answer_text)

        else:
            with st.chat_message("assistant"):
                st.write(content)

# 使用者輸入框
user_input = st.chat_input("請輸入您的問題...")

if user_input:
    # 顯示使用者輸入
    st.chat_message("user").write(user_input)

    # 儲存使用者輸入到歷史紀錄
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 建立 Groq 客戶端
    client = Groq(api_key=API_KEY)

    # 呼叫 API 取得回應
    completion = client.chat.completions.create(
        model=model_name,
        messages=st.session_state.messages,
        temperature=0.6,
        max_completion_tokens=1024,
        top_p=0.95,
        stream=True,  # 啟用流式輸出
        reasoning_format="raw"
    )

    # **改進部分：即時解析 <think> 區塊**
    response = ""
    think_text = ""
    answer_text = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
    print('------------')
    print(response)
    # **解析 `<think>` 區塊**
    if "<think>" in response and "</think>" in response:
        think_start = response.find("<think>") + len("<think>")
        think_end = response.find("</think>")
        think_text = response[think_start:think_end].strip()
        answer_text = response[think_end + len("</think>"):].strip()

        # **1️⃣ 顯示 AI 思考過程**
        with st.expander("🤔 AI 思考過程", expanded=False):
            st.write(think_text)

        # **2️⃣ 顯示 AI 的最終回應**
        with st.chat_message("assistant"):
            st.write(answer_text)

    else:
        with st.chat_message("assistant"):
            st.write(response)

    # 儲存 AI 回應到歷史紀錄
    st.session_state.messages.append({"role": "assistant", "content": response})

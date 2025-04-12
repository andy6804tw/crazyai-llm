import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 載入環境變數
load_dotenv()

# 設定 OpenAI API 金鑰與模型端點
token = '' # 請在 .env 檔中設定 API 金鑰，或直接填入金鑰字串
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

# 初始化 LangChain 的 ChatOpenAI 模型
llm = ChatOpenAI(
    temperature=1.0,
    model_name=model_name,
    openai_api_base=endpoint,
    openai_api_key=token,
    max_tokens=1000,
)

# 定義系統提示訊息
SYSTEM_PROMPT = "你是一個有用的助手。且會根據使用者輸入的語言做回應。"

# 初始化對話歷史 (僅用於顯示，不保存上下文)
if "display_messages" not in st.session_state:
    st.session_state["display_messages"] = []

# 顯示對話歷史
for message in st.session_state["display_messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 接收使用者輸入
if user_input := st.chat_input("請輸入您的訊息..."):
    # 顯示使用者訊息
    st.session_state["display_messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 建立對話訊息列表，使用 LangChain 的訊息格式
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_input)
    ]
    
    # 調用 LangChain 模型，使用 invoke 方法獲取回應
    response = llm.invoke(messages)
    assistant_response = response.content

    # 顯示助理回應
    st.session_state["display_messages"].append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

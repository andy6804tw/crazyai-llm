---
author: Tsai Yi Lin
date: 2025-02-19
tags:
  - Ollama
---

# 使用 Ollama API 整合 OpenAI Python 函式庫

範例程式：[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/andy6804tw/crazyai-llm/blob/main/docs/llm-practical/code/Ollama%20API%20整合%20OpenAI.ipynb)

## 前言
Ollama 提供了與 OpenAI API 部分功能的相容，協助現有應用程式連接到 Ollama。這篇教學文件將引導你如何利用 OpenAI 函式庫與 Ollama API 整合，進而快速切換不同家的大型語言模型（LLM）服務。利用 OpenAI 庫的優點在於，它相容市面上大多數 LLM 服務，只需替換 API URL，即可快速整合不同廠商的服務。

!!! info

    若要了解如何安裝 Ollama，請參考前一篇文章： [Ollama使用教學](Ollama使用教學.md)。

## 1. 環境設定與客戶端初始化
首先，我們需要安裝 OpenAI 函式庫：

```sh
pip install openai
```

接著透過下列程式碼初始化客戶端，並指定 API 伺服器的 URL 與金鑰。  
以下範例中使用的是本機伺服器（例如：http://localhost:11434/v1/ ），金鑰雖必填，但此處實際上不會使用。

```python
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',  # 設定 API 伺服器的 URL，這裡使用本機端點
    api_key='ollama',                      # API 金鑰（此例中為 'ollama'）
)
```

**說明：**  
這段程式碼將 OpenAI 模組引入，並根據指定的 URL 與金鑰建立 `client` 實例，以供後續 API 呼叫使用。


!!! note "如何在 Linux 讓 Ollama 服務允許遠端設備存取"
        目前的教學內容是使用 **localhost** 來做示範，因為執行這段程式的 Python 環境和部署 **Ollama 服務** 的機器是 **同一台電腦**，所以可以直接存取。  

        若有 **不同電腦** 需要 **遠端存取** Ollama 服務，請參考這篇文章進行設定： [如何在 Linux 讓 Ollama 服務允許遠端設備存取](https://andy6804tw.github.io/2025/02/22/ollama-service-remote-access/)

        **設定完成後**，即可透過：

        - **固定 IP** 直接連線存取  
        - **雲平台提供的 Port Forwarding URL** 來遠端存取服務  

---

## 2. Chat Completion API（對話生成）

### 2.1 純文字聊天

接下來，我們示範如何使用 Chat Completion API 聊天。此範例中，使用 `gemma2:9b` 模型，並傳送一則文字訊息。

```python
# 使用 chat API 建立一個聊天請求
chat_completion = client.chat.completions.create(
    messages=[
        {
            'role': 'user',  # 設定角色為「使用者」
            'content': '法國的首都在哪?',  # 提供要詢問的問題（提示詞）
        }
    ],
    model='gemma2:9b',  # 指定模型
)

# 取得模型回應的內容
print(chat_completion.choices[0].message.content)
```

**說明：**  
這裡我們傳送一個對話訊息，角色設定為 `user`，內容為「法國的首都在哪?」。API 將根據此訊息使用 `gemma2:9b` 模型產生對話的回應。

### 2.2 文字與影像混合輸入的聊天
Ollama 的 API 除了支援純文字外，還可支援影像輸入。以下範例展示如何同時傳送文字與以 base64 編碼的影像資料：

```py
import openai
import base64

# 讀取本機圖片並轉為 Base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# 圖片路徑
image_path = "./image.jpg"
base64_image = encode_image(image_path)
```

以下程式使用多模態模型，請先下載 llama3.2-vision:11b，並使用以下指令執行：
```sh
ollama run llama3.2-vision:11b
```

```python
response = client.chat.completions.create(
    model="llama3.2-vision:11b",  # 確保使用支援 Vision 的模型
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "這張圖片裡有什麼?"},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
            ]
        }
    ],
    max_tokens=300,
)

# 取得回應
print(response.choices[0].message.content)
```

**說明：**  
這段程式碼利用 `llama3.2-vision:11b` 模型進行對話，輸入內容同時包含一段文字訊息「這張圖片裡有什麼?」與一個以 base64 編碼表示的影像資料。`max_tokens` 參數限制了 API 回應的最大 token 數量，確保回應不會過長。

---

## 3. Completion API(單次問答)
若不需要多輪對話，也可以直接使用單次問答 API。以下範例以 prompt 提示「美國首都在哪裡?」並使用 `gemma2:9b` 模型取得提問結果：

```python
completion = client.completions.create(
    model="gemma2:9b", # 指定模型
    prompt="美國首都在哪裡?", # 提供要詢問的問題（提示詞）
)

# 取得模型回應的內容
print(completion.choices[0].text)
```

**說明：**  
此方法僅傳送一個 prompt，模型將依據輸入內容生成回應。

---

## 4. 模型操作
### 4.1 列出所有可用模型

你可以使用下列程式碼列出目前 API 支援的所有模型：

```python
from datetime import datetime

# 取得可用模型列表
list_completion = client.models.list()

# 轉換 Unix 時間戳
for model in list_completion.data:
    readable_time = datetime.utcfromtimestamp(model.created).strftime('%Y-%m-%d %H:%M:%S')
    print(f"模型 ID: {model.id}")
    print(f"建立時間: {readable_time}")
    print(f"類型: {model.object}")
    print(f"擁有者: {model.owned_by}")
    print("-" * 30)
```

**說明：**  
此指令會回傳一個包含所有可用模型資訊的清單，方便開發者了解目前有哪些模型可以使用。

### 4.2 取得特定模型資訊
若想查詢某一特定模型的詳細資訊，可使用：

```python
from datetime import datetime

model = client.models.retrieve("gemma2:9b")

print(f"模型 ID: {model.id}")
print(f"建立時間: {datetime.utcfromtimestamp(model.created):%Y-%m-%d %H:%M:%S}")
print(f"類型: {model.object}")
print(f"擁有者: {model.owned_by}")
```

**說明：**  
這裡以 `gemma2:9b` 為例，查詢該模型的詳細資訊，例如版本、能力等。

---

## 5. 產生 Embeddings
另一項常用的功能是利用 embeddings 將句子轉換為向量表示，這對於語意相似度、文本分類等應用非常有用。以下範例使用 `all-minilm` 模型來為兩個句子生成 embeddings：

```python
embeddings = client.embeddings.create(
    model="all-minilm",
    input=["why is the sky blue?", "why is the grass green?"],
)
```

**說明：**  
此段程式碼將兩個問題作為輸入，透過 `all-minilm` 模型計算其向量表示。這些向量可用於後續的相似度計算或其他自然語言處理任務。

---

## 總結

在這篇教學文件中，我們介紹了如何利用 OpenAI Python 函式庫與 Ollama API 介面進行應用整合，涵蓋的重點包括：

- **環境設定與客戶端初始化：** 如何指定 API 伺服器與金鑰。
- **對話生成 (Chat Completions)：** 包含純文字以及文字加影像混合輸入的範例。
- **單次問答 (Completions)：** 直接利用 prompt 進行文字生成。
- **執行多輪對話 (Run a multi-turn dialogue)：** 讓AI記錄下彼此的對話內容，維持連鎖的交流，例如聊天機器人或客戶支援應用程式。
- **模型操作：** 列出所有模型與查詢特定模型資訊。
- **Embeddings 產生：** 為輸入的文本生成向量表示。

使用 OpenAI 庫的優點在於它能夠與多數市面上 LLM 服務相容，只需修改 API URL，即可輕鬆切換不同供應商的服務。希望此篇文件能協助你在 Python 開發中快速上手 Ollama API 的整合應用。

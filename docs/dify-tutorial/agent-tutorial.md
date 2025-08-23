

# Dify Agent 教學：打造一個能思考又能動手的 AI 助理

在上一篇文章，我們已經學會如何在 **Dify 建立知識庫**，並以上傳電商常見問題資料，完成了一個 **電商問答知識庫**。今天，我們要更進一步，帶你認識 **Dify Agent**，並實作一個能「懂知識」又能「動手查資料」的小任務。

---

## 1. 為什麼要用 Agent？

單純的 RAG（檢索增強生成）可以回答知識，但它沒辦法幫你「執行任務」。
舉個例子：

* RAG 可以回答：「我們的網站支援哪些付款方式？」
* 但 RAG 沒辦法幫你「查詢用戶編號 2 的帳號資料」。

這就是 **Agent 的價值**：它能根據使用者問題，自己判斷是要 **查知識**，還是要 **呼叫工具（API）** 來動手處理。

---

## 2. Dify Agent 的組成

在 Dify 中，一個 Agent 由三個要素組成：

* **LLM**：用來理解問題、做出決策
* **Knowledge Base（知識庫）**：RAG 檢索文件答案
* **Tool（工具）**：讓 Agent 能「動手」，例如呼叫 API、查資料庫

我們今天的任務就是把這三個東西串起來，做一個小型的 **AI 助理**。

---

## 3. 實作範例任務

接下來我們要完成一個任務：

* 當使用者問「你們網站有支援貨到付款嗎？」 → Agent 要去 **知識庫** 找答案
* 當使用者問「幫我查 user\_id=2 的名字」 → Agent 要去 **API 工具** 查詢

### 3.1 建立一個具有 RAG 問答的 Agent

1. 在 Dify 後台，建立一個 **Agent 應用**
2. 在知識庫選擇 **上一篇文章建好的電商問答知識庫**
3. 測試一下：

   * 問「你們網站可以刷信用卡嗎？」
   * Agent 會從知識庫找到答案 → 「可以，我們支援信用卡付款。」

這樣就完成了第一步，讓 Agent 具備 **RAG 問答能力**。

---

### 3.2 讓 Agent 能夠呼叫外部 API

接著，我們要讓 Agent 具備「動手」能力，幫我們查詢用戶資料。

#### Step 1. 建立一個簡單的 FastAPI

先寫一個小小的 API 服務：

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/userinfo")
def get_userinfo(user_id: int):
    dummy_users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return {"id": user_id, "name": dummy_users.get(user_id, "Unknown")}
```

啟動伺服器：

```bash
uvicorn main:app --reload
```

然後在瀏覽器輸入：

```
http://localhost:8000/openapi.json
```

你會看到一坨 JSON Schema。這就是 FastAPI 自動生成的 **OpenAPI 規格**，裡面包含了 API 的路由、參數、回傳格式等等。

---

#### Step 2. 在 Dify 新增自定義工具

1. 進入 **工具 → 建立自定義工具**
2. 把剛剛的 **OpenAPI JSON** 貼上去
3. 你應該會看到「可用工具」那邊多了一些東西，就是我們在程式中定義的 `/userinfo` API

---

#### Step 3. 測試 Agent 呼叫 API

現在我們回到 Agent，重新測試：

* 問：「幫我查 user\_id=2 的名字」
* Agent 會自己判斷要呼叫 `/userinfo?user_id=2`
* 回答你：「這個使用者的名字是 Bob」

---

## 4. 總結

到這裡，我們完成了一個結合 **知識庫 + API 工具** 的 Dify Agent：

* 知識問答 → 查知識庫
* 資料查詢 → 呼叫 API

這樣的架構可以延伸到很多場景：

* 客服機器人：結合知識庫 + CRM API
* 工業 PdM：結合知識庫 + 即時感測數據 API
* 文件助理：結合知識庫 + Excel/DB 操作


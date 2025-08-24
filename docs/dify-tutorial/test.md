
---

## 

---

## 在 Agent 裡怎麼用？

* **引導使用者先選類別**
  使用者：「我想看筆電的商品」
  Agent：先提示可用類別（呼叫 `/categories`），若使用者指定「筆電」，再呼叫 `/products?category=筆電` 列出清單。

* **直接查庫存（單步）**
  使用者：「AirPods Pro 庫存多少？」
  Agent：直接呼叫 `/inventory?product_name=AirPods%20Pro`，將結果回覆。

### 建議的 System Prompt（片段）

```
你是門市商品助理。原則：
1) 若使用者未指定類別：先呼叫 /categories 提供可用類別；再請對方選擇。
2) 若已指定類別但未指定商品：呼叫 /products 並條列商品清單，讓使用者從中選。
3) 若使用者直接說商品名稱：呼叫 /inventory 查庫存並回覆數量與單位。
4) 找不到類別或商品時，請禮貌說明並引導正確選項。
```

---

## 測試用範例指令（可貼到 Dify 測試對話）

* 「有哪些商品種類可以查？」 → 期望呼叫 `/categories`
* 「幫我列出**配件**類有哪些商品」 → 期望呼叫 `/products?category=配件`
* 「查一下 **AirPods Pro** 的庫存」 → 期望呼叫 `/inventory?product_name=AirPods%20Pro`

---

\##（可選）本機快速測試 `curl`

```bash
# 1) 類別清單
curl "http://localhost:8000/categories"

# 2) 列出該類別的商品
curl "http://localhost:8000/products?category=筆電"

# 3) 查單一商品庫存
curl "http://localhost:8000/inventory?product_name=AirPods%20Pro"
```

---

這樣一來，你的 **Dify Agent** 就能：

* 先「**引導**」使用者挑類別 → 看清單
* 或者直接 **回答** 指定商品的庫存數量

之後若要接企業內部資料庫，只要把 `INVENTORY` 換成 DB/ERP 查詢邏輯即可，OpenAPI 描述不變，Dify 工具也能無痛沿用。

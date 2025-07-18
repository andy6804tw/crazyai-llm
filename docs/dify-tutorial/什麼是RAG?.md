# Build a Retrieval Augmented Generation (RAG) App
> 建置 RAG 問答應用程式

## 什麼是 RAG？  
RAG（Retrieval Augmented Generation）是一種將語言模型（LLM）的生成能力與檢索系統結合的技術。透過先從外部知識庫中檢索相關文件，再將檢索到的內容當作 prompt 的一部分，能讓模型回答私有資料或訓練截止後的新資訊相關問題。若模型不確定答案，就應直接回覆「我不知道」以確保回應真實可靠。

## RAG 核心概念  
- **索引（Indexing）**  
  1. **載入（Load）**：使用 Document Loader 將資料來源（例如 PDF、Markdown 同檔案）讀取成 `Document` 物件。  
  2. **切分（Split）**：以 Text Splitter 將大型文件切成可被模型處理的小段落，避免超過上下文視窗限制。  
  3. **存儲（Store）**：將切分後的段落利用 Embeddings 轉成向量，並儲存在 VectorStore（例如 Qdrant、Chroma、FAISS）中以便後續檢索。

![](https://python.langchain.com/v0.2/assets/images/rag_indexing-8160f90a90a33253d0154659cf7d453f.png)

- **檢索與生成（Retrieval & Generation）**  
  1. **檢索（Retrieve）**：用 Retriever 根據使用者提問搜尋最相關的向量段落。  
  2. **生成（Generate）**：將檢索到的段落與使用者問題一起送入 ChatModel（或 LLM），讓模型生成回答。

![](https://python.langchain.com/v0.2/assets/images/rag_retrieval_generation-1046a4668d6bb08786ef73c56d4f228a.png)

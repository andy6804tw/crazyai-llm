# GitHub Models 免費試玩 GPT、Llama、DeepSeek
> 帶你玩轉 Playground、API 串接，打造自己的 LLM 專案！

範例程式：[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/andy6804tw/crazyai-llm/blob/main/docs/3.免費LLM API串接資源/github-basic.ipynb)

## GitHub Models 介紹

[GitHub Models](https://github.com/marketplace?type=models) 是 GitHub 提供的一項免費服務，讓開發者能夠試用各種大型語言模型 (LLM)，例如 **GPT-4o、Llama 3.3、Phi-3.5** 等。這項服務特別適合個人開發者或小型專案，每日提供一定額度的免費 API 請求，讓使用者可以直接在 GitHub Playground 測試，或是透過 API 串接 GitHub Models 來開發自己的 AI 應用程式。



!!! note

      如果你正在尋找一個免費的 LLM 測試環境，GitHub Models 絕對值得一試！

## GitHub Models 的特點

✅ **免費額度**：每天最多可發送 50~150 次 API 請求（依模型而異）  
✅ **Playground**：無需寫程式即可在線上測試模型  
✅ **API 串接**：支援 OpenAI API 格式，與現有的 LLM 應用相容  
✅ **多種模型可選**：支援 GPT-4o、Llama、Phi 等多種 AI 模型  

---

## GitHub Models 支援的模型清單

GitHub Models 提供多種 **大型語言模型 (LLM)** 供開發者試用，涵蓋 **聊天模型、Embedding 模型**，適合不同的 AI 應用場景。

完整清單可在 [GitHub Models marketplace](https://github.com/marketplace?type=models) 查詢，以下是部分熱門模型：

### 📌 聊天模型
- DeepSeek-R1
- OpenAI GPT-4o
- OpenAI GPT-4o mini
- Llama-3.3–70B-Instruct
- Llama-3.2–90B-Vision-Instruct
- Phi-3.5-MoE instruct
- Phi-3.5-vision instruct
- Mistral Large
- Cohere Command R+
- AI21 Jamba 1.5
- JAIS 30b Chat
- ...

### 📌 Embedding 模型
- OpenAI Text Embedding 3
- Cohere Embed v3 Multilingual
- ...

---

## 免費與付費計畫

GitHub Models **免費用戶 (GitHub Copilot 免費版)** 可以使用部分模型，但如果想使用 **GPT-o1、GPT-o3-mini** 等最新模型，則需要升級到付費計畫 **[GitHub Copilot Pro](https://github.com/features/copilot/plans?cft=copilot_li.features_copilot)**。

> **💡 如果你是老師或學生**，可以透過 GitHub Education **[申請免費使用 GitHub Copilot Pro](https://medium.com/彼得潘的-swift-ios-app-開發問題解答集/用老師-學生身份免費使用-github-copilot-223236e0e0e8)**，享受更高級的模型與更多額度，對於學術研究與 AI 學習特別有幫助！

![GitHub Copilot 方案](https://miro.medium.com/v2/resize:fit:875/1*EQfN7QF8YWWPaent-bSxBw.png)

---

## GitHub Models 使用限制與限流說明

在開始使用 **GitHub Models** 之前，了解 **速率限制 (Rate Limits)** 非常重要。GitHub Models 依據不同的模型類型，將使用限制分為四個等級：

- **Low (低限制)**：適用於部分輕量模型，請求數量較少，適合一般測試用途。
- **High (高限制)**：適用於較大型的模型，例如 GPT-4o，速率限制較嚴格。
- **Embedding (嵌入式模型)**：適用於向量嵌入 (Embedding) 相關模型，主要用於語意搜尋與相似度計算。
- **Custom (自訂限制)**：適用於特殊模型，例如 Azure OpenAI o1-preview、o1/o3-mini，這些模型的使用限制會依據官方公告動態調整。

> **🔗 詳細請求限制資訊，請參考官方文件：**  
> [GitHub Models Rate Limits](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits)

---

## 🎮 在 Playground 測試 LLM 模型

GitHub Models 提供 **Playground**，讓開發者可以無需寫程式，直接測試 LLM 模型的能力。只需選擇一個模型，即可輸入 Prompt 進行互動。

![GitHub Models Playground 入口](https://miro.medium.com/v2/resize:fit:875/1*eKqTzeJjU_CIbPZ1BFHQ4g.png)

### 如何進入 Playground

1. **前往 GitHub Models**： [GitHub Models 入口](https://github.com/marketplace/models)
2. **選擇模型**：從下拉式選單中選擇一個模型
3. **開始聊天**：在輸入框輸入 Prompt，與 AI 進行對話

---

## 👨🏻‍💻 使用 API 測試 LLM 模型 (Colab 教學)

如果你希望將 GitHub Models **整合到自己的應用程式**，可以使用 **API 串接** 來發送請求。GitHub Models API **與 OpenAI API 格式相容**，讓開發者能夠無縫轉換至 GitHub 的 LLM 服務。

### API 申請步驟

1. **建立 GitHub Personal Access Token (PAT)**：
   - 前往 [GitHub Settings](https://github.com/settings/personal-access-tokens)
   - 進入 **Developer settings > Personal access tokens > Fine-grained tokens**
   - 生成 Token 並**妥善保存**
   
2. **在 Google Colab 執行 API 測試**
   - 在 Google Colab 左側選單點擊「🔑 Secrets」
   - 點擊「+ Add new secret」
   - **Name** 欄位輸入 `GITHUB_TOKEN`
   - **Value** 欄位貼上剛剛在 GitHub 生成的 Token
   - 點擊「access✓」按鈕允許 Colab 存取金鑰

> 📌 **開啟 [範例程式 (Google Colab)](https://colab.research.google.com/github/1010code/github-models-tutorial/blob/main/basic.ipynb)**

---

## 總結與下一步建議

透過這篇教學，我們學習了 **GitHub Models API** 的基本使用方式，包括 **Playground 測試及 API 串接**，並透過 **Google Colab** 示範如何讓 LLM 生成回應。

💡 **鼓勵你動手實作！**  
✅ **整合 RAG (Retrieval-Augmented Generation)**，結合外部知識庫提升 AI 回答準確性  
✅ **使用 Streamlit 或 Gradio** 封裝成 **聊天應用**，打造一個互動式 AI Chatbot  

透過這樣的練習，不僅能深化對 LLM 模型的理解，也能為你添加個人作品！現在就開始你的 **GitHub Models AI 專案** 吧！🚀🎯

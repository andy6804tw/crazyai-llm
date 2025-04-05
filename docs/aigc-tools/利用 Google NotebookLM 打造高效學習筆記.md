---
author: Tsai Yi Lin
date: 2025-03-09
tags:
  - AI寫作生成
  - 生產力工具
---

# 如何利用 Google NotebookLM 打造高效學習筆記？
> 學生自學/閱讀論文的最佳拍檔

## 什麼是 NotebookLM？

[NotebookLM](https://notebooklm.google/) 是由 Google 推出的一款個人化 AI 協作工具，主要是協助使用者更有效地創作和思考。透過上傳個人文件，NotebookLM 能夠立即理解這些來源的內容，並與使用者互動。你可以在平台上閱讀文件、撰寫記事，並與 NotebookLM 協作，整理想法並將其付諸實行。這項工具結合了大型語言模型的強大功能和你的個人資料，為你的工作和學習帶來前所未有的便利。

!!! note

    簡單來說 Google NotebookLM 是一個免費的 AI 虛擬助教。

<iframe width="560" height="315" src="https://www.youtube.com/embed/S9CdTp6xrTM?si=X5fsHr6RQWA3qcIx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
NotebookLM 背後的技術核心是基於 Google 自家的 **Gemini 多模態大型語言模型**（Large Multimodal Language Model, LLM）。這款模型結合了強大的自然語言處理能力，能夠理解和處理文本內容，同時支援多模態資料的分析，如文本、圖像等。藉由這樣的技術，NotebookLM 可以快速分析、總結使用者上傳的資料，並根據其內容進行互動。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*3JL0eKwxyiao8q35Rh-ebA.png)

!!! note

        - 學術論文參考：[Gemini LLM 論文](https://arxiv.org/pdf/2312.11805)

---

## 如何使用 NotebookLM？

首先，只要有 **Google 帳號** 就能免費使用 [NotebookLM](https://notebooklm.google/) 服務。為了充分利用這個平台的強大功能，必須先上傳你的第一個資料來源。由於 NotebookLM 僅針對使用者上傳的文件進行筆記彙整，這有效避免了現今大型語言模型常見的幻覺問題（例如答非所問或偏離主題）。透過上傳你的資料來源，AI 能夠根據這些內容提供精準且相關的協助，提升你的工作和學習效率。上傳過程簡單直觀，讓你可以迅速開始與 NotebookLM 進行互動，整理思緒並將想法付諸實行。

### **支援的文件格式**
- **Google 文件或 Google 簡報**：直接從 Google 雲端硬碟上傳。
- **PDF 或 TXT 檔案**：支援常見的文件格式，方便上傳各種資料。
- **純文字內容**：可直接貼上文字內容，建立新的來源。

### **操作步驟**
1. **選取筆記本**：選擇現有筆記本，或點選「新增筆記本」並輸入自訂名稱。
2. **新增資料來源**：在畫面左側的來源檢視器中，按一下「加號」圖示新增來源。
3. **選取文件**：選擇要上傳的文件，例如 PDF 或 Google Docs。
4. **確認上傳**：點擊「插入」按鈕，NotebookLM 會開始解析內容。

---

## 上傳文件來源

NotebookLM 還支援一次上傳 **多個文件**，無論是會議記錄、研究報告，還是多篇文章，系統都能同時處理並彙整這些資料。以下為一個機器學習的教學 PDF 文件範例：

📄 **下載示範文件**：[全民瘋 AI 系列_經典機器學習 v2.1.pdf](https://github.com/andy6804tw/crazyai-ml/releases/download/v2.0/crazyai-ml_v2.1.pdf)

![NotebookLM 功能指引](https://miro.medium.com/v2/resize:fit:700/1*2xnu-n9uexpCjpLhLlQ3CA.png)


!!! info

    ⚠️ 注意：每個來源最多只能包含 50 萬字！

---

## **建立新記事**

NotebookLM 提供 **「產生記事」** 功能，能夠快速生成特定格式的筆記，例如：

- **常見問題（FAQ）**
- **學習指南**
- **目錄**
- **時間軸**
- **簡介文件**

這些功能能幫助使用者 **有條理地整理資訊，並節省大量時間**，讓你專注於思考和創作，而非繁瑣的資料整理。

![NotebookLM 提供的記事功能](https://miro.medium.com/v2/resize:fit:700/1*UFgFBuHMFw4EakQRP45gQQ.png)

當你點選 NotebookLM 的 學習指南 生成功能後，系統會自動生成如下圖所示的內容，為你提供一個結構化的小測驗或問題集，幫助你檢驗是否掌握了相關知識。這些問題通常會涵蓋關鍵概念與技術細節，透過回顧與回答這些問題，你可以清楚了解自己是否有吸收課程內容，並加強對重要概念的理解。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*WyuxbUXRhRaI_eOK)

在 NotebookLM 中，平台透過 AI 技術分析你上傳的文件，並自動為你生成幾個使用者可能會提出的 Prompt。Prompt 的概念其實就是我們在 ChatGPT 這類對話式機器人服務中常見的互動方式，指的是使用者向 AI 提出問題，然後 AI 根據資料回應。只要你輸入一個問題或指示，AI 就會根據文件內容生成相對應的資訊。

NotebookLM 幫助我們產生一些可能的 Prompt，這些提示通常根據文件的關鍵內容，方便使用者快速發問而不需要自己編寫問題。例如，當你上傳了一份機器學習課程的資料，平台可能會提供以下 Prompt：

- 「書中介紹了哪些機器學習演算法，以及如何使用這些演算法解決實際問題？」
- 「這本書主要介紹哪些 AI 相關概念與應用？」

NotebookLM 的 **提問功能** 是與使用者上傳的資料進行互動的關鍵功能之一。如果你想從上傳的文件中獲得特定資訊，只需要在右下方的對話方塊輸入問題或指示，然後按下箭頭或按 Enter 鍵來發送問題。NotebookLM 會根據資料來源進行分析，提供與問題相關的回覆。

這項功能不僅僅是給出回答，NotebookLM 還會附上具體的引用內容，這些引用來自你上傳的文件。點選引文後，系統會直接跳轉到文件中的相關段落，這樣你可以輕鬆確認 AI 回覆的依據，並深入瞭解更多細節。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*hVJI6I79AMbuE9tkny0wSw.png)

例如，當你提問「此書中介紹了哪些機器學習演算法？」時，NotebookLM 不僅會列出主要的演算法，還會在回答中標明這些內容的來源頁面，讓你能夠追溯到原始文件的具體段落。這樣的引用功能確保了回覆的準確性與可追溯性，讓使用者在學習或工作中更具信心。

NotebookLM 的提問功能應用範圍非常廣泛，不僅限於學術研究或文檔分析，還能幫助你在工作、學習、創作等各種場景中大幅提升效率。例如可以拿來做以下事情：

- **會議記錄摘要**：你可以上傳會議記錄，然後讓 NotebookLM 協助你快速提取重要資訊。例如，可以要求「**製作 2024 年行銷預算討論的摘要**」，NotebookLM 會根據記錄的內容生成一個重點總結，幫助你節省時間並清晰掌握核心討論點。

- **專業科學文章的關鍵詞提取**：對於需要快速了解一篇專業文章的重點時，你可以上傳科學或技術類文件，並請求 NotebookLM 建立關鍵詞表。例如，上傳一篇有關神經科學的文章，你可以詢問「**建立與多巴胺相關的重要詞彙表**」，NotebookLM 會根據文中內容提取多巴胺的主要概念或術語，幫助你快速抓住要點。

- **歷史研究**：NotebookLM 也能應用於歷史或人物研究中。上傳與某位歷史人物相關的筆記，然後提出問題，例如「**Hopper 對電腦科學有哪些貢獻？**」NotebookLM 會自動從資料中提取出與該人物相關的重要貢獻或事蹟，為你的研究提供幫助。

NotebookLM 不僅可以查詢來源中的資訊，還能激發創作靈感。舉例來說：

- **上傳短篇故事的草稿**，並請求 NotebookLM「_建議可以加入這篇故事的新角色_」。
- **上傳業務計畫**，並讓 NotebookLM「**為這項產品提供三項新功能的建議**」。
- **上傳網誌文章的草稿**，並詢問 NotebookLM「**提供三組適合這篇文章的標題或副標題**」。


---

## **NotebookLM 新功能：語音生成功能（生成 Podcast 音檔）**

NotebookLM 的 **Audio Overview（音訊概述）** 是 Google 於 **2024 年 9 月 11 日** 推出的新功能。使用者可以將筆記或研究內容快速轉換為 **音訊 Podcast**，方便隨時隨地收聽或分享。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*mzcp5rF0hkvpSrV6k5hVOA.png)

🎙️ **應用場景**：

- **生成 Podcast 音檔**：將筆記、學習指南或報告內容轉換為 Podcast 形式，適合音頻學習。
- **學習輔助工具**：可將長篇文檔轉換為音訊，方便在通勤、運動時複習學習內容。

🎧 **功能特色**：

- **文字轉語音技術**：AI 自動將筆記或文章內容轉換為自然流暢的語音。
- **輕鬆分享**：生成的 Podcast 或音訊檔案可輕鬆與他人分享或作為教學資源。

這項功能的推出，使 NotebookLM 從文本處理擴展至音頻領域，為使用者提供了更多元的內容呈現方式，無論是製作 Podcast 還是進行學習，都變得更加方便。以下音檔是 **全民瘋AI系列 [經典機器學習]** Podcast 的介紹。

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/episode/4Bv2crsefXvQX5YAZrviYw?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

接下來，我會將陸續推出三十天的內容，每一集都會轉換成音檔，並且附上完整的字幕與翻譯，讓大家無論是在學習 AI 技術還是提升英文能力，都能輕鬆跟上。如果你對 AI 和機器學習感興趣，或是想要一邊聽 Podcast 一邊練習英文，誠摯邀請你來收聽，讓我們一起展開這段充滿知識的學習之旅！

### 2024/9/15更新：繼 NotebookLM 後 Google 再推出 Illuminate
繼 NotebookLM 之後，Google 於 2024 年 9 月推出了 Illuminate，這是一款全新的 AI 驅動工具，專為將長篇文章、書籍或學術論文轉換為對話式 Podcast 而設計。Illuminate 結合了 AI 語音技術和自然語言處理技術，能自動生成以兩人對話形式呈現的音檔，模擬真人討論的方式，讓用戶更輕鬆地透過聽覺來理解和吸收複雜資訊。這種創新的音訊呈現方式大大提升了學習與資訊傳遞的便利性。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*R2_CxX6Qs_Hcljb840b5nw.png)

### 2024/9/27更新：匯入Youtube 連結功能
NotebookLM 新增了匯入 YouTube 連結的功能，使用者現在可以將 YouTube 影片直接匯入到 NotebookLM 進行分析。這項功能特別適合希望從視聽資料中提取重要資訊的使用者，如學術研究或內容創作者。

**目前的功能限制：**

- NotebookLM 只能處理已經提供字幕的影片。如果影片本身沒有字幕，NotebookLM 將無法直接讀取影片中的內容。

**解決方案：**

- 對於沒有字幕的影片，使用者可以選擇其他語音轉文字工具，例如 Memo.AI 或 Whisper，將影片內容轉錄為文字檔後，再匯入 NotebookLM 進行進一步的整理與分析。

這項功能的推出，使得 NotebookLM 的應用範圍更加廣泛，特別是在多媒體內容的學習和分析上，未來也可能會支援自動生成字幕的功能，提升無字幕影片的可讀性與使用體驗。

## **結語**

Google NotebookLM 透過 AI **提升筆記整理與知識管理的效率**，提供強大的摘要、生成功能，甚至能夠 **轉換為音訊 Podcast**，使得學習更加直覺化與高效。如果你正在尋找一款能夠幫助你整理筆記、加速學習的工具，那麼 NotebookLM 是一個值得一試的選擇！



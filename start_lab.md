# 實驗室 Alpha：基礎環境與 API 測試計畫

## 1. 基礎建設 (Infra)
- 檢查是否安裝 `uv`，若無請安裝它。
- 使用 `uv` 初始化 Python 環境。
- 安裝套件：`yfinance`, `pandas`。

## 2. 程式開發 (Dev)
- 建立 `hello_api.py`。
- 邏輯：
    1. 抓取台積電 `2330.TW` 今天的即時價格。
    2. 印出：「實驗室 Alpha 啟動成功！台積電當前價格：[價格]」。
    3. 將結果存入 `result.txt`。

## 3. Git 自動化 (Ops)
- 建立 `.gitignore` 排除 .venv。
- 執行 `git add .` 與 `git commit -m "feat: first automated lab task"`。
import yfinance as yf


def get_tsmc_price() -> float | None:
    """
    尋找 2317.TW 的最新價格。
    盡量用 fast_info，失敗再 fallback 到 info。
    """
    ticker = yf.Ticker("2317.TW")

    # fast_info 通常更快
    try:
        last_price = ticker.fast_info.get("last_price")
        if last_price is not None:
            return float(last_price)
    except Exception:
        pass

    # fallback：info 欄位可能不同（不同 API 版本）
    try:
        info = ticker.info
        for key in ("currentPrice", "lastPrice", "regularMarketPrice"):
            val = info.get(key)
            if val is not None:
                return float(val)
    except Exception:
        pass

    return None


def main() -> None:
    price = get_tsmc_price()
    if price is None:
        msg = "實驗室 Alpha 啟動成功！鴻海當前價格：[N/A]"
    else:
        msg = f"實驗室 Alpha 啟動成功！鴻海當前價格：{price}"

    print(msg)
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(msg)


if __name__ == "__main__":
    main()


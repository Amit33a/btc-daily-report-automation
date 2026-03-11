from decimal import Decimal
from typing import List, Dict, Any


def _to_float(x):
    if isinstance(x, Decimal):
        return float(x)
    return float(x)


def build_report(last_rows: List[Dict[str, Any]]) -> str:
    if not last_rows:
        return "BTC Daily Report\n\nNo data found in the last 7 records."

    prices = [_to_float(r["price_usd"]) for r in last_rows]

    latest = prices[0]
    oldest = prices[-1]

    avg_price = sum(prices) / len(prices)
    high_price = max(prices)
    low_price = min(prices)

    change = latest - oldest
    pct_change = (change / oldest) * 100 if oldest != 0 else 0.0

    lines = []
    lines.append("BTC Daily Report (Last 7 Records)")
    lines.append("")
    lines.append(f"Records: {len(prices)}")
    lines.append(f"Latest price: ${latest:,.2f}")
    lines.append(f"7-record average: ${avg_price:,.2f}")
    lines.append(f"7-record high: ${high_price:,.2f}")
    lines.append(f"7-record low: ${low_price:,.2f}")
    lines.append(f"Change (latest - oldest): ${change:,.2f}")
    lines.append(f"% Change: {pct_change:.2f}%")
    lines.append("")
    lines.append("Recent prices (newest -> oldest):")

    for i, p in enumerate(prices, start=1):
        lines.append(f"{i}. ${p:,.2f}")

    return "\n".join(lines)
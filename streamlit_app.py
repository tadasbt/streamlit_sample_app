import requests
from bs4 import BeautifulSoup
import re

BASE_URL = "https://s.minkabu.jp/stock/{code}/dividend"
HEADERS = {
  "User-Agent":"Mozilla/5.0"
}

def get_minkabu_dividend_month(code:str) -> list[str] | None:
  """
  例： code='7272' -> ['6月','12月'] を返す想定。
  取得できなければ None。
  """
  url = BASE_URL.format(code=code)
  resp = requests.get(url, headers=HEADERS, timeout=10)

  soup = BeautifulSoup(resp.text, "html.parser")

  # 「権利月」という文字列を含む要素を探す
  candidates = soup.find_all(string=re.compile("権利月"))
  if not candidates:
    return None

  for s in candidates:
    text = s.parent.get_text(strip=True)
    # 例："権利月6月，12月" or "権利月　6月，12月"
    m = re.search(r"権利月s*[:：]?s*(.+)", text)
    if not m:
      continue
    months_part = m.group(1)
    # 「6月，，12月」→ 「"6月","12月"」
    months = [x.strip() for x in re.split(r"[,s]+", months_part) if x.strip()]
    return months
  return None

x=10
'x: ', x
'import requests'
dividend_month=get_minkabu_dividend_month("7987")
'dividend_month: ', dividend_month

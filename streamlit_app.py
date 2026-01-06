import requests
from bs4 import BeautifulSoup
import re

BASE_URL = "https://s.minkabu.jp/stock/
{code}/dividend"
HEADERS = {
  "User-Agent":"Mozilla/5.0"
}

def get_minkabu_dividend_month(code:str) -> list[str] | None:
  """
  例： code='7272' -> ['6月','12月'] を返す想定。
  取得できなければ None。
  """
  url = BASE_URL.format(code=code)
x=10
'x: ', x
'import requests'

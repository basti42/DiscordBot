import requests
from lxml import html

class CoinbaseGetter:

    def __init__(self):
        self.baseurl = "https://www.coinbase.com/price/"
        self.divcontainer = "ChartPriceHeader__BigAmount-sc-9ry7zl-4 dKeshi"

    def getPriceFor(self, s: str) -> str:
        """
        parses the current price of the requested
        crypto currency from coinbase
        returns a dict
        """
        try:
            page = html.fromstring(requests.get(self.baseurl+s).content)
            div = page.xpath(".//div[@class='"+self.divcontainer+"']")[0]
            content = div.getchildren()[0].text
            return content
        except BaseException as bex:
            print(f"unable to get price for {s}")
            print(bex)
            return None

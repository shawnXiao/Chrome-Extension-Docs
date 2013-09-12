import mechanize
import json
import re
from bs4 import BeautifulSoup

class extensionDoc(object):
    def __init__(self):
        self.parser = "html.parser"
        self.base_url = "http://developer.chrome.com/extensions/api_index.html#supported"
        self.url_prefex = "http://developer.chrome.com/extensions/"
        br = mechanize.Browser()
        self.browser = br

    def downLoadDoc(self):
        contentPage = self.browser.open(self.base_url, timeout = 50.0)
        soup = BeautifulSoup(contentPage, self.parser)
        anchor_list = soup.select('#gc-pagecontent li > a[href$="html"]')
        api_list = {}
        for anchor in anchor_list:
            api_name = anchor.get_text()
            api_list[api_name] = {}
            api_url = self.url_prefex + anchor.get("href")
            api_list[api_name]["api_url"] = api_url
            api_Detail_page = self.browser.open(api_url, timeout = 50.0)
            api_Detail_soup = BeautifulSoup(api_Detail_page, self.parser)
            api_intro_tr_list = api_Detail_soup.select(".intro tr ")
            for api_intro_tr in api_intro_tr_list:
                api_intro_title_str = api_intro_tr.select(".title")[0].get_text()
                m = re.split(':', api_intro_title_str)
                api_intro_title = m[0]
                api_intro_content = api_intro_tr.select("td:nth-of-type(2)")[0].get_text().strip()
                api_list[api_name][api_intro_title] = api_intro_content
        return json.dumps(api_list)
def main():
    doc = extensionDoc()
    doc.downLoadDoc()
if __name__ == "__main__":
    main()

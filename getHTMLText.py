import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        return "产生异常"


if __name__ == "__main__":
    url = "https://item.jd.com/100006607543.html"
    print(getHTMLText(url))

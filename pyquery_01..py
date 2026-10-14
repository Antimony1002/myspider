import requests
from pyquery import PyQuery as pq

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

def get_html(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    return pq(resp.text)

def parse_html(doc):
    data = []
    pages = doc(".review-item").items()
    for page in pages:
        movie = page.find("img[title]").attr("title")
        short_review = page.find(".main-bd h2 a").text()
        long_review = page.find(".short-content").text()
        if movie:
            data.append({
                "movie": movie,
                "short_review": short_review,
                "long_review": long_review
            })
    return data

def main():
    url = "https://movie.douban.com/review/best/?app_name=movie"
    doc = get_html(url)
    data = parse_html(doc)
    for item in data:
        print(item)

if __name__ == "__main__":    main()

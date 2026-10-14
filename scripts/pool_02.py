import requests
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

def single(page):
    url = f"https://www.qimao.com/qimaoapi/api/classify/book-list?channel=a&category1=203&category2=219&words=a&update_time=a&is_vip=a&is_over=a&order=click&page={page}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "Referer": "https://www.qimao.com/shuku/a-203-219-a-a-a-a-click-1/"
    }

    resp = requests.get(url,headers=headers)
    dic = resp.json()
    book = dic['data']['book_list']
    return book

def extract_book_info(book):
    return {
        'title': book['title'],
        'author': book['author'],
        'words': book['words_num'],
        'status': book['is_over_txt'],
        'update': book['update_time'],
    }

if __name__ == '__main__':
    all_books = []
    pages = range(1, 48)  # 要抓取的页码
    
    # 创建线程池，最多同时运行4个线程
    with ThreadPoolExecutor(max_workers=2) as executor:
        # 提交所有任务，返回future对象字典
        future_to_page = {executor.submit(single, page): page for page in pages}
        
        # 收集完成的任务
        for future in as_completed(future_to_page):
            page = future_to_page[future]
            try:
                books = future.result()  # 获取任务返回值
                all_books.extend(books)
                print(f"第{page}页完成，获取到{len(books)}本书")
            except Exception as e:
                print(f"第{page}页失败：{e}")
    
    # 写入文件（这部分不需要多线程，因为文件写入是顺序操作）
    if all_books:
        with open('novel.csv', 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=['title', 'author', 'words', 'status', 'update', 'intro'])
            w.writeheader()
            w.writerows([extract_book_info(b) for b in all_books])
        print(f"完成！共写入{len(all_books)}本书")

import requests, os, time

genres = {
    "mystery": "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "poetry": "http://books.toscrape.com/catalogue/category/books/poetry_23/index.html",
    "science": "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
}

os.makedirs("data/raw", exist_ok=True)

for label, url in genres.items():
    filename = f"data/raw/{label}-{time.strftime('%Y%m%d-%H%M%S')}.html"
    resp = requests.get(url)
    with open(filename, "wb") as f:
        f.write(resp.content)
    print(f"Saved {label} HTML to {filename}")


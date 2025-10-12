from bs4 import BeautifulSoup
import pandas as pd, glob, os

all_books = []

for filepath in glob.glob("data/raw/*.html"):
    label = os.path.basename(filepath).split("-")[0]  # genre uit bestandsnaam
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    titles = [a["title"] for a in soup.find_all("a") if a.get("title")]
    for t in titles:
        all_books.append({"title": t, "label": label})
os.makedirs("data/processed", exist_ok=True)
df = pd.DataFrame(all_books)
df.to_csv("data/processed/books.csv", index=False)

print(f"Saved {len(df)} books to data/processed/books.csv")

import pandas as pd, sqlite3, os
df = pd.read_csv("data/processed/books.csv")
df["title"] = df["title"].str.lower().str.strip()
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/books_clean.csv", index=False)
conn = sqlite3.connect("data/books.db")
df.to_sql("books", conn, if_exists="replace", index=False)
conn.close()
print("Saved cleaned CSV and SQLite database")

# 📅 Week 5: [Data Ingestion, Web Scraping and Machine Learning Classification]

## 🛠️ 1. What I Built
- **Summary**:
 📅 Week 5 : Data Ingestion, Web Scraping and Machine Learning Classification
 During Week 5, I developed a complete data pipeline that covers the full process from collecting raw data to training a machine learning model for text classification. The project involved downloading book data from different genre pages, extracting and cleaning the text, storing it in structured formats, and applying a classification algorithm to predict book genres based on titles.

The work was divided into four main scripts:

fetch_data.py : downloads raw HTML pages containing book information.
scrape_books.py : parses the HTML and extracts relevant book titles.
clean_books.py : cleans and standardises the dataset for further processing.
classify.py : trains and evaluates a machine learning model using TF-IDF and Logistic Regression.

All parts of the pipeline are fully automated and reproducible. Data is organised into dedicated folders (data/, logs/, src/), and the process can be run entirely using a Makefile.

- **Key Tools Used**  
  - Python (requests, BeautifulSoup, pandas, scikit-learn, sqlite3)
  - SQLite for local data storage
  - Bash and Makefile for automation
  - Git and GitHub for version control
  - Virtual environment (.venv) for dependency management


- **Artifact Location**  
  - `Scripts → /week5/src/
  - Processed datasets → /week5/data/processed/
  - SQLite database → /week5/data/books.db
  - Logs (metrics) → /week5/logs/metrics.csv
  - Repository → MLOps-Practical-1/week5

- **How to Run**  

# 1. Activate the environment
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the complete pipeline
make all


---

## 🔍 2. My Exploration
- **What I Investigated Further**  
Throughout this week, I focused on understanding how each stage of a data workflow connects to the next. I learned how raw HTML can be transformed into structured information, and how this cleaned data can then be used to train and evaluate a model. Working with BeautifulSoup was particularly interesting because it demonstrated how data can be extracted from unstructured web pages. I also explored the impact of text cleaning converting titles to lowercase, removing punctuation, and trimming spaces on the model’s accuracy. The dataset contained 53 book titles spread across three genres. Using TF-IDF vectorisation and Logistic Regression, the model achieved an accuracy of about 0.55. This result showed the importance of data quality and quantity in training reliable models.Additionally, I experimented with storing data in SQLite. This made the process more reproducible, as all stages of the pipeline could access a consistent and queryable data source without external dependencies.

Challenges
- Managing file paths that contained spaces, especially on macOS.
- Resolving a small coding error (os.makedirs instead of s.makedirs).
- Structuring output folders and logs clearly for easy tracking.

Results
- Dataset: 53 books across three genres.
- Model: Logistic Regression with TF-IDF vectorisation.
- Accuracy: approximately 0.55.
- Outputs: books_clean.csv, books.db, and metrics.csv.



- **Link to Evidence**  
  I have a folder of Evidence where you can see the results of the terminal

---

## 🤖 3. Use of Genai
I briefly used an AI tool to help identify the cause of a small coding error that was preventing one of my scripts from running. The error turned out to be a simple typo where I had written s.makedirs instead of os.makedirs. After discovering this, I corrected the code myself and verified that the pipeline ran successfully. This short moment of assistance helped me understand the error message more clearly and reinforced my ability to debug similar issues independently in the future.

## 💬 4. Reflection
- **How did this week’s work support reproducibility or deployment?**  
 This week reinforced the importance of reproducible workflows. By saving both raw and processed data and automating the entire process with a Makefile, I created a consistent and transparent workflow. The use of SQLite ensured that the data could be accessed and verified at any stage of the process, while the virtual environment guaranteed consistent dependencies

- **What was most confusing or interesting?**  
The most interesting part was seeing how all components, from web scraping to machine learning, fit together into one logical pipeline. was rewarding to build something that performs every step automatically. The most challenging aspect was maintaining a clean folder structure and managing file paths correctly across operating systems.

- **If someone else looked at your repo, what would help them use this part of the project?**  
A detailed README explaining how to activate the environment, install dependencies, and run make all would make it easy for anyone to reproduce the results. Including example outputs, such as the metrics file or screenshots of the pipeline running, would also help new users quickly understand the workflow.

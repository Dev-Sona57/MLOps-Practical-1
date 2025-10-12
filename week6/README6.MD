# 📅 WWeek 6: [Model Deployment and API Integration with FastAPI]

## 🛠️ 1. What I Built
- **Summary**:
 📅 During Week 6, I extended the machine-learning pipeline from Week 5 into a deployable application. The main goal was to make the trained book-genre classifier accessible through an API interface. This required integrating the model with FastAPI, serialising the model artefacts, and ensuring the overall workflow remained reproducible and maintainable.

The work was divided into two primary scripts:

classify.py: trains the model, evaluates it, and saves both the trained classifier and the TF-IDF vectoriser.
app.py: creates a FastAPI web application that loads the saved artefacts and exposes endpoints for real-time predictions.

Projet Structure
week6/
│
├── src/
│   ├── classify.py
│   └── app.py
│
├── data/
│   └── processed/books_clean.csv
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── logs/
│   └── metrics.csv
│
├── evidence/
│   ├── terminal_output.png
│   ├── swagger_ui.png
│   └── prediction_test.png
│
└── venv/

My pipeline overview:
Load the cleaned dataset (books_clean.csv) created in Week 5.
Train a Logistic Regression model using TF-IDF vectorisation.
Evaluate model performance and export metrics to logs/metrics.csv.
Save the trained model and vectoriser to the models
Deploy a REST API using FastAPI and test it through the built-in Swagger UI

- **Key Tools Used**  
  - Python (pandas, scikit-learn, joblib, FastAPI, Uvicorn)
  - Virtual environment for dependency isolation
  - RESTful API development using FastAPI
  - Git and GitHub for version control


- **Artifact Location**  
  - Model and vectoriser → /week6/models/
  - Processed data → /week6/data/processed/
  - API source code → /week6/src/
  - Logs (metrics) → /week6/logs/metrics.csv
  - Evidence screenshots → /week6/evidence/
  - Repository → MLOps-Practical-1/week6

- **How to Run**  
# 1. Activate environment
source venv/bin/activate

# 2. Run training
python src/classify.py

# 3. Start API
uvicorn src.app:app --reload

# 4. Test in browser
http://127.0.0.1:8000/docs



## 🔍 2. My Exploration
- **What I Investigated Further**  
What I Investigated Further
This week focused on bridging the gap between model training and deployment. I learned how to store and reload model artefacts reliably using joblib, and how to integrate them into an API that can accept user input and return predictions dynamically. Testing the API endpoints through FastAPI’s interactive Swagger UI was particularly insightful. It allowed me to verify how requests and responses are structured in JSON format and to observe how the model behaves when provided with unseen titles.

Challenges
Handling missing file paths during setup (ensuring data/processed/ and models/ existed before saving artefacts).
Debugging syntax and import errors after renaming files.
Managing the active virtual environment and keeping the Uvicorn server stable while running.

Results:
- Dataset → 53 books across three genres.
- Model → Logistic Regression with TF-IDF vectorisation.
- Accuracy → ~ 0.55 on the validation set.
- Model and vectoriser successfully saved to /models/.
FastAPI app served locally at http://127.0.0.1:8000 with a working /predict/ endpoin

Example API response: {
  "title": "The Science of the Universe",
  "predicted_label": "science"
}

- **Link to Evidence**  
 document and verify my progress, I created a dedicated folder named /week6/evidence/ containing screenshots that demonstrate the functionality of my project:

- terminal_output.png → shows the server startup and model-training logs.
- swagger_ui.png → displays the interactive FastAPI documentation interface.
- prediction_test.png → captures a successful prediction request sent via /predict/.

These screenshots provide concrete evidence of the API running locally and the model making predictions in real time.
---

## 🤖 3. Use of Genai
At one point, I encountered persistent path and syntax errors while integrating the saving mechanism for the trained model. I briefly consulted an AI assistant to clarify how to correctly use joblib.dump() and to confirm the proper structure of a FastAPI endpoint. After that, I independently applied and tested the solution, verifying that the API and model operated as expected. The AI served as a great debugging aid.

## 💬 4. Reflection
- **How did this week’s work support reproducibility or deployment?**  
 This week marked the transition from a local machine-learning experiment to a deployable, service-oriented architecture. By exporting the model and vectoriser as artefacts and wrapping them in a FastAPI endpoint, I achieved a reproducible deployment process. Consistent folder structures and environment management ensured that the workflow can be replicated easily.

- **What was most confusing or interesting?**  
The most interesting aspect was seeing my trained model come to life through a real API interface, transforming a static script into an interactive web service. The most challenging parts were maintaining clean file paths and keeping the server process stable. Once those issues were solved, seeing real-time predictions in the Swagger UI was extremely rewarding.

- **If someone else looked at your repo, what would help them use this part of the project?**  
AA detailed README with environment activation, training, and deployment instructions would make it straightforward for others to reproduce my results. Including the screenshots in the evidence folder and references to the working endpoints ensures transparency and clarity for new users.
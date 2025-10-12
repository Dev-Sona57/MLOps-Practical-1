# 📅 Week 4: [Environments & Docker]

## 🛠️ 1. What I Built
- **Summary**:
 📅 Week 4: Environments & Docker
This week, I set up three isolated Python environments to keep project dependencies separate and ensure reproducible results. This included two Conda environments (`envA` and `envB`) with different versions of `numpy` and one Python `venv` (`.sandboxA`) with `numpy` and `pandas`. Additionally, I created a test file (`test_results.txt`) to record the installation and output of the packages.

- **Key Tools Used**  
  - Conda  
  - Python venv  
  - pip / requirements.txt  
  - Terminal / Bash commands  
  - GitHub (repository management)

- **Artifact Location**  
  - `environment.yml`, `environmentB.yml`, `requirements.txt` → `/week4`  
  - `test_results.txt` → `/`  
  - GitHub repo: [link to your Week4 folder]

- **How to Run**  
  - Conda envA:  
    ```bash
    conda activate /Users/sonacecherif/MLOps-Practical-1/envA
    python -c "import numpy; print(numpy.__version__)"
    ```
    Expected output: `1.24.0`  

  - Conda envB:  
    ```bash
    conda activate /Users/sonacecherif/MLOps-Practical-1/envB
    python -c "import numpy; print(numpy.__version__)"
    ```
    Expected output: `1.26.0`  

  - venv `.sandboxA`:  
    ```bash
    source .sandboxA/bin/activate
    pip install -r /Users/sonacecherif/MLOps-Practical-1/week4/requirements.txt
    python -c "import numpy, pandas; print(numpy.__version__, pandas.__version__)"
    ```
    Expected output: `1.24.0 2.3.2`

---

## 🔍 2. My Exploration
- **What I Investigated Further**  
  - The difference between Conda and venv in isolating dependencies and Python versions.  
  - Correctly capturing dependencies with `requirements.txt` and `environment.yml` for reproducible environments.  
  - Automating test outputs to `test_results.txt` using Bash scripts.

  During this week, I investigated the differences between Conda and venv environments, focusing on their scope and capabilities. Conda can manage both Python and non-Python dependencies, while venv is limited to Python packages. I explored the purpose of creating multiple isolated environments, which include: avoiding dependency conflicts, testing code with different package versions, and ensuring reproducibility of results. I also experimented with capturing environments using requirements.txt and environment.yml files, and verified that re-creating environments produced the same package versions. Finally, I explored the benefits of Docker for packaging an entire project with its dependencies in a consistent environment.

- **Link to Evidence**  
  - `test_results.txt` in repository  
  - Bash script `run_tests.sh` for automated tests

---

## 🤖 3. Use of Genai
I used ChatGPT and online guidance to help me understand Conda activation errors, how to properly set up venv environments. From this guidance, I learned why Conda activation sometimes fails and how to resolve it. I understood the differences between Conda and venv environments and the purpose of creating multiple isolated environments: to avoid dependency conflicts, test code with different package versions, and ensure reproducibility.There were some issues to be aware of. For example, ChatGPT occasionally suggested defaults, such as using a pre-filled Docker Hub username, which I had to adjust. I also needed to be careful when switching between different shells, such as Mac terminal and Git Bash, to avoid path issues.Overall, this process helped me understand the importance of isolated environments, the practical value of Docker for reproducibility, and how to clearly document and communicate my work.

## 💬 4. Reflection
- **How did this week’s work support reproducibility or deployment?**  
 This week’s work reinforced the importance of reproducibility and dependency isolation in Python projects. By setting up multiple environments, I confirmed that package versions can be managed independently, avoiding conflicts and ensuring that code behaves consistently. Using Docker further strengthened my understanding of environment reproducibility by packaging the entire project in a container.

- **What was most confusing or interesting?**  
  The most interesting part was seeing how different environments can coexist peacefully while running different package versions, which clarified the practical value of virtual environments and Docker in research and deployment scenarios.

- **If someone else looked at your repo, what would help them use this part of the project?**  
For someone else looking at this repository, clear instructions for activating environments, installing dependencies, and running the Python scripts would make it straightforward to reproduce the results. The included requirements.txt, environment.yml, and Dockerfile provide all necessary information to set up and test the environments.
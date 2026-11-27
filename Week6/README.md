Week 6 – LLM Evaluation and Baseline Testing

In Week 6, I developed an LLM evaluation system using the Llama 3.2 model through Ollama. The program uses a golden question set to evaluate model responses, calculates keyword-based scores, and generates a baseline evaluation report (Release v0.1).

Steps I followed:
1. Created a Week6 project in VS Code with main.py, golden_set.json and requirements.txt.
2. Checked the Ollama version and downloaded the Llama 3.2 model.
3. Created a golden dataset containing 30 questions, expected answers, keywords and source links.
4. Installed the required requests library.
5. Connected Python to the Ollama API to generate answers.
6. Implemented keyword matching to calculate evaluation scores.
7. Generated PASS, REVIEW and ERROR statuses based on the results.
8. Saved the evaluation results in baseline_results.csv and generated a summary report.

Commands used:
ollama --version

ollama pull llama3.2

pip install -r requirements.txt

python main.py

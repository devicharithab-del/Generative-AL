## Week 6 – LLM Evaluation

In Week 6, I developed an LLM evaluation system using the Llama 3.2 model through Ollama. The program uses a golden question set to evaluate model responses, calculates keyword-based scores and generates a baseline evaluation report (Release v0.1).

### Steps I followed:

1. Created a Week6 project in VS Code with `main.py`, `golden_set.json` and `requirements.txt`.
2. Checked Ollama and downloaded the Llama 3.2 model.
3. Created a golden dataset containing 30 questions, expected answers, keywords and sources.
4. Installed the required `requests` library.
5. Connected Python to the Ollama API to generate answers.
6. Implemented keyword matching to calculate evaluation scores.
7. Generated PASS, REVIEW and ERROR statuses.
8. Saved the results in `baseline_results.csv` and generated an evaluation summary.

### Commands used:

```powershell
ollama --version

ollama pull llama3.2

pip install -r requirements.txt

python main.py
```

**Final Result:** Successfully completed the Llama 3.2 baseline evaluation and generated Release v0.1.

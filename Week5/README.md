

In Week 5, I developed a Token Economics budgeting tool to estimate the token consumption, API expenses and rate-limit requirements of an LLM-based application. The program calculates expected usage and checks whether the proposed feature stays within the specified budget and provider limits.

Steps I followed:

1. Created a Python project named TokenEconomics in VS Code.
2. Set up the project files, including `budget.py`, `test_budget.py`, `.env` and `requirements.txt`.
3. Installed the required `python-dotenv` library.
4. Configured token usage, API pricing, daily requests and monthly budget values in the `.env` file.
5. Implemented a Python program using a dataclass to manage feature budget assumptions.
6. Calculated input tokens, output tokens and total daily token consumption.
7. Estimated daily and monthly API costs using the configured token prices.
8. Checked RPM and TPM limits by applying a safety margin.
9. Generated a budget report to identify whether the proposed LLM feature meets the cost and capacity requirements.

Commands used:

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python budget.py

python -m unittest test_budget.py

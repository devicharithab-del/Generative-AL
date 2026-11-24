

In Week 2, I developed a provider-independent LLM client that supports both Google's Gemini cloud model and the locally running Ollama model. The main objective was to access different LLM providers through a single Python interface.

Steps I followed:

1. Downloaded and installed Ollama on my local system.
2. Verified the Ollama installation using PowerShell.
3. Downloaded the Llama 3.2 model using the Ollama command.
4. Created a Week 2 project folder in VS Code.
5. Designed a common LLM interface using Python's abstract base class.
6. Connected Gemini and Ollama as separate providers.
7. Developed a main program to select the provider and enter prompts.
8. Tested the application by generating responses using both models.

Commands used:

ollama --version

ollama pull llama3.2

cd week-2

pip install -r requirements.txt

python main.py

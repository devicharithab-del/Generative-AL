

In Week 4, I carried out a multilingual tokenization experiment to compare BPE, WordPiece and SentencePiece methods. I used pretrained tokenizer models to analyse how English, Telugu and Hindi sentences are converted into smaller tokens.

Steps I followed:

1. Created a project folder in VS Code for the Week 4 experiment.
2. Activated the existing Python virtual environment.
3. Installed the Transformers and SentencePiece packages.
4. Loaded the GPT-2, Multilingual BERT and XLM-R tokenizer models.
5. Entered sample sentences in English, Telugu and Hindi.
6. Wrote a Python program to tokenize the given sentences.
7. Extracted the generated tokens and their corresponding token IDs.
8. Compared the token counts for all three tokenizer models.
9. Observed how tokenization differs across different languages.

Commands used:

..\\.MyEnv\Scripts\Activate.ps1

pip install -r requirements.txt

python tokenizer_comparison.py

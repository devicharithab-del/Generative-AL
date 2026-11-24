

In Week 3, I explored and compared three popular tokenization techniques: BPE, WordPiece and SentencePiece. I used pretrained tokenizer models to understand how English, Telugu and Hindi sentences are divided into smaller tokens.

Steps I followed:

1. Created a Python project in VS Code.
2. Installed the required libraries, Transformers and SentencePiece.
3. Selected three pretrained tokenizer models: GPT-2, Multilingual BERT and XLM-R.
4. Provided sample sentences in English, Telugu and Hindi.
5. Loaded the pretrained tokenizers using the Hugging Face library.
6. Converted the input sentences into tokens and token IDs.
7. Compared the token pieces and total token counts for all three languages.
8. Observed how different tokenization methods produce different results.

Commands used:

..\\.MyEnv\Scripts\Activate.ps1

pip install -r requirements.txt

python tokenizer_comparison.py

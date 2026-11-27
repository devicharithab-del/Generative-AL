 Week 7 – Next Token Prediction

In Week 7, I implemented a next-token prediction program using the DistilGPT-2 pretrained language model. The program takes a user prompt, generates token probabilities, displays the top 5 next-token predictions with their logits and identifies the most likely next token.

 Steps I followed:

1. Created a Python project in VS Code.
2. Imported the required PyTorch and Transformers libraries.
3. Loaded the pretrained DistilGPT-2 model and tokenizer.
4. Accepted a text prompt from the user.
5. Converted the input text into tokens.
6. Generated logits and converted them into probabilities using Softmax.
7. Displayed the top 5 next-token predictions with their probabilities and raw logits.
8. Identified the most likely next token using Argmax.

Commands used:

```powershell
pip install torch transformers

python main.py
```

**Final Result:** Successfully implemented next-token prediction and displayed the top 5 token predictions with probabilities and logits.

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load a small pretrained language model
model_name = "distilgpt2"

print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

model.eval()

print("Model loaded successfully!")

# Get input from user
prompt = input("\nEnter your prompt: ")

# Convert text into tokens
inputs = tokenizer(prompt, return_tensors="pt")

# Get model output
with torch.no_grad():
    outputs = model(**inputs)

# Extract logits of the last token position
logits = outputs.logits[0, -1, :]

# Convert logits into probabilities
probabilities = torch.softmax(logits, dim=-1)

# Get top 5 predictions
top_k = 5
top_probs, top_indices = torch.topk(probabilities, top_k)

print("\nInput Prompt:", prompt)
print("\nTop 5 Next Token Predictions:")
print("-" * 45)

for i in range(top_k):
    token_id = top_indices[i].item()
    token = tokenizer.decode([token_id])
    probability = top_probs[i].item() * 100

    print(f"{i+1}. Token: {repr(token):15} Probability: {probability:.4f}%")

# Display raw logits
print("\nRaw Logits of Top 5 Tokens:")
print("-" * 45)

for i in range(top_k):
    token_id = top_indices[i].item()
    logit = logits[token_id].item()
    token = tokenizer.decode([token_id])

    print(f"Token: {repr(token):15} Logit: {logit:.4f}")

# Generate next token
next_token_id = torch.argmax(probabilities).unsqueeze(0)
next_token = tokenizer.decode(next_token_id)

print("\nMost Likely Next Token:", repr(next_token))

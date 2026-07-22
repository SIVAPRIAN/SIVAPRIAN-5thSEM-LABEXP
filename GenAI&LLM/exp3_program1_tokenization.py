# Program 1 - Tokenization
import logging
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)

from transformers import AutoTokenizer

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Artificial Intelligence is transforming education."

# Tokenize
tokens = tokenizer.tokenize(text)

print("Original Text:")
print(text)

print("\nTokens:")
print(tokens)

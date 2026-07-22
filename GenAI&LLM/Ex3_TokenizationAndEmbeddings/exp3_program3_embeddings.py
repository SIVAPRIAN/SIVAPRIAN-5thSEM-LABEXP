# Program 3 - Word Embeddings
import logging
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)

import transformers
transformers.logging.set_verbosity_error()

from transformers import AutoTokenizer, AutoModel
import torch

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

text = "Artificial Intelligence"

inputs = tokenizer(text, return_tensors="pt")

# Disable gradient calculation
with torch.no_grad():
    outputs = model(**inputs)

# Last hidden state
embeddings = outputs.last_hidden_state

print("Embedding Shape:")
print(embeddings.shape)

print("\nEmbedding Vector for First Token:")
print(embeddings[0][0][:10])

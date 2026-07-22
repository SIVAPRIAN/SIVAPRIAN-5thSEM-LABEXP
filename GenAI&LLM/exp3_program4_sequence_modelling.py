# Program 4 - Sequence Modelling Using BERT
import logging
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)

import transformers
transformers.logging.set_verbosity_error()

from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

sentence = "The cat sat on the mat."

inputs = tokenizer(sentence, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

hidden_states = outputs.last_hidden_state

tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

print("Token\t\tEmbedding Size")

for token, embedding in zip(tokens, hidden_states[0]):
    print(f"{token:12} {embedding.shape}")

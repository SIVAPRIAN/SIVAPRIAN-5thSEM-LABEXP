from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_name = "gpt2"

print("Loading GPT-2 model and tokenizer...")
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Set pad_token_id to eos_token_id to avoid warning
model.config.pad_token_id = model.config.eos_token_id

prompt = "Define Artificial Intelligence is transforming education.."
print(f"Prompt: {prompt}\n")

input_ids = tokenizer.encode(
    prompt,
    return_tensors="pt",
    add_special_tokens=True
)

attention_mask = torch.ones(
    input_ids.shape,
    dtype=torch.long
)

print("Generating text...")
output = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_length=100,
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    top_k=50,
    top_p=0.95,
    temperature=0.7,
    do_sample=True  # Required when temperature/top_k/top_p are used
)

generated_text = tokenizer.decode(
    output[0],
    skip_special_tokens=True
)

print("\n--- Generated Output ---")
print(generated_text)
print("------------------------")

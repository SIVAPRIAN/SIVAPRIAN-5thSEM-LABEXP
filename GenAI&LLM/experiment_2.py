from transformers import pipeline

# -------------------------------
# Sentiment Analysis
# -------------------------------

print("Sentiment Analysis")
print("SENTIMENT ANALYSIS RESULTS")
print("="*50)
print()

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

texts = [
    "I love learning Generative AI.",
    "This course is difficult.",
    "The workshop was okay."
]

for i, text in enumerate(texts):
    result = sentiment(text)[0]
    print(f"Text: {text}")
    print(result["label"])
    if i < len(texts) - 1:
        print()

# -------------------------------
# Document Classification
# -------------------------------

print("Document Classification")
print("DOCUMENT CLASSIFICATION RESULTS")
print("="*50)
print()

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

text = """
Large Language Models are transforming artificial intelligence
and enabling advanced conversational systems.
"""

labels = [
    "Technology",
    "Sports",
    "Education",
    "Business"
]

result = classifier(text, labels)

print("Predicted Category:")
print(result["labels"][0])

print("\nAll Scores:")
for label, score in zip(result["labels"], result["scores"]):
    print(f"{label} : {score:.4f}")

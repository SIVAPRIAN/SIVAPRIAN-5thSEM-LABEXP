# Experiment 2: Perform Sentiment Analysis and Document Classification Using Foundation Models

## Aim
To perform sentiment analysis and document classification using pre-trained foundation models based on transformer architectures.

---

## Objectives
1. Analyze the sentiment of text data using a pre-trained sentiment analysis model.
2. Classify documents into predefined categories using a zero-shot classification model.
3. Understand the application of foundation models in Natural Language Processing (NLP) tasks.

---

## Theory

### Sentiment Analysis
Sentiment Analysis is a Natural Language Processing (NLP) technique used to determine the emotional tone of a text. It identifies whether a piece of text expresses a positive, negative, or neutral sentiment.

Foundation models such as BERT and DistilBERT are pre-trained on large text corpora and fine-tuned for sentiment classification tasks. In this experiment, `distilbert-base-uncased-finetuned-sst-2-english` is used.

### Document Classification & Zero-Shot Learning
Document Classification is the process of assigning predefined categories to textual documents. Traditional methods require task-specific training datasets. However, foundation models can perform classification using **Zero-Shot Learning**, where the model predicts categories without any prior task-specific training or fine-tuning on those labels.

In this experiment:
- **DistilBERT** is used for Sentiment Analysis.
- **BART Large MNLI** (`facebook/bart-large-mnli`) is used for Zero-Shot Document Classification.

---

## Software & Hardware Requirements
* Python 3.x
* Google Colab / Jupyter Notebook
* PyTorch & Hugging Face Transformers

### Installation Commands
```bash
pip install transformers torch
```

---

## Algorithm

### Sentiment Analysis
1. Load a pre-trained sentiment analysis pipeline.
2. Provide input text samples.
3. Predict the sentiment label and confidence score for each sample.
4. Display the results.

### Document Classification
1. Load a pre-trained zero-shot classification pipeline.
2. Define the target document content.
3. Specify candidate labels/categories.
4. Predict relevance scores for each category.
5. Display category scores and the predicted label.

---


## Sample Execution

### Sample Output
```text
SENTIMENT ANALYSIS RESULTS
==================================================
Text: I love learning Generative AI.
[{'label': 'POSITIVE', 'score': 0.9998}]
--------------------------------------------------
Text: This course is difficult.
[{'label': 'NEGATIVE', 'score': 0.9996}]
--------------------------------------------------
Text: The workshop was okay.
[{'label': 'POSITIVE', 'score': 0.9985}]
--------------------------------------------------

DOCUMENT CLASSIFICATION RESULTS
==================================================
Predicted Category:
Technology

All Scores:
Technology: 0.9600
Education: 0.0200
Business: 0.0100
Sports: 0.0100
```

---

## Result
Thus, sentiment analysis and document classification were successfully performed using pre-trained foundation models. The sentiment of input text was identified, and the document was accurately classified into the most relevant category.

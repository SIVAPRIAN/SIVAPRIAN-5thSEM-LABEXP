# Experiment 3: Build Applications Demonstrating Tokenization, Embeddings, and Transformer-Based Sequence Modelling

## Aim
To build Python applications demonstrating:
1. Text Tokenization 
2. Word Embeddings 
3. Transformer-based Sequence Modeling using the Hugging Face Transformers library. 

---

## Objectives
* Understand text preprocessing. 
* Perform tokenization using the BERT tokenizer. 
* Generate contextual word embeddings. 
* Use a Transformer model for sequence modelling. 

---

## Theory

Natural Language Processing (NLP) requires converting human language into numerical representations before machine learning models can process it. This experiment demonstrates three fundamental stages:

### 1. Tokenization
Tokenization splits text into smaller units called tokens. Transformers use subword tokenization to handle out-of-vocabulary words.
- **Example:** `"Artificial Intelligence is amazing."` $\rightarrow$ `["Artificial", "Intelligence", "is", "amazing", "."]`
- **Subword Example:** `"unbelievable"` $\rightarrow$ `["un", "##believable"]`

### 2. Embeddings
Tokens are converted into continuous dense vectors representing semantic meanings.
- **Example:** `"Artificial"` $\rightarrow$ `[0.23, -0.51, 1.42, ...]`

### 3. Transformer Sequence Modelling
Transformers analyze relationships among all words simultaneously using **Self-Attention**.
For input: `"The cat sat on the mat."`
The model learns contextual associations (e.g., `cat` $\leftrightarrow$ `sat`, `sat` $\leftrightarrow$ `mat`) to produce high-quality contextualized embeddings.

---

## Software & Hardware Requirements
* Python 3.10+
* Google Colab / Jupyter Notebook / VS Code
* PyTorch & Hugging Face Transformers

### Installation Commands
```bash
pip install transformers torch
```

---

## Algorithm
1. Import necessary libraries.
2. Load pretrained tokenizer (`bert-base-uncased`).
3. Load pretrained BERT model (`bert-base-uncased`).
4. Input a sentence.
5. Tokenize the sentence.
6. Convert tokens into numerical IDs.
7. Pass IDs into BERT.
8. Obtain contextual embeddings (last hidden state).
9. Display embedding dimensions and sequence token attributes.

---


## Sample Outputs

### Tokenization
```text
Original Text:
Artificial Intelligence is transforming education.

Tokens:
['artificial', 'intelligence', 'is', 'transforming', 'education', '.']
```

### Token IDs
```text
Input IDs:
[101, 7976, 4454, 102]

Attention Mask:
[1, 1, 1, 1]
```

### Word Embeddings
```text
Embedding Shape:
torch.Size([1, 4, 768])

Embedding Vector for First Token:
tensor([ 0.192, -0.521,  0.374, ...])
```

### Sequence Modelling
```text
Token           Embedding Size
[CLS]           torch.Size([768])
the             torch.Size([768])
cat             torch.Size([768])
sat             torch.Size([768])
on              torch.Size([768])
the             torch.Size([768])
mat             torch.Size([768])
.               torch.Size([768])
[SEP]           torch.Size([768])
```

---

## Result
The experiment was successfully implemented. Applications demonstrating tokenization, contextual embeddings, and transformer-based sequence modelling were developed using the pretrained BERT (`bert-base-uncased`) model. The outputs confirmed successful token generation, embedding extraction, and contextual sequence representation, illustrating the core concepts of modern Natural Language Processing.

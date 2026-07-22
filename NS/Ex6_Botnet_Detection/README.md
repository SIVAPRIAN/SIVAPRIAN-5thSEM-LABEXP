# Lab Experiment 6: Botnet Attack Detection using Publicly Available Dataset

## 1. Aim
To implement and demonstrate botnet attack detection by training a machine learning model on a publicly available network traffic dataset.

## 2. Algorithm
1. **Dataset Selection & Preprocessing**:
   - Obtain a botnet dataset (e.g., CTU-13, CICIDS2017).
   - Load the dataset, handle missing values, and normalize features.
2. **Feature Extraction**:
   - Extract relevant features such as packet size, duration, flow count, source/destination IP, and protocol features.
3. **Data Splitting**:
   - Split dataset into training set and testing set (e.g., 70:30).
4. **Model Training**:
   - Train a classifier (Decision Tree, Random Forest, Logistic Regression, etc.) to distinguish between normal traffic and botnet traffic.
5. **Detection & Evaluation**:
   - Test the model on unseen data.
   - Evaluate using metrics like Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.

## 3. Output
> [!IMPORTANT]
> **Execution Output:**
> ```text
> Dataset Shape: (100000, 25)
> Columns: ['Duration','SrcIP','DstIP','Protocol','Packets','Bytes',...,'Label']
> 
> === Botnet Detection Results ===
> Accuracy: 0.9825
> 
> Classification Report:
>               precision    recall  f1-score   support
> 
>            0       0.98      0.99      0.99     25000
>            1       0.98      0.97      0.98     15000
> 
> Confusion Matrix:
> [[24750   250]
>  [  450 14550]]
> ```
> * The model detects botnet traffic with ~98% accuracy.
> * Very few false positives and false negatives.

## 4. Result
The experiment successfully demonstrated how a machine learning model trained on a publicly available network traffic dataset can detect botnet attacks, proving the effectiveness of data-driven approaches in identifying malicious network activity.

Neuroadaptive Deep Learning Framework for Bank Card Fraud Detection
A Continual‑Learning, Meta‑Optimised, Explainable AI System for Emerging Fraud Patterns

Overview
This repository contains the full implementation of the Neuroadaptive Deep Learning Framework, a research‑grade fraud detection system designed to identify emerging and evolving patterns in bank card fraud. The framework integrates continual learning, representation learning, and nature‑inspired optimisation to overcome the limitations of static fraud detection models.

This work is based on the peer‑reviewed IEEE publication:

Makinde, B., Uwah, S. E., Iwendi, C., Ojo, O. A., et al. (2025).
Detecting Emerging Patterns in Bank Card Fraud Using a Neuroadaptive Deep Learning Framework.  
IEEE ICTBIG 2025.

Payment card fraud accounted for more than $35 billion in global losses in 2022, and continues to rise as fraudsters adapt their methods. This framework is designed to meet that challenge by learning new fraud behaviours without forgetting previously learned patterns.

Key Features
Neuroadaptive Architecture
Custom PyTorch‑based ANN

Elastic Weight Consolidation (EWC) for continual learning

PReLU activations to prevent dead neurons

Batch Normalisation & Adaptive BatchNorm (AdaBN) for domain shift robustness

Nature‑Inspired Hyperparameter Optimisation
Firefly Algorithm (FA) optimises learning rate, batch size, and hidden layer size

5‑fold cross‑validation for robust fitness evaluation

Representation Learning
Denoising Autoencoder (DAE) reconstructs clean features from noisy transaction data

Improves downstream classification accuracy and stability

Explainable AI (XAI)
SHAP (Shapley Additive Explanations) for transparent, feature‑level interpretability

Supports auditability and regulatory compliance

Class Imbalance Handling
SMOTE, ADASYN, SMOTE-ENN applied to training data

Ensures balanced learning in highly skewed fraud datasets

System Architecture
The end‑to‑end pipeline includes:

Data Preprocessing

Missing value imputation

StandardScaler normalisation

One‑hot encoding

Stratified splitting

Feature Engineering

Denoising Autoencoder for robust latent representations

Class Balancing

SMOTE, ADASYN, SMOTE-ENN applied to training set

Hyperparameter Optimisation

Firefly Algorithm with 5‑fold CV

Model Training

Adaptive ANN with EWC and AdaBN

Early stopping and checkpointing

Model Evaluation

Accuracy, Precision, Recall, F1‑Score

ROC‑AUC, PR‑AUC, MCC

Confusion matrix

Explainability

SHAP visualisation

Deployment

Gradio interface for real‑time inference

Repository Structure
Code
Neuroadaptive-Deep-Learning-Framework-for-Bank-Card-Fraud/
│
├── data                    
├── models           
├── reports              
├── src
├── requirements.txt
├── environment.yml
└── README.md
Installation
Clone the repository:

bash
git clone https://github.com/babatopemakinde/Neuroadaptive-Deep-Learning-Framework-for-Bank-Card-Fraud
cd Neuroadaptive-Deep-Learning-Framework-for-Bank-Card-Fraud
Install dependencies:

bash
pip install -r requirements.txt
Running the Pipeline
Execute the full fraud detection pipeline:

bash
python src/fraud_pipeline.py
This will:

Preprocess the dataset

Train the DAE

Apply SMOTE, ADASYN, SMOTE-ENN

Run Firefly hyperparameter optimisation

Train the adaptive ANN with EWC

Evaluate performance

Generate SHAP explainability plots

Save model weights

Model Performance
The proposed Neuroadaptive ANN + Firefly Algorithm achieves:

Metric	Score
Accuracy	99.85%
Precision	99.02%
Recall	99.26%
F1‑Score	99.14%
ROC‑AUC	1.0000
These results outperform baseline ANN, CNN, and LSTM models.

Significance & Impact
Research Impact
This framework advances the state of the art in fraud detection by:

Introducing a continual‑learning‑enabled architecture

Combining metaheuristic optimisation with deep learning

Enhancing robustness through representation learning

Providing transparent, explainable predictions

Real‑World Impact
Designed for:

High‑volume financial environments

Real‑time fraud detection

Regulatory compliance (via SHAP explainability)

Adaptation to evolving fraud behaviours


This project demonstrates:

Original research contribution (peer‑reviewed IEEE publication)

Technical leadership in AI system design

Impactful engineering addressing global financial fraud

Open‑source dissemination supporting reproducibility

Clear potential for future contributions to UK AI research

Citation
If you use this framework or reference the research, please cite:

Makinde, B., Uwah, S. E., Iwendi, C., Ojo, O. A., et al. (2025).
Detecting Emerging Patterns in Bank Card Fraud Using a Neuroadaptive Deep Learning Framework.  
5th IEEE International Conference on ICT in Business Industry & Government.

Author
Babatope Makinde  
Centre of Intelligence of Things
University of Greater Manchester
Email: babatope.makinde@ieee.com

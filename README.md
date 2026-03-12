# Neuroadaptive-Deep-Learning-Framework-for-Bank-Card-Fraud
End-to-end fraud detection pipeline contains preprocesses data with imputation, scaling, encoding, and a denoising autoencoder, balances classes, tunes hyperparameters via Firefly optimisation, trains a PyTorch model with EWC and AdaBN, evaluates performance, and deploys a Gradio demo.


Detecting Emerging Patterns in Bank Card Fraud Using a Neuroadaptive Deep Learning Framework

Project Overview
This project introduces a state-of-the-art neuroadaptive framework designed to secure digital financial systems against evolving fraud tactics. Traditional static models often become obsolete as fraudsters adapt; this framework solves that by integrating continual learning and nature-inspired optimisation to detect emerging fraudulent patterns in real-time.

Developed at the University of Greater Manchester, this research addresses the critical global challenge of payment card fraud, which accounted for over $35 billion in global losses in 2022.

Key Technical Innovations
Neuroadaptive Architecture: A custom-built Artificial Neural Network (ANN) featuring Elastic Weight Consolidation (EWC) to enable continual learning without "catastrophic forgetting" of past fraud patterns.
Nature-Inspired Optimisation: Implements the Firefly Algorithm for rapid and efficient hyperparameter tuning, significantly enhancing model adaptivity.
Representation Learning: Utilises Denoising Autoencoders (DAE) to reconstruct clean transaction data from noisy inputs, improving feature extraction.
Explainable AI (XAI): Integrated SHAP (Shapley Additive Explanations) to provide transparent, feature-level insights into why specific transactions are flagged as fraudulent.

Tech Stack & Methodology
Architecture & Framework
Deep Learning: Adaptive ANN with PReLU activation and Batch Normalisation.
Continual Learning: Elastic Weight Consolidation (EWC) and Adaptive Batch Normalization (AdaBN) to handle domain shifts.
Data Balancing: SMOTE, SMOTE-ENN, and ADASYN to address extreme class imbalance in financial datasets.

The Pipeline
Preprocessing: Feature normalisation using StandardScaler and stratified splitting.
Feature Engineering: Denoising Autoencoder for robust representation learning.
Optimisation: Firefly Algorithm-driven 5-fold cross-validation.
Inference & Interpretability: Real-time classification with SHAP visualisation for auditability.

Significance & Impact
Resilience: Addresses the "Concept Drift" common in financial data by learning new fraud patterns without unlearning old ones.
Transparency: Moves away from "Black Box" AI by providing clear prediction reasonability, crucial for regulatory compliance in banking.
Scalability: Designed for high-volume digital finance environments, ensuring reduced operational costs and enhanced customer confidence.

Citation
If you use this framework or research, please cite:
Makinde, B., Uwah, S. E., Iwendi, C., et al. (2025). Detecting Emerging Patterns in Bank Card Fraud Using a Neuroadaptive Deep Learning Framework. 5th IEEE International Conference on ICT in Business Industry & Government.

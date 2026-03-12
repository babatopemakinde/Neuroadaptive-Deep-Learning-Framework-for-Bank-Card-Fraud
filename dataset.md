The dataset contains 1,000,000 credit card transaction records designed for fraud detection research. Each record represents a single transaction with 7 predictive features and 1 binary target variable (fraud) indicating whether the transaction is fraudulent.

Source: Kaggle
Link: https://www.kaggle.com/datasets/elakiyasekar/card-transdata

Features

distance_from_home – Distance between the transaction location and the cardholder’s home location. Larger distances may indicate suspicious activity.

distance_from_last_transaction – Distance between the current transaction and the previous transaction location. Large jumps may signal abnormal behavior.

ratio_to_median_purchase_price – Ratio of the current transaction amount to the cardholder’s median purchase price, capturing spending anomalies.

repeat_retailer – Binary indicator showing whether the transaction occurred at a retailer previously used by the customer (1 = yes, 0 = no).

used_chip – Indicates whether the card’s chip was used for the transaction.

used_pin_number – Indicates whether a PIN was used during the transaction.

online_order – Binary variable specifying whether the purchase was made online.

Target Variable

fraud – Binary label where 1 indicates a fraudulent transaction and 0 indicates a legitimate transaction.

Dataset Characteristics

Total records: 1,000,000

Features: 7 input features + 1 target variable

Fraud rate: ~8.74% fraudulent transactions

Legitimate transactions: ~91.26%

The dataset reflects highly imbalanced fraud detection conditions, typical in financial security problems, making it suitable for testing machine learning techniques such as anomaly detection, class imbalance handling, and fraud classification models.

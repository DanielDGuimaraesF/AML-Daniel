import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\diel9\\Downloads\\AML case Data.xlsx'
xls = pd.ExcelFile(file_path)

transactions_df = pd.read_excel(file_path, sheet_name='transactions')

features_1 = transactions_df[['amount', 'payment_method', 'capture_method', 'status']]

features_1_encoded = pd.get_dummies(features_1, drop_first=True)

isolation_forest_1 = IsolationForest(contamination=0.1, random_state=42)
transactions_df['anomaly_score_1'] = isolation_forest_1.fit_predict(features_1_encoded)

anomalies_1 = transactions_df[transactions_df['anomaly_score_1'] == -1].groupby('merchant_id').size()

top_10_merchants_1 = anomalies_1.nlargest(10)

plt.figure(figsize=(10, 6))
top_10_merchants_1.plot(kind='bar', title='Top 10 Merchants with Most Anomalies (Model 1)')
plt.xlabel('Merchant ID')
plt.ylabel('Number of Anomalies')
plt.show()

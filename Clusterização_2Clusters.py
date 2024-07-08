import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

file_path = 'C:\\Users\\diel9\\Downloads\\AML case Data.xlsx'
data = pd.read_excel(file_path, sheet_name='transactions')

data['is_denied'] = data['status'] == 'denied'

merchant_group = data.groupby('merchant_id').agg(
   mean_amount=('amount', 'mean'),
   refund_rate=('status', lambda x: (x == 'refunded').mean() * 100),  # Converter para porcentagem
   denied_rate=('is_denied', 'mean')
).reset_index()

scaler = StandardScaler()
scaled_features = scaler.fit_transform(merchant_group[['mean_amount', 'refund_rate', 'denied_rate']])

kmeans = KMeans(n_clusters=2, random_state=0).fit(scaled_features)

merchant_group['cluster'] = kmeans.labels_

cluster_risk = merchant_group.groupby('cluster').agg(
   refund_rate=('refund_rate', 'mean'),
   denied_rate=('denied_rate', 'mean')
)

low_risk_cluster = cluster_risk.mean(axis=1).idxmin()

merchant_group['adjusted_cluster'] = merchant_group['cluster'].apply(
   lambda x: 1 if x == low_risk_cluster else 0
)

plt.figure(figsize=(10, 6))
colors = ['red', 'blue']
for cluster in range(2):
   clustered_data = merchant_group[merchant_group['adjusted_cluster'] == cluster]
   plt.scatter(
       clustered_data['mean_amount'],
       clustered_data['refund_rate'],
       color=colors[cluster],
       label=f'Cluster {cluster}',
       s=clustered_data['denied_rate'] * 1000,  # Dimensionar o tamanho dos pontos pela taxa de negados
       alpha=0.6
   )

plt.xlabel('Ticket Médio')
plt.ylabel('Taxa de Reembolso (%)')
plt.title('Clusterização de Comerciantes (considerando taxa de transações negadas)')
plt.legend()
plt.show()

low_risk_merchants = merchant_group[merchant_group['adjusted_cluster'] == 1]

print(low_risk_merchants)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

file_path = 'C:\\Users\\diel9\\Downloads\\AML case Data.xlsx'
data = pd.read_excel(file_path, sheet_name='transactions')

data['is_denied'] = data['status'] == 'denied'
data['is_refunded'] = data['status'] == 'refunded'

merchant_group = data.groupby('merchant_id').agg(
    mean_amount=('amount', 'mean'),
    refund_rate=('is_refunded', 'mean'),
    denied_rate=('is_denied', 'mean')
).reset_index()

scaler = StandardScaler()
scaled_features = scaler.fit_transform(merchant_group[['mean_amount', 'refund_rate', 'denied_rate']])

inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=0).fit(scaled_features)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Número de Clusters')
plt.ylabel('Inertia')
plt.title('Método do Cotovelo para Encontrar o Número Ótimo de Clusters')
plt.show()

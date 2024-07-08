AML Case Study - Python Scripts
Este repositório contém três scripts em Python para a análise de dados de transações financeiras com foco em Prevenção à Lavagem de Dinheiro (AML). Cada script aborda uma abordagem diferente para detecção de anomalias e clusterização de comerciantes. Abaixo está uma descrição detalhada de cada script.

1. Detecção de Anomalias com Isolation Forest
Arquivo: anomaly_detection_isolation_forest.py

##Descrição
Este script utiliza o algoritmo Isolation Forest para detectar anomalias em transações financeiras. Ele realiza a codificação das variáveis categóricas e aplica o modelo de Isolation Forest para identificar transações anômalas.

##Etapas do Script
Importação das bibliotecas necessárias: pandas, sklearn.ensemble.IsolationForest e matplotlib.pyplot.
Leitura dos dados de transações a partir de um arquivo Excel.
Seleção e codificação das características relevantes (amount, payment_method, capture_method, status).
Aplicação do modelo Isolation Forest para detectar anomalias.
Agrupamento e contagem das anomalias por merchant_id.
Plotagem dos 10 comerciantes com maior número de anomalias.

2. Clusterização com KMeans (Elbow Method)
Arquivo: kmeans_elbow_method.py

##Descrição
Este script utiliza o algoritmo KMeans para realizar a clusterização dos comerciantes com base em características específicas. O Método do Cotovelo é usado para determinar o número ideal de clusters.

##Etapas do Script
Importação das bibliotecas necessárias: pandas, matplotlib.pyplot, sklearn.cluster.KMeans e sklearn.preprocessing.StandardScaler.
Leitura dos dados de transações a partir de um arquivo Excel.
Cálculo de métricas agregadas por merchant_id (mean_amount, refund_rate, denied_rate).
Normalização das características usando StandardScaler.
Aplicação do KMeans para diferentes valores de k e cálculo da inércia.
Plotagem da inércia em função do número de clusters para encontrar o ponto ideal (Método do Cotovelo).

3. Clusterização de Comerciantes e Identificação de Baixo Risco
Arquivo: merchant_clustering_low_risk.py

##Descrição
Este script também utiliza o algoritmo KMeans, mas com um foco específico na identificação de comerciantes de baixo risco. Ele clusteriza os comerciantes e ajusta os clusters com base nas taxas de reembolso e negação.

##Etapas do Script
Importação das bibliotecas necessárias: pandas, matplotlib.pyplot, sklearn.cluster.KMeans e sklearn.preprocessing.StandardScaler.
Leitura dos dados de transações a partir de um arquivo Excel.
Cálculo de métricas agregadas por merchant_id (mean_amount, refund_rate, denied_rate).
Normalização das características usando StandardScaler.
Aplicação do KMeans para determinar clusters iniciais.
Ajuste dos clusters para identificar comerciantes de baixo risco.
Plotagem dos clusters, destacando comerciantes de baixo risco.
Impressão dos comerciantes identificados como de baixo risco.

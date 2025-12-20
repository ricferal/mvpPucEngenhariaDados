# 📊 Amazon Sales Analysis - MVP Pipeline de Dados

**Projeto:** MVP Engenharia de Dados - Análise de Vendas Amazon  
**Autor:** Ricardo Fernandes de Almeida  
**Disciplina:** Engenharia de Dados - PUC-Rio  
**Data:** Dezembro 2025

---

## 🎯 Visão Geral

Este notebook implementa um **pipeline completo de dados** para análise de vendas da Amazon, utilizando a **Arquitetura Medalhão** (Bronze, Silver, Gold) no Databricks. O objetivo é responder perguntas estratégicas de negócio sobre:

- 📈 Performance de vendas
- 👥 Comportamento do cliente
- 📦 Análise de produtos
- ⚙️ Operações e logística
- ⏰ Sazonalidade e tendências

---

## 📋 Arquivos do Projeto

| Arquivo | Descrição |
|---------|-----------|
| `Amazon_Sales_Analysis_MVP.ipynb` | Notebook principal com pipeline completo |
| `catalogo_de_dados_tabelas_amazon.ipynb` | Catálogo de dados com DER das tabelas |
| `Consultas_SQL_Avancadas_Amazon.ipynb` | 16 consultas SQL especializadas |
| `Amazon.csv` | Dataset fonte (Kaggle) |


---

## 🚀 Passo a Passo do Pipeline

### **1. 🎯 Objetivos do Projeto**

- Apresenta o problema de negócio e as perguntas de pesquisa
- Lista as principais métricas e insights esperados
- Define KPIs estratégicos para análise

### **2. 🥉 Coleta de Dados (Bronze Layer)**

- Realiza o download do dataset `Amazon.csv` via Kaggle
- Define o schema completo dos dados brutos
- Carrega os dados na camada **Bronze** (Delta Table)
- Realiza análise inicial de volume e períodos temporais

**Características da Bronze Layer:**
- Dados brutos sem transformações
- Preservação do formato original
- Auditoria de carga (timestamp, source)

### **3. 🥈 Análise e Limpeza de Dados (Silver Layer)**

- Analisa qualidade dos dados: valores nulos, duplicados e tipos
- Aplica transformações e validações de negócio
- Remove inconsistências e registros inválidos
- Cria camada **Silver** com dados limpos e estruturados

**Transformações Aplicadas:**
- Padronização de tipos de dados
- Tratamento de valores nulos e outliers
- Validação de integridade referencial
- Enriquecimento com campos calculados

### **4. 🥇 Modelagem Dimensional (Gold Layer)**

Cria **Star Schema** com tabelas otimizadas para análise:

**Tabelas Dimensionais:**
- `dim_customer` - Dimensão de clientes (país, estado, segmento)
- `dim_product` - Dimensão de produtos (categoria, marca, preço)
- `dim_seller` - Dimensão de vendedores (segmento de negócio)
- `dim_date` - Dimensão temporal (ano, mês, trimestre, dia da semana)

**Tabela Fato:**
- `fact_sales` - Fatos de vendas com todas as métricas de negócio

**Métricas Calculadas:**
- Receita total, bruta e líquida
- Descontos aplicados
- Custos de frete
- Taxas e percentuais

### **5. ✅ Análise de Qualidade dos Dados**

Gera relatórios completos sobre:

| Dimensão | Métricas |
|----------|----------|
| **Completude** | % de campos preenchidos por coluna |
| **Validade** | Conformidade com regras de negócio |
| **Consistência** | Integridade entre camadas |
| **Precisão** | Exatidão dos cálculos e agregações |

### **6. 🔍 Análise de Negócio (Consultas SQL)**

Executa **16 consultas SQL especializadas** para responder:

#### **📈 Performance de Vendas**
1. Volume total de vendas por mês e trimestre
2. Produtos com melhor performance de vendas
3. Impacto do desconto no volume de vendas

#### **👥 Comportamento do Cliente**
4. Países/regiões que geram mais receita
5. Ticket médio por cliente
6. Métodos de pagamento mais utilizados

#### **📦 Análise de Produtos**
7. Categorias de produtos mais vendidas
8. Distribuição de preços por categoria
9. Marcas com melhor performance

#### **⚙️ Análise Operacional**
10. Taxa de cancelamento e devolução
11. Impacto dos custos de frete na margem
12. Distribuição de status dos pedidos

#### **⏰ Análise Temporal**
13. Sazonalidade nas vendas
14. Períodos de maior volume de pedidos

### **7. 📊 Visualização e Insights**

- Gera gráficos e dashboards interativos com **Plotly**
- Explica os principais insights extraídos de cada consulta
- Apresenta recomendações estratégicas baseadas em dados

**Tipos de Visualizações:**
- Gráficos de linha (tendências temporais)
- Gráficos de barra (comparações categóricas)
- Heatmaps (sazonalidade)
- Treemaps (participação de mercado)
- Scatter plots (correlações)

### **8. 📝 Autoavaliação e Documentação**

- Resume os objetivos atingidos
- Documenta dificuldades encontradas
- Sugere melhorias futuras
- Apresenta a linhagem dos dados (data lineage)

---

## 💻 Como Executar

### **Pré-requisitos**

```bash
# Ambiente
- Databricks (cluster com suporte a Delta Lake e PySpark)
- Python 3.8+
- Permissão para instalar pacotes via %pip

# Dataset
- Amazon.csv (disponível no Kaggle)
```

### **Passo a Passo**

1. **Clone ou importe o projeto no Databricks:**
   ```bash
   # Faça upload dos arquivos .ipynb para o Databricks Workspace
   ```

2. **Configure o cluster:**
   - Databricks Runtime 11.3 LTS ou superior
   - Habilite Delta Lake
   - Configure permissões para instalação de pacotes

3. **Execute os notebooks na ordem:**
   ```
   1. Amazon_Sales_Analysis_MVP.ipynb (pipeline principal)
   2. catalogo_de_dados_tabelas_amazon.ipynb (documentação)
   3. Consultas_SQL_Avancadas_Amazon.ipynb (análises SQL)
   ```

4. **Ajuste caminhos de arquivos conforme necessário:**
   ```python
   # Exemplo: ajuste o caminho do dataset
   file_path = "/dbfs/FileStore/tables/Amazon.csv"
   ```

5. **Execute as células sequencialmente** seguindo o fluxo do índice

6. **Analise os resultados** e utilize os insights para tomada de decisão

---

## 📦 Requisitos Técnicos

### **Plataforma**
- ✅ Databricks (cluster com Delta Lake e PySpark)
- ✅ Databricks Runtime 11.3 LTS ou superior

### **Bibliotecas Python**
```python
pyspark
delta-spark
plotly
pandas
numpy
kaggle
```

### **Acesso a Dados**
- Dataset `Amazon.csv` (Kaggle)
- Credenciais Kaggle API (para download automático)

---

## 🏗️ Arquitetura do Projeto

```
📁 mvpEngenhariaDados/
│
├── 📊 Amazon.csv                                    # Dataset fonte
├── 📓 Amazon_Sales_Analysis_MVP.ipynb              # Pipeline principal
├── 📓 catalogo_de_dados_tabelas_amazon.ipynb       # Catálogo de dados + DER
├── 📓 Consultas_SQL_Avancadas_Amazon.ipynb         # 16 consultas SQL
├── 📄 requisitos.md                                 # Requisitos do projeto
└── 📄 README.md                                     # Este arquivo
```

### **Camadas de Dados**

```
🥉 Bronze Layer (Raw Data)
    ↓
🥈 Silver Layer (Cleaned & Validated)
    ↓
🥇 Gold Layer (Star Schema)
    ├── fact_sales
    ├── dim_customer
    ├── dim_product
    ├── dim_seller
    └── dim_date
```

---

## 🎯 Principais Funcionalidades

### ✅ **Pipeline de Dados Completo**
- Ingestão automatizada de dados
- Transformações com PySpark e Delta Lake
- Modelagem dimensional (Star Schema)
- Validação e qualidade de dados em todas as camadas

### ✅ **Análises Avançadas**
- 16 consultas SQL especializadas
- Métricas de negócio calculadas (YoY, MoM, market share)
- Segmentação de clientes e produtos
- Análise de sazonalidade e tendências

### ✅ **Visualizações Interativas**
- Dashboards com Plotly
- Gráficos de tendências temporais
- Análises comparativas
- Insights acionáveis

### ✅ **Documentação Completa**
- Catálogo de dados com DER
- Dicionário de dados
- Linhagem de transformações
- Boas práticas de engenharia de dados

---

## 📊 Principais Insights Gerados

### **Performance de Vendas**
- Identificação de produtos estrela e categorias campeãs
- Análise do impacto de descontos na receita
- Tendências de crescimento MoM e YoY

### **Comportamento do Cliente**
- Segmentação por valor (VIP, High Value, Standard)
- Análise de ticket médio e lifetime value
- Preferências de pagamento por região

### **Operacional**
- Taxa de cancelamento e devolução
- Impacto do frete na margem
- Eficiência operacional por status

### **Estratégico**
- Sazonalidade e períodos de pico
- Oportunidades de crescimento por categoria
- Recomendações para otimização de estoque

---


## 🤝 Contribuições

Este projeto foi desenvolvido como MVP para a disciplina de **Engenharia de Dados** da PUC-Rio. 

Sugestões de melhorias são bem-vindas! 

---

## 📞 Contato

**Autor:** Ricardo Fernandes de Almeida  
**Instituição:** PUC-Rio  
**Disciplina:** Engenharia de Dados  
**Período:** 2025

---

## 📄 Licença

Este projeto é de uso acadêmico e educacional.

---



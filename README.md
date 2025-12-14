# MVP Engenharia de Dados - PUC

## 📊 Visão Geral

Este projeto implementa um pipeline ETL (Extract, Transform, Load) completo para o MVP da disciplina de Engenharia de Dados da PUC. O sistema é modular, escalável e segue as melhores práticas de engenharia de dados.

## 🎯 Objetivos

- Implementar um pipeline ETL robusto e modular
- Demonstrar processos de extração, transformação e carga de dados
- Aplicar boas práticas de engenharia de dados
- Fornecer documentação clara e exemplos práticos

## 🏗️ Arquitetura

O projeto está organizado em três módulos principais:

```
mvpPucEngenhariaDados/
├── src/
│   ├── extract/          # Módulo de extração de dados
│   ├── transform/        # Módulo de transformação de dados
│   ├── load/            # Módulo de carga de dados
│   ├── pipeline.py      # Orquestrador do pipeline ETL
│   └── generate_sample_data.py  # Gerador de dados de exemplo
├── data/
│   ├── raw/             # Dados brutos
│   └── processed/       # Dados processados
├── config/              # Arquivos de configuração
├── logs/                # Logs do sistema
├── requirements.txt     # Dependências Python
├── Dockerfile          # Configuração Docker
└── docker-compose.yml  # Orquestração de containers
```

## 🔧 Componentes do Pipeline

### 1. Extract (Extração)
- Extração de dados de múltiplas fontes (CSV, JSON, APIs)
- Suporte a diferentes formatos de dados
- Validação e logging de dados extraídos

### 2. Transform (Transformação)
- Remoção de duplicatas
- Tratamento de valores faltantes
- Normalização de dados
- Agregações e filtros
- Conversão de tipos de dados

### 3. Load (Carga)
- Carga para CSV, JSON, Parquet
- Suporte a bancos de dados relacionais
- Diferentes modos de carga (append, replace)

## 🚀 Como Executar

### Pré-requisitos

- Python 3.11+
- Docker e Docker Compose (opcional)
- PostgreSQL (opcional, para persistência em banco de dados)

### Instalação Local

1. Clone o repositório:
```bash
git clone https://github.com/ricferal/mvpPucEngenhariaDados.git
cd mvpPucEngenhariaDados
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Gere dados de exemplo:
```bash
python src/generate_sample_data.py
```

4. Execute o pipeline:
```bash
python src/pipeline.py
```

### Execução com Docker

1. Build e execute os containers:
```bash
docker-compose up --build
```

2. Para executar em background:
```bash
docker-compose up -d
```

3. Para parar os containers:
```bash
docker-compose down
```

## 📝 Exemplo de Uso

### Uso Básico do Pipeline

```python
from src.pipeline import ETLPipeline

# Inicializar o pipeline
pipeline = ETLPipeline(config_path="config/pipeline_config.yaml")

# Executar o pipeline
pipeline.run_pipeline(
    source_path="data/raw/sample_data.csv",
    output_path="data/processed/processed_data.csv"
)
```

### Uso Individual dos Módulos

```python
from src.extract.extractor import DataExtractor
from src.transform.transformer import DataTransformer
from src.load.loader import DataLoader

# Extração
extractor = DataExtractor()
df = extractor.extract_from_csv("data/raw/sample_data.csv")

# Transformação
transformer = DataTransformer()
df = transformer.remove_duplicates(df)
df = transformer.handle_missing_values(df, strategy='drop')

# Carga
loader = DataLoader()
loader.load_to_csv(df, "data/processed/output.csv")
```

## 📊 Dados de Exemplo

O projeto inclui um gerador de dados de vendas com as seguintes características:

- **1000+ registros** de transações de vendas
- **Múltiplas categorias** de produtos
- **Dados de clientes** e regiões
- **Duplicatas intencionais** (~5%) para demonstrar limpeza
- **Valores faltantes** (~3%) para demonstrar tratamento

## 🔍 Funcionalidades

### Extração
- ✅ Leitura de CSV
- ✅ Leitura de JSON
- ✅ Integração com APIs REST
- ✅ Validação de dados na entrada

### Transformação
- ✅ Remoção de duplicatas
- ✅ Tratamento de valores nulos
- ✅ Normalização de dados numéricos
- ✅ Agregações e agrupamentos
- ✅ Filtros e condições
- ✅ Conversão de tipos

### Carga
- ✅ Exportação para CSV
- ✅ Exportação para JSON
- ✅ Exportação para Parquet
- ✅ Carga em banco de dados SQL
- ✅ Suporte a append e replace

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**: Linguagem principal
- **Pandas**: Manipulação de dados
- **NumPy**: Operações numéricas
- **SQLAlchemy**: ORM para bancos de dados
- **PostgreSQL**: Banco de dados relacional
- **Docker**: Containerização
- **PyYAML**: Configuração
- **Requests**: Integração com APIs

## 📈 Monitoramento e Logs

O sistema gera logs detalhados de todas as operações:

```
2024-XX-XX XX:XX:XX - pipeline - INFO - Starting ETL Pipeline
2024-XX-XX XX:XX:XX - extractor - INFO - Extracted 1000 rows from CSV
2024-XX-XX XX:XX:XX - transformer - INFO - Removed 50 duplicate rows
2024-XX-XX XX:XX:XX - loader - INFO - Successfully loaded 950 rows
2024-XX-XX XX:XX:XX - pipeline - INFO - Pipeline completed in 2.34 seconds
```

## 🧪 Testes

Para executar os módulos individualmente:

```bash
# Testar extrator
python -m src.extract.extractor

# Testar transformador
python -m src.transform.transformer

# Testar loader
python -m src.load.loader
```

## 📚 Documentação Adicional

- **Configuração**: Veja `config/pipeline_config.yaml` para opções de configuração
- **Exemplos**: Execute `src/generate_sample_data.py` para gerar dados de teste
- **Logs**: Verifique o diretório `logs/` para histórico de execuções

## 🤝 Contribuições

Este é um projeto acadêmico para o MVP de Engenharia de Dados da PUC.

## 📄 Licença

Projeto acadêmico - PUC

## 👨‍💻 Autor

Desenvolvido como MVP para a disciplina de Engenharia de Dados - PUC

---

## 🎓 Aspectos Acadêmicos

Este projeto demonstra:

1. **Conceitos de ETL**: Implementação completa de pipeline Extract-Transform-Load
2. **Qualidade de Dados**: Tratamento de duplicatas, valores faltantes e validações
3. **Modularidade**: Código organizado em módulos reutilizáveis
4. **Escalabilidade**: Uso de Docker para facilitar deployment
5. **Boas Práticas**: Logging, tratamento de erros, documentação
6. **Integração**: Suporte a múltiplas fontes e destinos de dados
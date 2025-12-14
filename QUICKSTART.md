# Quick Start Guide - MVP Engenharia de Dados

## 🚀 Início Rápido

### 1. Instalação

```bash
# Clone o repositório
git clone https://github.com/ricferal/mvpPucEngenhariaDados.git
cd mvpPucEngenhariaDados

# Opção A: Usar o script de setup (recomendado)
bash setup.sh

# Opção B: Instalação manual
pip install -r requirements.txt
python src/generate_sample_data.py
```

### 2. Executar o Pipeline

```bash
# Executar o pipeline completo
python src/pipeline.py

# Executar exemplos
python example.py
```

### 3. Com Docker

```bash
# Iniciar todos os serviços
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar serviços
docker-compose down
```

## 📊 Estrutura dos Dados

### Entrada (data/raw/)
- Dados brutos de fontes externas
- Formato: CSV, JSON, APIs

### Saída (data/processed/)
- Dados limpos e transformados
- Formato: CSV, JSON, Parquet

## 🔧 Exemplos de Uso

### Exemplo 1: Pipeline Básico

```python
from src.pipeline import ETLPipeline

pipeline = ETLPipeline()
pipeline.run_pipeline(
    source_path="data/raw/sample_data.csv",
    output_path="data/processed/output.csv"
)
```

### Exemplo 2: Módulos Individuais

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

### Exemplo 3: Com Configuração

```python
from src.pipeline import ETLPipeline

pipeline = ETLPipeline(config_path="config/pipeline_config.yaml")
pipeline.run_pipeline(
    source_path="data/raw/sample_data.csv",
    output_path="data/processed/output.csv"
)
```

## 🎯 Funcionalidades Principais

### Extract (Extração)
- `extract_from_csv()` - Extrair de CSV
- `extract_from_json()` - Extrair de JSON
- `extract_from_api()` - Extrair de API REST

### Transform (Transformação)
- `remove_duplicates()` - Remover duplicatas
- `handle_missing_values()` - Tratar valores faltantes
- `normalize_columns()` - Normalizar dados
- `filter_data()` - Filtrar dados
- `aggregate_data()` - Agregar dados

### Load (Carga)
- `load_to_csv()` - Carregar para CSV
- `load_to_json()` - Carregar para JSON
- `load_to_parquet()` - Carregar para Parquet
- `load_to_database()` - Carregar para banco de dados

## 📈 Fluxo do Pipeline

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Extract   │ ───> │  Transform   │ ───> │    Load     │
└─────────────┘      └──────────────┘      └─────────────┘
     │                      │                      │
     │                      │                      │
  CSV/JSON/API       Clean/Filter/Agg      CSV/JSON/DB
```

## 🔍 Logs e Monitoramento

Os logs são gerados automaticamente:

```
INFO - Starting ETL Pipeline
INFO - Extracted 1050 rows from CSV
INFO - Removed 43 duplicate rows
INFO - Successfully loaded 918 rows
INFO - Pipeline completed in 0.01 seconds
```

## ⚙️ Configuração

Edite `config/pipeline_config.yaml` para customizar:

```yaml
transform:
  remove_duplicates: true
  missing_values:
    strategy: drop  # ou fill, ffill, bfill

load:
  output_format: csv  # ou json, parquet, database
```

## 🐛 Troubleshooting

### Erro: Module not found
```bash
pip install -r requirements.txt
```

### Erro: Sample data not found
```bash
python src/generate_sample_data.py
```

### Erro: Permission denied
```bash
chmod +x setup.sh
```

## 📚 Documentação Completa

Consulte o [README.md](README.md) para documentação detalhada.

## 🤝 Suporte

Para dúvidas ou problemas:
1. Verifique a documentação
2. Execute os exemplos
3. Verifique os logs

---

**MVP Engenharia de Dados - PUC**

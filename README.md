# Análise de Imóveis Rurais com Web Scraping e Machine Learning

## 📋 Descrição do Projeto

Este projeto acadêmico realiza a coleta automatizada de dados de imóveis rurais utilizando técnicas de web scraping, seguida por análise exploratória de dados (EDA) e previsão de preços através de modelos de regressão linear.

## 👨‍🎓 Autor

**Marcos Paulo Roriz Lima Reis**  
RA: 22007534  
Curso: Engenharia da Computação  
Instituição: UniCEUB (Centro Universitário de Brasília)

## 🎯 Objetivos

- Coletar dados de imóveis rurais de forma automatizada
- Realizar análise exploratória dos dados (EDA)
- Desenvolver modelo de regressão linear para predição de preços
- Aplicar boas práticas de ciência de dados e engenharia de software

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal do projeto
- **Playwright**: Automação de navegador para web scraping
- **Pandas**: Manipulação e análise de dados
- **Scikit-learn**: Algoritmos de machine learning (regressão linear)
- **Matplotlib/Seaborn**: Visualização de dados
- **Jupyter Notebook**: Ambiente interativo para análise

## 📁 Estrutura do Projeto

```
TesteLinearRegression/
├── scripts/
│   └── scraper.py              # Script de web scraping com Playwright
├── notebooks/
│   ├── eda.ipynb              # Análise exploratória de dados
│   └── linear_regression.ipynb # Modelo de regressão linear
├── data/
│   ├── raw/                    # Dados brutos coletados
│   └── processed/              # Dados processados
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação
```

## 🚀 Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/LoveDead0289/TesteLinearRegression.git
cd TesteLinearRegression
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
playwright install
```

### 3. Executar Web Scraping

```bash
python scripts/scraper.py
```

### 4. Análise e Modelagem

Abra os notebooks Jupyter para realizar a análise:

```bash
jupyter notebook notebooks/
```

- Execute `eda.ipynb` para análise exploratória
- Execute `linear_regression.ipynb` para treinamento do modelo

## 📊 Metodologia

### 1. Coleta de Dados (Web Scraping)
- Utilização do Playwright para navegar e extrair dados de sites de imóveis
- Coleta de informações como: preço, área, localização, características

### 2. Análise Exploratória (EDA)
- Limpeza e preparação dos dados
- Análise estatística descritiva
- Visualizações para identificar padrões e correlações

### 3. Modelagem (Machine Learning)
- Preparação dos dados para modelagem
- Treinamento de modelo de regressão linear
- Avaliação de métricas (R², RMSE, MAE)
- Análise de resíduos

## 📈 Resultados Esperados

- Dataset estruturado de imóveis rurais
- Insights sobre o mercado imobiliário rural
- Modelo preditivo para estimativa de preços
- Documentação completa do processo

## 📝 Licença

Este projeto é desenvolvido para fins acadêmicos.

## 📧 Contato

Para dúvidas ou sugestões sobre o projeto, entre em contato através do GitHub.

---

**Projeto desenvolvido como parte do curso de Engenharia da Computação - UniCEUB**
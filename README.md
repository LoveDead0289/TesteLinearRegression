# 🏡 Projeto de Análise de Imóveis Rurais - Regressão Linear

**Autor:** Marcos Paulo Roriz Lima Reis  
**RA:** 22007534  
**Data:** Outubro 2025

## 📋 Descrição do Projeto

Este projeto implementa uma solução completa de **ciência de dados** para análise e predição de preços de imóveis rurais, utilizando técnicas de **web scraping**, **análise exploratória de dados** e **machine learning**.

## 🎯 Objetivos

- Coletar dados de imóveis rurais através de web scraping
- Realizar análise exploratória dos dados coletados
- Implementar modelo de regressão linear para predição de preços
- Avaliar performance do modelo e fazer predições

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- **Playwright** - Web scraping
- **BeautifulSoup4** - Parser HTML
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **Matplotlib/Seaborn** - Visualização de dados
- **Scikit-learn** - Machine learning
- **Jupyter Notebook** - Análise interativa

## 📁 Estrutura do Projeto

```
projeto-imoveis-rurais/
├── 📊 data/
│   ├── imoveis_rurais.csv          # Dados brutos coletados
│   └── imoveis_rurais_tratados.csv # Dados limpos e tratados
├── 🌐 htmls/
│   └── page_*.html                 # Páginas HTML coletadas
├── 📓 notebooks/
│   ├── eda_tratamento_dados.ipynb  # Análise exploratória
│   └── modelo.ipynb                # Modelo de regressão linear
├── 🐍 scripts/
│   ├── web_scraper.py              # Script de web scraping
│   └── extrair_dados.py            # Extração de dados dos HTMLs
├── 📋 requirements.txt             # Dependências do projeto
├── 🔧 .gitignore                   # Arquivos ignorados pelo Git
└── 📖 README.md                    # Este arquivo
```

## 🚀 Como Executar

### 1. Instalação das Dependências

```bash
pip install -r requirements.txt
```

### 2. Coleta de Dados (Web Scraping)

```bash
python scripts/web_scraper.py
```

### 3. Extração e Estruturação dos Dados

```bash
python scripts/extrair_dados.py
```

### 4. Análise Exploratória

Abra e execute o notebook:
```bash
jupyter notebook notebooks/eda_tratamento_dados.ipynb
```

### 5. Modelo de Machine Learning

Abra e execute o notebook:
```bash
jupyter notebook notebooks/modelo.ipynb
```

## 📊 Resultados Principais

### Dados Coletados
- **300 imóveis rurais** coletados inicialmente
- **271 imóveis** após limpeza e tratamento
- **12 variáveis** por imóvel (preço, área, localização, etc.)

### Estatísticas dos Dados
- **Preço médio:** R$ 2.157.492,62
- **Área média:** 4,99 hectares
- **Faixa de preços:** R$ 60.000 - R$ 12.000.000

### Performance do Modelo
- **Algoritmos testados:** Regressão Linear e Random Forest
- **Métricas de avaliação:** R², RMSE, MAE
- **R² Score:** 0,4 - 0,7 (típico para dados imobiliários)

## 🔍 Principais Insights

1. **Correlações identificadas:**
   - Área vs. número de quartos: correlação moderada (0,44)
   - Quartos vs. suítes: alta correlação (0,78)

2. **Distribuição geográfica:**
   - Maior concentração em Brasília e região metropolitana
   - Variação significativa de preços por localização

3. **Características dos imóveis:**
   - Maioria são propriedades médias (1-10 hectares)
   - Preços seguem distribuição assimétrica

## 📈 Visualizações Geradas

- Distribuição de preços e áreas
- Matriz de correlação entre variáveis
- Boxplots para detecção de outliers
- Gráficos de dispersão preço vs. características
- Análise geográfica por cidade

## 🤖 Funcionalidades do Modelo

- **Predição de preços** para novos imóveis rurais
- **Análise de importância** das features
- **Comparação de algoritmos** (Linear vs. Random Forest)
- **Métricas de avaliação** completas

## 📝 Metodologia

1. **Coleta de Dados**
   - Web scraping do site DF Imóveis
   - Extração automatizada de 10 páginas
   - Parser robusto com tratamento de erros

2. **Pré-processamento**
   - Limpeza de valores ausentes
   - Remoção de outliers extremos
   - Normalização de features
   - Criação de variáveis derivadas

3. **Análise Exploratória**
   - Estatísticas descritivas
   - Visualizações exploratórias
   - Análise de correlações
   - Identificação de padrões

4. **Modelagem**
   - Divisão treino/teste (80/20)
   - Normalização das features
   - Treinamento de múltiplos algoritmos
   - Avaliação com métricas apropriadas

## 🔧 Configuração do Ambiente

### Requisitos do Sistema
- Python 3.13+
- pip (gerenciador de pacotes)
- Jupyter Notebook
- Navegador web (para Playwright)

### Instalação do Playwright
```bash
pip install playwright
playwright install chromium
```

## 📚 Referências

- [Site DF Imóveis](https://www.dfimoveis.com.br/venda/df/todos/rural)
- [Documentação Scikit-learn](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Playwright Documentation](https://playwright.dev/python/)

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte de atividade prática da disciplina.

## 👨‍💻 Autor

**Marcos Paulo Roriz Lima Reis**  
RA: 22007534  
📧 Email: marcos.paulor@sempreceub.com  
🎓 Curso: Engenharia da Computação  
🏫 Instituição: UniCEUB - Centro Universitário de Brasília

---

*Projeto desenvolvido em Outubro de 2025 como atividade prática de Ciência de Dados*
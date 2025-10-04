# Configurações do Projeto - Imóveis Rurais
# Autor: Marcos Paulo Roriz Lima Reis
# RA: 22007534
# Email: marcos.paulor@sempreceub.com
# Instituição: UniCEUB - Centro Universitário de Brasília

# URLs para scraping
BASE_URL = "https://www.dfimoveis.com.br/venda/df/todos/rural"
PAGES_TO_SCRAPE = 10

# Configurações de dados
DATA_DIR = "data"
HTML_DIR = "htmls"
RAW_DATA_FILE = "imoveis_rurais.csv"
CLEAN_DATA_FILE = "imoveis_rurais_tratados.csv"

# Configurações do modelo
TEST_SIZE = 0.2
RANDOM_STATE = 42

# Configurações de visualização
FIGURE_SIZE = (12, 8)
PLOT_STYLE = "default"

# Thresholds para limpeza de dados
OUTLIER_PERCENTILE = 0.95
MIN_PRICE = 50000
MAX_AREA_HA = 1000
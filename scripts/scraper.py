"""
Web Scraper para Coleta de Dados de Imóveis Rurais

Autor: Marcos Paulo Roriz Lima Reis
RA: 22007534
Curso: Engenharia da Computação - UniCEUB

Este script utiliza Playwright para realizar web scraping de dados
de imóveis rurais, incluindo preço, área, localização e características.
"""

import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from datetime import datetime
import json
import os


class RealEstateScraper:
    """Classe para realizar web scraping de imóveis rurais."""
    
    def __init__(self, output_dir='../data/raw'):
        """
        Inicializa o scraper.
        
        Args:
            output_dir (str): Diretório para salvar os dados coletados
        """
        self.output_dir = output_dir
        self.data = []
        
    async def scrape_property(self, page, url):
        """
        Coleta dados de um imóvel específico.
        
        Args:
            page: Página do Playwright
            url (str): URL do imóvel
            
        Returns:
            dict: Dicionário com dados do imóvel
        """
        try:
            await page.goto(url, wait_until='networkidle', timeout=30000)
            
            # Exemplo de extração de dados (ajustar conforme o site alvo)
            property_data = {
                'url': url,
                'titulo': await self.safe_extract(page, 'h1'),
                'preco': await self.safe_extract(page, '[data-testid="price"]'),
                'area': await self.safe_extract(page, '[data-testid="area"]'),
                'localizacao': await self.safe_extract(page, '[data-testid="location"]'),
                'descricao': await self.safe_extract(page, '[data-testid="description"]'),
                'data_coleta': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            return property_data
        except Exception as e:
            print(f"Erro ao coletar dados de {url}: {str(e)}")
            return None
    
    async def safe_extract(self, page, selector):
        """
        Extrai texto de um elemento de forma segura.
        
        Args:
            page: Página do Playwright
            selector (str): Seletor CSS do elemento
            
        Returns:
            str: Texto extraído ou None
        """
        try:
            element = await page.query_selector(selector)
            if element:
                return await element.inner_text()
        except:
            pass
        return None
    
    async def scrape_listings(self, base_url, max_pages=5):
        """
        Coleta dados de múltiplas páginas de listagens.
        
        Args:
            base_url (str): URL base das listagens
            max_pages (int): Número máximo de páginas a processar
        """
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            
            print(f"Iniciando coleta de dados de imóveis rurais...")
            
            for page_num in range(1, max_pages + 1):
                try:
                    url = f"{base_url}?page={page_num}"
                    print(f"Processando página {page_num}: {url}")
                    
                    await page.goto(url, wait_until='networkidle', timeout=30000)
                    
                    # Aguardar carregamento das listagens
                    await page.wait_for_selector('[data-testid="property-card"]', timeout=10000)
                    
                    # Coletar URLs de imóveis
                    property_links = await page.query_selector_all('[data-testid="property-card"] a')
                    urls = [await link.get_attribute('href') for link in property_links]
                    
                    print(f"Encontrados {len(urls)} imóveis na página {page_num}")
                    
                    # Processar cada imóvel
                    for idx, property_url in enumerate(urls, 1):
                        print(f"  Coletando dados do imóvel {idx}/{len(urls)}...")
                        property_data = await self.scrape_property(page, property_url)
                        if property_data:
                            self.data.append(property_data)
                    
                    # Pequeno delay entre páginas
                    await asyncio.sleep(2)
                    
                except Exception as e:
                    print(f"Erro ao processar página {page_num}: {str(e)}")
                    continue
            
            await browser.close()
            
            print(f"\nColeta finalizada! Total de imóveis coletados: {len(self.data)}")
    
    def save_data(self):
        """Salva os dados coletados em formato CSV e JSON."""
        if not self.data:
            print("Nenhum dado para salvar.")
            return
        
        # Criar diretório se não existir
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Salvar como CSV
        df = pd.DataFrame(self.data)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        csv_path = os.path.join(self.output_dir, f'imoveis_rurais_{timestamp}.csv')
        df.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"Dados salvos em CSV: {csv_path}")
        
        # Salvar como JSON
        json_path = os.path.join(self.output_dir, f'imoveis_rurais_{timestamp}.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        print(f"Dados salvos em JSON: {json_path}")
        
        # Exibir estatísticas básicas
        print(f"\nEstatísticas dos dados coletados:")
        print(f"- Total de registros: {len(df)}")
        print(f"- Colunas: {', '.join(df.columns)}")
        print(f"\nPrimeiras linhas dos dados:")
        print(df.head())


def generate_sample_data():
    """
    Gera dados de exemplo para fins de demonstração.
    
    Returns:
        list: Lista de dicionários com dados de imóveis
    """
    import random
    
    locations = ['Brasília - DF', 'Goiânia - GO', 'Palmas - TO', 'Cuiabá - MT', 'Campo Grande - MS']
    tipos = ['Fazenda', 'Sítio', 'Chácara', 'Terreno Rural', 'Haras']
    
    sample_data = []
    for i in range(50):
        property_data = {
            'url': f'https://exemplo.com/imovel/{i+1}',
            'titulo': f'{random.choice(tipos)} em {random.choice(locations)}',
            'preco': round(random.uniform(300000, 5000000), 2),
            'area': round(random.uniform(5, 500), 2),  # hectares
            'localizacao': random.choice(locations),
            'descricao': f'Excelente propriedade rural com {round(random.uniform(5, 500), 2)} hectares',
            'data_coleta': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        sample_data.append(property_data)
    
    return sample_data


async def main():
    """Função principal para executar o scraper."""
    scraper = RealEstateScraper()
    
    # NOTA: Substitua a URL abaixo pela URL real do site de imóveis
    # Este é apenas um exemplo. Para uso real, você precisa:
    # 1. Identificar o site alvo
    # 2. Ajustar os seletores CSS conforme a estrutura do site
    # 3. Respeitar o robots.txt e termos de uso do site
    
    use_sample_data = True  # Altere para False ao usar dados reais
    
    if use_sample_data:
        print("Gerando dados de exemplo para demonstração...")
        scraper.data = generate_sample_data()
    else:
        # Exemplo de uso real (descomentar e ajustar)
        # base_url = "https://www.exemplo-imoveis.com.br/imoveis-rurais"
        # await scraper.scrape_listings(base_url, max_pages=5)
        print("Para usar dados reais, configure a URL base e os seletores CSS no código.")
        print("Gerando dados de exemplo...")
        scraper.data = generate_sample_data()
    
    # Salvar dados
    scraper.save_data()


if __name__ == "__main__":
    # Executar o scraper
    asyncio.run(main())

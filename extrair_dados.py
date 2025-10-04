from bs4 import BeautifulSoup
import pandas as pd
import re
import os

def extrair_dados_imovel(html_content):
    """
    Extrai dados de imóveis rurais do HTML do site DF Imóveis
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    imoveis = []
    
    # Encontrar todos os cards de imóveis
    cards_imoveis = soup.find_all('a', class_='imovel-card')
    
    for card in cards_imoveis:
        try:
            imovel_data = {}
            
            # URL do imóvel
            imovel_data['url'] = card.get('href', '')
            
            # Localização (título principal)
            titulo_elem = card.find('h2', class_='ellipse-text body-medium accent-color bold')
            imovel_data['localizacao'] = titulo_elem.get_text(strip=True) if titulo_elem else ''
            
            # Tipo e área
            tipo_elem = card.find('h3', class_='ellipse-text body-small accent-color bold mobile-ellipse-view')
            if tipo_elem:
                tipo_text = tipo_elem.get_text(strip=True)
                imovel_data['tipo'] = tipo_text
                # Extrair área em hectares
                area_match = re.search(r'(\d+,?\d*)\s*ha', tipo_text)
                if area_match:
                    area_ha = area_match.group(1).replace(',', '.')
                    imovel_data['area_ha'] = float(area_ha)
                    imovel_data['area_m2'] = float(area_ha) * 10000  # Converter para m²
                else:
                    imovel_data['area_ha'] = None
                    imovel_data['area_m2'] = None
            else:
                imovel_data['tipo'] = ''
                imovel_data['area_ha'] = None
                imovel_data['area_m2'] = None
            
            # Descrição
            desc_elem = card.find('h3', class_='ellipse-text neutral-dark body-small text-uppercase')
            imovel_data['descricao'] = desc_elem.get_text(strip=True) if desc_elem else ''
            
            # Preço
            preco_elem = card.find('div', class_='imovel-price')
            if preco_elem:
                preco_span = preco_elem.find('span', class_='body-large bold')
                if preco_span:
                    preco_text = preco_span.get_text(strip=True)
                    # Remover pontos e converter para float
                    preco_limpo = re.sub(r'[^\d,]', '', preco_text)
                    if preco_limpo:
                        preco_limpo = preco_limpo.replace(',', '.')
                        try:
                            imovel_data['preco'] = float(preco_limpo)
                        except ValueError:
                            imovel_data['preco'] = None
                    else:
                        imovel_data['preco'] = None
                else:
                    imovel_data['preco'] = None
                
                # Valor por m²
                valor_m2_text = preco_elem.get_text()
                valor_m2_match = re.search(r'Valor m² R\$ \s*(\d+)', valor_m2_text)
                if valor_m2_match:
                    imovel_data['valor_m2'] = float(valor_m2_match.group(1))
                else:
                    imovel_data['valor_m2'] = None
            else:
                imovel_data['preco'] = None
                imovel_data['valor_m2'] = None
            
            # Características (quartos, suítes, vagas)
            features_div = card.find('div', class_='imovel-feature')
            imovel_data['quartos'] = 0
            imovel_data['suites'] = 0
            imovel_data['vagas'] = 0
            
            if features_div:
                features = features_div.find_all('div', class_='border-1')
                for feature in features:
                    feature_text = feature.get_text(strip=True)
                    
                    # Quartos
                    quartos_match = re.search(r'(\d+)\s*Quartos?', feature_text)
                    if quartos_match:
                        imovel_data['quartos'] = int(quartos_match.group(1))
                    
                    # Suítes
                    suites_match = re.search(r'(\d+)\s*Suítes?', feature_text)
                    if suites_match:
                        imovel_data['suites'] = int(suites_match.group(1))
                    
                    # Vagas
                    vagas_match = re.search(r'(\d+)\s*Vagas?', feature_text)
                    if vagas_match:
                        imovel_data['vagas'] = int(vagas_match.group(1))
            
            # Anunciante CRECI
            creci_elem = card.find('div', class_='imovel-anunciante')
            if creci_elem:
                creci_p = creci_elem.find('p', class_='label-medium ellipse-text')
                imovel_data['creci'] = creci_p.get_text(strip=True) if creci_p else ''
            else:
                imovel_data['creci'] = ''
            
            # Adicionar à lista se tem dados mínimos
            if imovel_data.get('localizacao') and imovel_data.get('preco'):
                imoveis.append(imovel_data)
                
        except Exception as e:
            print(f"Erro ao processar um imóvel: {e}")
            continue
    
    return imoveis

def processar_todos_htmls():
    """
    Processa todos os arquivos HTML da pasta htmls e cria um DataFrame
    """
    pasta_htmls = 'htmls'
    todos_imoveis = []
    
    if not os.path.exists(pasta_htmls):
        print(f"Pasta '{pasta_htmls}' não encontrada!")
        return None
    
    # Processar cada arquivo HTML
    arquivos_html = [f for f in os.listdir(pasta_htmls) if f.endswith('.html')]
    
    for arquivo in sorted(arquivos_html):
        caminho_arquivo = os.path.join(pasta_htmls, arquivo)
        print(f"Processando {arquivo}...")
        
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                html_content = f.read()
                
            imoveis_pagina = extrair_dados_imovel(html_content)
            todos_imoveis.extend(imoveis_pagina)
            print(f"  -> {len(imoveis_pagina)} imóveis encontrados")
            
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")
    
    # Criar DataFrame
    if todos_imoveis:
        df = pd.DataFrame(todos_imoveis)
        print(f"\nTotal de imóveis coletados: {len(df)}")
        
        # Criar pasta data se não existir
        os.makedirs('data', exist_ok=True)
        
        # Salvar em CSV
        df.to_csv('data/imoveis_rurais.csv', index=False, encoding='utf-8')
        print("Dados salvos em 'data/imoveis_rurais.csv'")
        
        # Mostrar estatísticas básicas
        print("\n=== ESTATÍSTICAS BÁSICAS ===")
        print(f"Preço médio: R$ {df['preco'].mean():,.2f}")
        print(f"Preço mínimo: R$ {df['preco'].min():,.2f}")
        print(f"Preço máximo: R$ {df['preco'].max():,.2f}")
        print(f"Área média: {df['area_ha'].mean():.2f} ha")
        
        return df
    else:
        print("Nenhum imóvel foi encontrado!")
        return None

if __name__ == "__main__":
    print("=== EXTRAÇÃO DE DADOS DOS IMÓVEIS RURAIS ===\n")
    df_imoveis = processar_todos_htmls()
    
    if df_imoveis is not None:
        print("\nPrimeiros 5 imóveis:")
        print(df_imoveis.head())
        
        print("\nColunas disponíveis:")
        print(df_imoveis.columns.tolist())
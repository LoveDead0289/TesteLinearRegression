#!/usr/bin/env python3
"""
Pipeline Principal - Análise de Imóveis Rurais
Autor: Marcos Paulo Roriz Lima Reis
RA: 22007534
Email: marcos.paulor@sempreceub.com
Instituição: UniCEUB - Centro Universitário de Brasília

Este script executa todo o pipeline de análise:
1. Web Scraping
2. Extração de dados
3. Análise básica
"""

import os
import sys
import subprocess
from datetime import datetime

def print_banner():
    """Exibe banner do projeto"""
    print("=" * 60)
    print("🏡 PROJETO ANÁLISE DE IMÓVEIS RURAIS")
    print("=" * 60)
    print(f"Autor: Marcos Paulo Roriz Lima Reis")
    print(f"RA: 22007534")
    print(f"Execução: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 60)

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    print("\n🔍 Verificando dependências...")
    try:
        import pandas
        import playwright
        import bs4  # beautifulsoup4
        print("✅ Todas as dependências estão instaladas!")
        return True
    except ImportError as e:
        print(f"❌ Dependência faltando: {e}")
        print("Execute: pip install -r requirements.txt")
        return False

def run_scraping():
    """Executa o web scraping"""
    print("\n🕸️ Iniciando Web Scraping...")
    try:
        result = subprocess.run([sys.executable, "scripts/web_scraper.py"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Web scraping concluído com sucesso!")
            return True
        else:
            print(f"❌ Erro no web scraping: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Erro ao executar web scraping: {e}")
        return False

def run_data_extraction():
    """Executa a extração de dados"""
    print("\n📊 Extraindo dados dos HTMLs...")
    try:
        result = subprocess.run([sys.executable, "scripts/extrair_dados.py"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Extração de dados concluída!")
            return True
        else:
            print(f"❌ Erro na extração: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Erro ao extrair dados: {e}")
        return False

def show_summary():
    """Exibe resumo dos dados coletados"""
    print("\n📈 Resumo dos dados coletados:")
    try:
        import pandas as pd
        if os.path.exists("data/imoveis_rurais.csv"):
            df = pd.read_csv("data/imoveis_rurais.csv")
            print(f"   • Total de imóveis: {len(df)}")
            print(f"   • Preço médio: R$ {df['preco'].mean():,.2f}")
            print(f"   • Área média: {df['area_ha'].mean():.2f} ha")
            print(f"   • Arquivo salvo: data/imoveis_rurais.csv")
        else:
            print("   ❌ Arquivo de dados não encontrado")
    except Exception as e:
        print(f"   ❌ Erro ao ler dados: {e}")

def main():
    """Função principal"""
    print_banner()
    
    # Verificar dependências
    if not check_dependencies():
        return 1
    
    # Executar web scraping
    if not run_scraping():
        print("\n❌ Pipeline interrompido devido ao erro no web scraping")
        return 1
    
    # Executar extração de dados
    if not run_data_extraction():
        print("\n❌ Pipeline interrompido devido ao erro na extração")
        return 1
    
    # Mostrar resumo
    show_summary()
    
    print("\n🎉 Pipeline executado com sucesso!")
    print("\nPróximos passos:")
    print("1. Execute: jupyter notebook notebooks/eda_tratamento_dados.ipynb")
    print("2. Execute: jupyter notebook notebooks/modelo.ipynb")
    print("\n" + "=" * 60)
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
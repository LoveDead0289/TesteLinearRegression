from playwright.sync_api import sync_playwright
from time import sleep
import os

def get_full_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True para não abrir a janela do navegador
        context = browser.new_context()
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded") 
        html = page.content()    
        context.close()                    
        sleep(3) 
        browser.close()
        
    return html

if __name__ == "__main__":
    # Cria o diretório htmls se não existir
    os.makedirs("htmls", exist_ok=True)
    
    # for de páginas para raspar várias páginas
    for page in range(1, 11):  # exemplo: 10 páginas
        url = f"https://www.dfimoveis.com.br/venda/df/todos/rural?pagina={page}"
        html = get_full_html(url)      
        print(f"Página {page}: {len(html)} caracteres coletados")
        # Salva em arquivo
        with open(f"htmls/page_{page}.html", "w", encoding="utf-8") as f:
            f.write(html)
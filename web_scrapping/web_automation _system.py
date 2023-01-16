from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
import sys;
sys.stdout.reconfigure(encoding='utf-8');

# PARA QUE O SELENIUM FUNCIONE, EH NECESSARIO BAIXAR O DRIVER QUE ESTEJA RELACIONADO A VERSAO DO SEU BROWSER E COLOCA-LO NA PASTA DE INSTALACAO DO PYTHON
# PARA DESCOBRIR LOCALIZACAO DO PYTHON, EXECUTE:
# python -c "import sys; print(sys.executable)"

browser = webdriver.Edge();
                 # .<nome-do-browser>

# CASO QUEIRA EXECUTAR O CODIGO SEM QUE O MESMO ABRA O NAVEGADOR, DESCOMENTE O CODIGO ABAIXO E COMENTE A LINHA 11
# from selenium.webdriver.edge.options import Options;
# edge_options= Options().headless=True;
# browser = webdriver.Edge( options=edge_options );



##=========== OBTENDO AS COTACOES DO DOLAR ======================

browser.get("https://www.google.com/");

# SELECIONANDO CAMPO DE BUSCA
campoBusca = browser.find_element(
                    'xpath', 
                    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
                );

campoBusca.send_keys("cotação dólar");
campoBusca.send_keys(Keys.ENTER);
browser.maximize_window();
browser.implicitly_wait(20);
                                         
cotacao_Dolar_Real = browser.find_element( By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]' );
# divCotacaoReal = browser.find_element( By.CLASS_NAME, 'b_focusTextSmall curr_totxt' );
# divCotacaoReal = browser.find_element('xpath', '//*[@id="cc_tdv"]');#//*[@id="cc_tv"]  #/html/body/div[1]/main/ol/li[1]/div[1]/div[1]/div[2]
print("Cotação do dólar em real: \n ",cotacao_Dolar_Real.text);

browser.back(); 



##=========== OBTENDO AS COTACOES DO EURO ======================

campoBusca = browser.find_element(
                    'xpath', 
                    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
                );
campoBusca.send_keys("cotação euro");
campoBusca.send_keys(Keys.ENTER);
cotacao_Euro_Real = browser.find_element( By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]' );
print("Cotação do Euro em real: \n ",cotacao_Euro_Real.text);




##=========== OBTENDO AS COTACOES DO OURO ======================

browser.get("https://www.melhorcambio.com/ouro-hoje");
cotacao_ouro = browser.find_element('xpath', '//*[@id="comercial"]').get_attribute("value").replace(',','.');
print("Cotação do Ouro: \n ",cotacao_ouro);




import pandas as pd;
table = pd.read_excel("Produtos.xlsx");
 


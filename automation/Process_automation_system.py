# automation process system
import requests;
import json;

# Para conseguir controlar o mouse, teclado e tela do computador, eh necessario instalar a biblioteca abaixo:
import pyautogui as pag;
import pyperclip;
import time;
import pandas as pd;

pag.PAUSE = 1;
# pag.press



pag.hotkey("alt","TAB");
pag.hotkey("ctrl","t");
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pag.hotkey("ctrl","v");
pag.press("enter");


time.sleep(5);
pag.click(x=378, y=281, clicks=3); # ENTRAR NA PASTA DO RELATORIO DE VENDAS

time.sleep(5);
pag.click(x=355, y=357, clicks=1); # SELECIONAR ARQUIVO

pag.click(x=1116, y=191, clicks=1); # CLICANDO NO "3 pontinhos"

time.sleep(1);
pag.click(x=917, y=587, clicks=1); # CLICANDO EM DOWNLOAD



tabela = pd.read_excel(r"C:\Users\Patrick\Downloads\Vendas - Dez.xlsx")

faturamento = tabela["Valor Final"].sum();
quantidade = tabela["Quantidade"].sum();


# ABRINDO O EMAIL
pag.hotkey("alt","TAB");
pag.hotkey("ctrl","t");
pag.write("https://mail.google.com/mail/u/0/#inbox");
pag.press("enter");
time.sleep(7);
pag.click(x=98, y=190, clicks=1); # Clicando em "Escrever"
time.sleep(1);


### DEFININDO DESTINATÁRIO
pyperclip.copy("marcospatrick039474@gmail.com");
pag.hotkey("ctrl","v");
time.sleep(1);
pag.press("tab");

#### ASSUNTO:
pyperclip.copy("Relatório de vendas");
pag.hotkey("ctrl","v");
pag.press("tab");

### CORPO
msg = f'''
    Prezados, bom dia
    O faturamento de ontem foi de: R$ {faturamento:,.2f}
    A quantidade de produtos foi de: {quantidade:,}

    Abs
    Patrick, Marcos, 2023
'''

pyperclip.copy(msg);
pag.hotkey("ctrl","v");
pag.click(771, 692); # Sending email

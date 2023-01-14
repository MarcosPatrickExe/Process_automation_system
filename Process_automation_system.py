# automation process system
import requests;
import json;

# Para conseguir controlar o mouse, teclado e tela do computador, eh necessario instalar a biblioteca abaixo:
import pyautogui as pag;
import pyperclip;
import time;
import pandas as pd;

pag.PAUSE = 1;
pag.press
"""
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
"""


tabela = pd.read_excel(r"C:\Users\Patrick\Downloads\Vendas - Dez.xlsx")

faturamento = tabela["Valor Final"].sum();
quantidade = tabela["Quantidade"].sum();

print("Soma do faturamento: ",faturamento);
print("Soma da quantitade: ",quantidade);

pag.hotkey("alt","TAB");
pag.hotkey("ctrl","t");
pag.write("https://mail.google.com/mail/u/0/#inbox");
pag.press("enter");

time.sleep(5);
pag.click(x=98, y=200, clicks=1);
time.sleep(1);
pag.write("marcospatrick039474@gmail.com");
pag.press("tab");




"""
# print("Terminado.....");
# time.sleep(5);
print(pyautogui.position());


# CALCULAR OS INDICADORES (FATURAMENTO E QUANTIDADE DE PRODUTOS)




response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu");

class Pokemon:
    def __init__(self, dict):
        self.__dict__.update(dict);


def dict2object(response):
    return json.loads(response.text, object_hook=Pokemon);


#for count in response:
#print(response.json() );
obj2 = dict2object(response);
print("obj2: ",obj2);
print(obj2.ability.name , "\n");



obj = json.loads(response.text);
print("Tipo do obj capturado: ", type(obj) );
print(obj['abilities']);
"""

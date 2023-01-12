# automaton process system
import requests;
import json;

# Para conseguir controlar o mouse, teclado e tela do computador, eh necessario instalar a biblioteca abaixo:
import pyautogui
import pyperclip;
import time;


pyautogui.PAUSE = 1;
pyautogui.press

pyautogui.hotkey("alt","TAB");
pyautogui.hotkey("ctrl","t");
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl","v");
pyautogui.press("enter");


time.sleep(5);
pyautogui.click(x=378, y=281, clicks=3); # ENTRAR NA PASTA DO RELATORIO DE VENDAS

time.sleep(5);
pyautogui.click(x=355, y=357, clicks=1); # SELECIONAR ARQUIVO

pyautogui.click(x=1116, y=191, clicks=1); # CLICANDO NO "3 pontinhos"

time.sleep(1);
pyautogui.click(x=917, y=587, clicks=1); # CLICANDO EM DOWNLOAD


# print("Terminado.....");
# time.sleep(5);
print(pyautogui.position());



"""
pyautogui.click();
pyautogui.write();
pyautogui.press();
"""



"""
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
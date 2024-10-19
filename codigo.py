# Entrar no sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Fazer o login no sistema
# Import da base de dados dos produtos
# Cadastrar os produtos
import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 0.3  # delay entre as ações

pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)  # aguardar o site carregar

pyautogui.click(x=770, y=394)  # click no campo de email
pyautogui.write("deboradiorato@admin.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.click(x=798, y=275)

# variavel tabela recebe o csv (ler um arquivo csv)
tabela = pd.read_csv("produtos.csv")
print(tabela)

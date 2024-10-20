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

for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]  # pegar o valor da linha e coluna
    # esqueleto do cadastro de produtos
    # str para escrever o codigo em formato de texto
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):  # se nao tiver uma obs, nao vai escrever
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)

    pyautogui.click(x=798, y=275)

# PASSO 1: ENTRAR NO SISTEMA DA EMPRESA -> https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
# pyautogui -> Automatiza a interação com o mouse e teclado
import time
import pyautogui
import pandas as pd

# pyautogui.write -> Escreve um texto
# pyautogui.click -> Clica em um lugar
# pyautogui.press -> Pressiona uma tecla

pyautogui.PAUSE = 1
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# -------------------------------------


# PASSO 2: FAZER LOGIN NO SISTEMA (email e senha)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# dar uma pausa de 2 segundos
time.sleep(3)

# Clicar na caixa de email
pyautogui.click(x=1874, y=-558)
pyautogui.write("teste@teste.com")
# Clicar na caixa de senha

pyautogui.click(x=1769, y=-418)
pyautogui.write("teste")

# Clicar no botão entrar
pyautogui.click(x=1928, y=-321)

time.sleep(2)


# -------------------------------------
# Passo 3: Importar/abrir a base de dados
# Usar o pandas para abrir o arquivo excel ou csv
# pip install pandas
# automacao\produtos.csv
path_produtos = "automacao/produtos.csv"
tabela = pd.read_csv(path_produtos)
print(tabela)

# -------------------------------------

# Passo 4: Cadastrar um produto
# x=1871, y=-744

linha = 0

# para cada linha da tabela faça:
for linha in tabela.index:
    # clicar no botao de novo cadastro
    pyautogui.click(x=1871, y=-744)
    time.sleep(1)

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # clicar no botao enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# Passo 5: Repetir o processo de cadastro de produto até finalizar a base de dados

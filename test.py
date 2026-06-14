# AUTOMATIC CADASTRATION OF PRODUCTS IN A SITE
# 1º step: open the site in the browser (in this case, we will use Google Chrome)
# 2º step: log in
# 3º step: import the dataset with the products' info
# 4º step: Register the products on the website, one by one
#  (for this, it was helpful to use the "for" loop).

# First we need to install the pyautogui and import it
import pyautogui
import time
pyautogui.PAUSE = 0.8

pyautogui.FAILSAFE = True

# pyautogui.press -> press a keyboard key
# pyautogui.click -> click
# pyautogui.write -> write
# pyautogui.hotkey -> keyboard shortcut ("ctrl", "C")

# to open the enterprise site in Google:
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(4)

pyautogui.click(x=500, y=422) 

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# enter the site and log in
pyautogui.write(site)
pyautogui.press("enter")

time.sleep(4)

pyautogui.click(x=565, y=403)
pyautogui.write("gmailinventado@gmail.com")

pyautogui.press("tab")
pyautogui.write("gmailinventado")
pyautogui.press("tab")
pyautogui.press("enter")

# IMPORT THE DATASET WITH THE PRODUCTS' INFO
import pandas
tabela = pandas.read_csv("produtos.csv.csv")

time.sleep(3)

# REGISTER THE PRODUCTS ON THE WEBSITE, ONE BY ONE

for linha in tabela.index:    # "linha" is a random name, since the "index" command is a list with the indices (lines).

    pyautogui.click(x=540, y=291)

    codigo = tabela.loc[linha, "codigo"]       # tabela.loc[index, column]
    pyautogui.write(str(codigo)) #codigo       #"str" is used to transform a number into a string (text)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)                     #brand
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)                     #type
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))              #category
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))     #unit price
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))           #cost
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])    #must put "str" here because the nan (empty) is text
    if obs != "nan":
        pyautogui.write(obs)                #obs

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)


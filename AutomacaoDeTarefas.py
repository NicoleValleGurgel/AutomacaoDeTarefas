import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

pyautogui.press ("win")
pyautogui.write ("opera")
pyautogui.press ("enter")

link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.click (x=230, y=50)
pyautogui.write (link)
pyautogui.press ("enter")
time.sleep (2)

email = ("emailfalso@gmail.com")
senha = ("senhafalsa")

pyautogui.click (x=538, y=389)
pyautogui.write (email)
pyautogui.press ("tab")

pyautogui.click (x=536, y=486)
pyautogui.write (senha)
pyautogui.press ("enter")

import pandas as pd
tabela = pd.read_csv("produtos.csv")
print (tabela)

for linha in tabela.index:
   
   # codigo do produto
   pyautogui.click (x=595, y=269)
   codigo = tabela.loc[linha, "codigo"]
   pyautogui.write (codigo)
   pyautogui.press ("tab")

   # marca
   marca = tabela.loc[linha, "marca"]
   pyautogui.write (marca)
   pyautogui.press ("tab")

   # tipo
   tipo = tabela.loc[linha, "tipo"]
   pyautogui.write (tipo)
   pyautogui.press ("tab")

   # categoria
   categoria = tabela.loc[linha, "categoria"]
   pyautogui.write (str(categoria))
   pyautogui.press ("tab")

   # preco unitario
   preco_unitario = tabela.loc[linha, "preco_unitario"]
   pyautogui.write (str(preco_unitario))
   pyautogui.press ("tab")

   # custo
   custo = tabela.loc[linha, "custo"]
   pyautogui.write (str(custo))
   pyautogui.press ("tab")

   # obs
   obs = tabela.loc[linha, "obs"]
   if not pd.isna (obs):
      pyautogui.write (obs)
   pyautogui.press ("tab")
   
   pyautogui.click (x=594, y=576)
   pyautogui.scroll (5000)

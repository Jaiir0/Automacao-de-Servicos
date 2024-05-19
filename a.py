import pyautogui
import time 

#Delay para cada ação
pyautogui.PAUSE = 0.8

#abre o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#entra no site da empresa
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#tempo de delay para carregar a pagina do google
time.sleep(5)

#faz o login
pyautogui.press('tab')
pyautogui.write('pythonteste.gmail.com')
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('tab')
pyautogui.press('enter')
                                                                                                                                                             
import pandas as pd
tabela =pd.read_csv('produtos.csv')
print (tabela)

#cadastro dos produtos
for linha in tabela.index:
    pyautogui.press('tab')
    code = tabela.loc[linha,'codigo']
    pyautogui.write(code)
    pyautogui.press('tab')
    code = tabela.loc[linha,'marca']
    pyautogui.write(code)
    pyautogui.press('tab')
    code = tabela.loc[linha,'tipo']
    pyautogui.write(code)
    pyautogui.press('tab')
    code = str (tabela.loc[linha,'categoria'])
    pyautogui.write(code)
    pyautogui.press('tab')
    code = str (tabela.loc[linha,'preco_unitario'])
    pyautogui.write(code)
    pyautogui.press('tab')
    code = str (tabela.loc[linha,'custo'])
    pyautogui.write(code)
    pyautogui.press('tab')
    code = str (tabela.loc[linha,'obs']).lower()
    if code == 'nan':
        pyautogui.press('tab')
    else:
        pyautogui.write(code)
        pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.click(x=150,y=280)
    pyautogui.scroll(5000)


    



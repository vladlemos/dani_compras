# coding UTF-8

from selenium import webdriver
from credenciais import USR, PWD
from selenium.webdriver.support.ui import Select
import time


from bs4 import BeautifulSoup

usr = USR
pwd = PWD

import sqlite3
connection = sqlite3.connect('dani_dados_requisicoes.db')
cursor = connection.cursor()

# abrir a página do sistema
driver = webdriver.Chrome()
driver.get('http://sistemas.usp.br')

time.sleep(3)

# fase de logar no sistema Parte Login:
username_box = driver.find_element_by_id('loginUsuario')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('senhaUsuario')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('botaoLogin')
login_btn.click()

time.sleep(3)

driver.get('https://uspdigital.usp.br/mercurioweb/buscarRequisicoesCompra?codmnu=265')


# formulário de pesquisa datas - Todo - fazer uma função

'''
Aqui estou pensando em fazer uma função ela deve receber o período inicial apenas
o período final será a data da pesquisa
deverá fazer um loop cortando dados em intervalo de 15 ou 30 dias da data inicial até hoje
'''

dia_inicio = driver.find_element_by_name('dta_dia')
mes_inicio = driver.find_element_by_name('dta_mes')
ano_inicio = driver.find_element_by_name('dta_ano')

periodo_inicial = ['01','01','2019']

dia_inicio.send_keys(periodo_inicial[0])
mes_inicio.send_keys(periodo_inicial[1])
ano_inicio.send_keys(periodo_inicial[2])


dia_final = driver.find_element_by_name('dta_diafim')
mes_final = driver.find_element_by_name('dta_mesfim')
ano_final = driver.find_element_by_name('dta_anofim')

periodo_final = ['30','01','2019']

dia_final.send_keys(periodo_final[0])
mes_final.send_keys(periodo_final[1])
ano_final.send_keys(periodo_final[2])

situacao = Select(driver.find_element_by_name('stareqcpr'))
situacao.select_by_value('Para compras')

time.sleep(2)
ano_final.submit()


# relação de contratos no periodo

tabela = driver.find_element_by_xpath("//*[@id='layout_conteudo']/form/table/tbody/tr[3]/td/table")
resultado = tabela.get_attribute("outerHTML")

soup = BeautifulSoup(resultado, 'html.parser')

soup2 = soup.find_all('a', attrs={'class':'menu_home'})


print(soup2)

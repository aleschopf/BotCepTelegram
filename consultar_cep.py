from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import json


def formatar_cep(cep:str)->str:
    cep_formatado = ''.join(re.findall('[0-9]+', cep))
    if cep_formatado.__len__() == 8:
        return cep_formatado
    else:
        return None


def formatar_resultado(resultado:str)->str:
    resultado_dict = json.loads(resultado)
    try:
        erro = resultado_dict['erro']
        resultado_formatado = 'CEP não localizado no banco de dados'
        return resultado_formatado
    except:
        cep = resultado_dict['cep']
        logradouro = resultado_dict['logradouro']
        complemento = resultado_dict['complemento']
        bairro = resultado_dict['bairro']
        municipio = resultado_dict['localidade']
        uf = resultado_dict['uf']
        
        if complemento == '':
            resultado_formatado = f'CEP: {cep}\nLogradouro: {logradouro}\nBairro: {bairro}\nMunicípio: {municipio} - {uf}'
            return resultado_formatado
        else:
            resultado_formatado = f'CEP: {cep}\nLogradouro: {logradouro}, {complemento}\nBairro: {bairro}\nMunicípio: {municipio} - {uf}'
            return resultado_formatado
        

def consultar_cep(cep:str)->str:
    cep = formatar_cep(cep)
    if cep:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=options)
        driver.get(f'https://viacep.com.br/ws/{cep}/json/')
        resultado = driver.find_element(By.XPATH, '/html/body/pre').text
        resultado = formatar_resultado(resultado)
        return resultado
    else:
        resultado = 'Informe um CEP válido'
        return resultado

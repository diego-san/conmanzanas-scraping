from bs4 import BeautifulSoup
import requests
import json
import time
import os.path
data = {}
dataa = {}
dataaa = {}
dataaaa = {}
dato = {}
dat= {}
data['super'] = []
dataa['restaurant'] = []
dataaa['ropa'] = []
dataaaa['servicios'] = []
dato['salario'] = []
dat['ocio'] = []
url = 'https://preciosmundi.com/chile/precios-supermercado'
url2 = 'https://preciosmundi.com/chile/precio-restaurantes'
url3 ='https://preciosmundi.com/chile/precio-ropa-calzado'
url4 ='https://preciosmundi.com/chile/precio-transporte-servicios'
url5 ='https://preciosmundi.com/chile/precio-vivienda-salarios'
url6 ='https://preciosmundi.com/chile/precio-ocio-deportes'
r = requests.get(url)
r2 = requests.get(url2)
r3 = requests.get(url3)
r4 = requests.get(url4)
r5 = requests.get(url5)
r6 = requests.get(url6)
soup= BeautifulSoup(r.content)
soup2= BeautifulSoup(r2.content)
soup3= BeautifulSoup(r3.content)
soup4= BeautifulSoup(r4.content)
soup5= BeautifulSoup(r5.content)
soup6= BeautifulSoup(r6.content)

for x in range(0,18):
    
    descripcionsuper= soup.find_all('td',class_='product-name')[x]
    preciosuper=soup.find_all('td',class_='price')[x]
    data['super'].append({
             
             'pagina': soup.title.string,
             'nombre': descripcionsuper.string,
             'precio Peso Chileno':preciosuper.text,
             'url': url,
             'fechaScrapy': time.strftime("%m-%d-%Y-%H-%M-%S"),
            
    })

pass
for xa in range(0,8):
    descripcionr= soup2.find_all('td',class_='product-name')[xa]
    preciosr=soup2.find_all('td',class_='price')[xa]
    dataa['restaurant'].append({
             'pagina': soup2.title.string,
             'nombre': descripcionr.string,
             'precio Peso Chileno':preciosr.text,
             'url': url2,
             'fechaScrapy': time.strftime("%m-%d-%Y-%H-%M-%S"),
    })
pass
for xb in range(0,4):
    descripcionropa= soup3.find_all('td',class_='product-name')[xb]
    precioropa=soup3.find_all('td',class_='price')[xb]
    dataaa['ropa'].append({
             'pagina': soup3.title.string,
             'nombre': descripcionropa.string,
             'precio Peso Chileno':precioropa.text,
             'url': url3,
             'fechaScrapy': time.strftime("%m-%d-%Y-%H-%M-%S"),
    })
pass
for xc in range(0,10):
    descripcionser= soup4.find_all('td',class_='product-name')[xc]
    precioser=soup4.find_all('td',class_='price')[xc]
    dataaaa['servicios'].append({
             'pagina': soup4.title.string,
             'nombre': descripcionsuper.string,
             'precio Peso Chileno':preciosuper.text,
             'url': url4,
             'fechaScrapy': time.strftime("%m-%d-%Y-%H-%M-%S"),
    })
pass
for xd in range(0,8):  
    descripcionsa= soup5.find_all('td',class_='product-name')[xd]
    preciosa=soup5.find_all('td',class_='price')[xd]
    dato['salario'].append({
             'pagina': soup5.title.string,
             'nombre': descripcionsa.string,
             'precio Peso Chileno':preciosa.text,
             'url': url5,
             'fechaScrapy': time.strftime("%m-%d-%Y-%H-%M-%S"),
    })
pass
for xe in range(0,8):
    descripciono= soup6.find_all('td',class_='product-name')[xe]
    precioo=soup6.find_all('td',class_='price')[xe]
    dat['ocio'].append({
             'pagina': soup6.title.string,
             'nombre': descripciono.string,
             'precio Peso Chileno':precioo.text,
             'url': url6,
             'fechaScrapy': time.strftime("%m-%d-%Y-%H-%M-%S"),
    })
pass    

dir = os.path.dirname(os.path.abspath(__file__)) + '/data'

file_name ='archivo__'+time.strftime("%m-%d-%Y-%H-%M-%S")+'.json'

with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        json.dump(dataa, file, indent=4, ensure_ascii=False)
        json.dump(dataaa, file, indent=4, ensure_ascii=False)
        json.dump(dataaaa, file, indent=4, ensure_ascii=False)
        json.dump(dato, file, indent=4, ensure_ascii=False)
        json.dump(dat, file, indent=4, ensure_ascii=False)
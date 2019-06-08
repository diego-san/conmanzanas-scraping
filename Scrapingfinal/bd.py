import requests
import json
import sqlite3


d= requests.get('https://preciosmundi.com/chile/precios-supermercado')
dato=json.loads(d.content)

 
sql = sqlite3.connect('bdCM.db')
cur = sql.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS bdCM
            (pag text, nombre text)''')
 

for row in dato['Super']:
    cur.execute("INSERT INTO bdtarea VALUES (?, ?)", (row['pagina'], row['NombreEmpresa']))
print('-------------------------------------------')
print('base de datos creada con exito!')
print('-------------------------------------------')
for row in cur.execute('SELECT * FROM bdtarea'):
    print(row)
sql.commit()
sql.close()

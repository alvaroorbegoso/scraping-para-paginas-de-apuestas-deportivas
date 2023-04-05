import requests
from bs4 import BeautifulSoup
import json

# URL de la página de resultados de partidos
url = 'https://example.com/resultados'

# Hacer una solicitud GET a la página web
response = requests.get(url)

# Crear objeto BeautifulSoup a partir del contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todas las tablas en la página web
tables = soup.find_all('table')

# Crear una lista para almacenar los resultados
results = []

# Iterar sobre cada tabla y extraer los datos
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        results.append(cols)

# Crear un objeto JSON para almacenar los resultados
output = {'results': results}

# Guardar los resultados en un archivo JSON
with open('output.json', 'w') as f:
    json.dump(output, f)

print('Los datos se han extraído con éxito y se han guardado en output.json')

import json
import base64
import os

# Tu JSON original
data = {
    "1": "xxxx",
    "2": "xxxx",
    "3": "xxxx",
    "4": "xxxx"
}

print(f"Cadena Base64 escrita en {data}")

# Convertir el diccionario a una cadena JSON
json_string = json.dumps(data)

# Codificar la cadena JSON en Base64
base64_bytes = base64.b64encode(json_string.encode('utf-8'))
base64_string = base64_bytes.decode('utf-8')

# Crear el directorio resources si no existe
output_dir = "static"
os.makedirs(output_dir, exist_ok=True)

# Escribir la cadena Base64 en el archivo resources/resources.json
output_path = os.path.join(output_dir, "base.txt")
with open(output_path, "w") as file:
    file.write(base64_string)

print(f"Cadena Base64 escrita en {output_path}")

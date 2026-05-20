def read_sales(filename):
    """
    Lee un archivo con ventas en formato "producto:valor;producto:valor;..."
    (todo en una sola línea, los registros separados por ';') y agrupa los
    valores en una lista por producto.

    Reglas:
    - Los valores se convierten a float.
    - El orden de los montos dentro de la lista es el mismo en que aparecen
      en el archivo.
    - Los separadores ';' finales sin contenido se ignoran (es común que
      el archivo termine con ';').
    - Si el archivo no existe, propagar FileNotFoundError.
    """
    diccionario = {}
    with open(filename, "r") as archivo:
        # Separamos la línea completa por los puntos y comas
        lista = archivo.read().split(";")
        
        for i in lista:
            # Quitamos espacios y saltos de línea invisibles
            elemento_limpio = i.strip()
            
            # Si el fragmento no está vacío, lo procesamos
            if len(elemento_limpio) > 0:
                # SEPARAMOS POR LOS DOS PUNTOS (:)
                variable = elemento_limpio.split(":")
                
                # Guardamos limpiando con .strip() a ambos lados
                producto = variable[0].strip()
                valor = float(variable[1].strip())
                
                # Acumulamos en el diccionario
                if producto in diccionario:
                    diccionario[producto].append(valor)
                else:
                    diccionario[producto] = [valor]
                    
    return diccionario


def process_sales(data):
    """
    Para cada producto del diccionario, imprime en el orden natural del dict:

        producto: ventas totales $X.XX, promedio $Y.YY

    Los valores de total y promedio deben mostrarse siempre con DOS
    decimales.
    """
    for producto, valor in data.items():
        total = sum(valor)
        promedio = total / len(valor)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

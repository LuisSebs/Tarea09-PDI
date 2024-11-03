import os
import argparse
import webbrowser
from PIL import Image
from utils.colores import random_color, verde, reset, rojo
from utils.progress_bar import progress_bar
from cartas import *

HTML = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tarea09-PDI</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: "JetBrains Mono", monospace;
                    font-optical-sizing: auto;
                    font-weight: 500;
                    font-style: normal;
                }
            </style>
        </head>
        <body>
            {body_content}
        </body>
        </html>
    """

def letras_color(imagen,letra):
    body = ''
    total_pixeles = imagen.width * imagen.height
    pixeles_procesados = 0
    color = random_color()
    for y in range(imagen.height):
        for x in range(imagen.width):
            pixel = imagen.getpixel((x,y))
            span = "<span style='color: rgb({}, {}, {});'>{}</span>".format(*pixel, letra)
            body += span
            # Actualizar la barra de progreso
            pixeles_procesados += 1
            if pixeles_procesados % (total_pixeles // 100) == 0:
                progress_bar(pixeles_procesados, total_pixeles, color)
        # Salto de linea
        body += '<br>\n'

    print(verde+f"Imagen con letras creada ʕ•ᴥ•ʔ"+reset)

    # Agregamos el cuerpo al documento
    return HTML.replace("{body_content}", body)

def letras_tonos_gris(imagen,letra):
    imagen_tonos_gris = imagen.convert('L')
    body = ''
    total_pixeles = imagen.width * imagen.height
    pixeles_procesados = 0
    color = random_color()
    for y in range(imagen.height):
        for x in range(imagen.width):
            pixel = imagen_tonos_gris.getpixel((x,y))
            span = "<span style='color: rgb({}, {}, {});'>{}</span>".format(pixel,pixel,pixel, letra)
            body += span
            # Actualizar la barra de progreso
            pixeles_procesados += 1
            if pixeles_procesados % (total_pixeles // 100) == 0:
                progress_bar(pixeles_procesados, total_pixeles, color)
        # Salto de linea
        body += '<br>\n'

    print(verde+f"Imagen con letras creada ʕ•ᴥ•ʔ"+reset)

    # Agregamos el cuerpo al documento
    return HTML.replace("{body_content}", body)

def letras_simbolos(imagen):
    # simbolos = ['M','N','H','#','Q','U','A','D','O','Y','2','$','%','+','.', ' ']
    simbolos = ['@', '#', 'M', 'W', 'H', '8', '&', '%', 'B', 'Q', 'O', 'D', 'U', 'Y', '2', '$', '+', '~', '-', ':', '.', ' ']
    imagen_tonos_gris = imagen.convert('L')
    body = ''
    total_pixeles = imagen.width * imagen.height
    pixeles_procesados = 0
    color = random_color()
    for y in range(imagen.height):
        for x in range(imagen.width):
            pixel = imagen_tonos_gris.getpixel((x,y))
            i = pixel // 16
            simbolo = simbolos[i]
            span = "<span>{}</span>".format(simbolo)
            body += span
            # Actualizar la barra de progreso
            pixeles_procesados += 1
            if pixeles_procesados % (total_pixeles // 100) == 0:
                progress_bar(pixeles_procesados, total_pixeles, color)
        # Salto de linea
        body += '<br>\n'

    print(verde+f"Imagen con letras creada ʕ•ᴥ•ʔ"+reset)

    # Agregamos el cuerpo al documento
    return HTML.replace("{body_content}", body)

def letras_simbolos_color(imagen):
    # simbolos = ['M','N','H','#','Q','U','A','D','O','Y','2','$','%','+','.', ' ']
    simbolos = ['@', '#', 'M', 'W', 'H', '8', '&', '%', 'B', 'Q', 'O', 'D', 'U', 'Y', '2', '$', '+', '~', '-', ':', '.', ' ']
    imagen_tonos_gris = imagen.convert('L')
    body = ''
    total_pixeles = imagen.width * imagen.height
    pixeles_procesados = 0
    color = random_color()
    for y in range(imagen.height):
        for x in range(imagen.width):
            pixel_color = imagen.getpixel((x,y))
            pixel_gris = imagen_tonos_gris.getpixel((x,y))
            i = pixel_gris // 16
            simbolo = simbolos[i]
            span = "<span style='color: rgb({}, {}, {});'>{}</span>".format(*pixel_color, simbolo)
            body += span
            # Actualizar la barra de progreso
            pixeles_procesados += 1
            if pixeles_procesados % (total_pixeles // 100) == 0:
                progress_bar(pixeles_procesados, total_pixeles, color)
        # Salto de linea
        body += '<br>\n'

    print(verde+f"Imagen con letras creada ʕ•ᴥ•ʔ"+reset)

    # Agregamos el cuerpo al documento
    return HTML.replace("{body_content}", body)

def letras_frase(imagen,frase):
    frase_lista = list(frase)
    body = ''
    total_pixeles = imagen.width * imagen.height
    pixeles_procesados = 0
    color = random_color()
    for y in range(imagen.height):
        for x in range(imagen.width):
            if not frase_lista:
                frase_lista = list(frase)
            letra = frase_lista.pop(0)
            pixel = imagen.getpixel((x,y))
            span = "<span style='color: rgb({}, {}, {});'>{}</span>".format(*pixel, letra)
            body += span
            # Actualizar la barra de progreso
            pixeles_procesados += 1
            if pixeles_procesados % (total_pixeles // 100) == 0:
                progress_bar(pixeles_procesados, total_pixeles, color)
        # Salto de linea
        body += '<br>\n'

    print(verde+f"Imagen con letras creada ʕ•ᴥ•ʔ"+reset)

    # Agregamos el cuerpo al documento
    return HTML.replace("{body_content}", body)

def poker(imagen: Image):
    tonos = ['🂡','🂢','🂣','🂤','🂥','🂦','🂧','🂨','🂩','🂪','🂫']
    body = ''
    total_pixeles = imagen.width * imagen.height
    pixeles_procesados = 0
    color = random_color()
    imagen_tonos_gris = imagen.convert('L')

    # Divisor para mapear los tonos de gris a las cartas
    divisor = 256 // len(tonos)

    for y in range(imagen.height):
        for x in range(imagen.width):
            pixel = imagen_tonos_gris.getpixel((x, y))
            i = pixel // divisor
            if i >= len(tonos):  # Asegúrate de que el índice no se pase de la lista
                i = len(tonos) - 1
            carta = tonos[i]
            body += f'<span>{carta}</span>'
            # Actualizar la barra de progreso
            pixeles_procesados += 1
            if pixeles_procesados % (total_pixeles // 100) == 0:
                progress_bar(pixeles_procesados, total_pixeles, color)
        # Salto de línea
        body += '<br>\n'

    print(verde + "Imagen con letras creada ʕ•ᴥ•ʔ" + reset)

    # Agregamos el cuerpo al documento
    return HTML.replace("{body_content}", body)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programa que crea imagenes con letras")

    info_algoritmos = """
        
    c: Letras a color
    g: Tonos de gris
    s: Simbolos
    sc: Simbolos a color
    f: Frase
    p: Poker

    """

    # Argumentos no opcionales    
    parser.add_argument("imagen", help="Ruta de la imagen de entrada")
    parser.add_argument("salida", help="Ruta de salida con extension html")
    parser.add_argument("algoritmo", help=info_algoritmos)
    # Argumentos opcionales
    parser.add_argument("--c", type=str, default="M", help="Cadena/Letra")
    
    # Obtenemos los argumentos
    args = parser.parse_args()

    # Cargamos la imagen
    imagen = None
    try:
        imagen = Image.open(args.imagen)
    except Exception as e:
        print(rojo+f"Error al cargar la imagen: {e}"+reset)
        exit()
    
    # Dithering a aplicar
    algoritmo = args.algoritmo
    resultado = None
    if algoritmo == "c":
        resultado = letras_color(imagen, args.c)
    elif algoritmo == "g":
        resultado = letras_tonos_gris(imagen, args.c)
    elif algoritmo == "s":
        resultado = letras_simbolos(imagen)
    elif algoritmo == "sc":
        resultado = letras_simbolos_color(imagen)
    elif algoritmo == "f":
        resultado = letras_frase(imagen, args.c)
    elif algoritmo == "p":
        resultado = poker(imagen)
    else:
        print(rojo+f"Algoritmo invalido: {algoritmo} \n Algoritmos validos: {info_algoritmos}"+reset)
        exit()
    
    # Creamos el documento HTML
    with open(args.salida, 'w', encoding='utf-8') as file:
        file.write(resultado)

    # Convertimos la ruta de salida a una ruta absoluta
    ruta_absoluta = os.path.abspath(args.salida)

    # Abrimos el documento
    webbrowser.open(f'file://{ruta_absoluta}')




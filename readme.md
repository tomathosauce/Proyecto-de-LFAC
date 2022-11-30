# Proyecto final de lenguajes formales, autómatas y compiladores

Esto es un programa (analizador léxico + analizador sintáctico) que reconoce el lenguaje de programación *Jay Plus Plus*.

## ¿Cómo correr el programa?

Si es el archivo `.py` escribir (sin los signos de mayor que e igual que)

`python <direccion>`

Si es el ejecutable 

`jaypp.exe <direccion>`

Si la direccion contiene espacios, encerrarla con doble comillas (`"<direccion>"`)

### Argumentos obligatorios

- direccion: dirección del archivo

### Argumentos opcionales

- `--cwd` : esto permite utilizar la dirección relativa del archivo
- `--debug` : activa el modo debug del parser
- `--tokens` : muestra los tokens leídos

## ¿Cómo compilar el programa?

Con el comando

`pyinstaller main.py --onefile --paths=./.venv/Lib/site-packages --name=jaypp`

Se genera el ejecutable en la carpeta `./dist/`

## Características
- Sentencias de control IF y WHILE
- Expresiones especiales de notación polaca reversa
- Declaraciones, asignaciones
- Funciones LEER e IMPRIMIR disponibles

## Links utiles
* **https://ply.readthedocs.io/en/latest/ply.html#error-handling**
* https://www.geeksforgeeks.org/ply-python-lex-yacc-an-introduction/
* https://www.skenz.it/compilers/ply
* https://riptutorial.com/python/example/31583/the--hello--world---of-ply---a-simple-calculator
* https://my.eng.utah.edu/~cs3100/lectures/l14/ply-3.4/doc/ply.html
* https://www.dabeaz.com/ply/ply.html
* https://dev.to/taw/episode-18-ply-python-lex-yacc-11bl

## Recomendaciones
* Utilizar un ambiente virtual de python
    * Crear el ambiente virtual
        * ```python -m venv .venv```
    * Activar el ambiente
        * ```./.venv/scripts/activate```
    * Instalar PLY (Python-Lex-Yacc)
        * ```pip install ply```
    * Instalar todas las dependencias
        * ```pip install -r requirements.txt```
    * Salir del ambiente virtual
        * ```exit```
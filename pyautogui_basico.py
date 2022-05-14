import pyautogui


# Obtener la posicion del mouse
a = pyautogui.position()
print(a)


# Mover el mouse 
pyautogui.moveTo(300, 200)
# Mover en 3 segundos 
pyautogui.moveTo(50, 992, 1)


# Mover a posicion determinando con movimiento

# linear (valor por defecto)
# easeInBack
# easeInBounce
# easeInCirc (natural)
# easeInCubic
# easeInExpo
# easeInOutBack
pyautogui.moveTo(1496, 992, 1, pyautogui.easeInCirc)


# Mover de forma relativa a la posicion del mouse
pyautogui.moveRel(-1000, -600, 1)


# hacer clicks
pyautogui.click()
pyautogui.doubleClick()
pyautogui.tripleClick()
# Click en posicion
pyautogui.click(0, 0)


# Especificar boton

# middle  (medio)
# left    (izquierdo)
# right   (derecho)
pyautogui.click(button="right")


# Arrastrar y soltar
pyautogui.dragTo(500, 400, duration= 1)
# Arrastrar en posicion relativa
pyautogui.dragRel(100, 50, duration= 1)


# Hacer scroll con el mouse
pyautogui.scroll(400)


# Precionar y soltar una tecla
pyautogui.press("a")
pyautogui.press("enter")
# Combinar teclas
pyautogui.hotkey("ctrl", "s")
# Ver teclas disponibles
a = pyautogui.KEYBOARD_KEYS


# Produce escribir un texto
pyautogui.typewrite("Recursos Python")
# "\n" provoca la presión de la tecla Enter.
# interval indica en segundos el intervalo entre una tecla y otra.
pyautogui.typewrite("Recursos\nPython", interval=0.2)


# Desplegar un mensaje.
pyautogui.alert("¡Hola, mundo!", "Desde PyAutoGUI")
# cambiar mensaje del boton
pyautogui.alert("¡Hola, mundo!", "Desde PyAutoGUI", button="Aceptar")


#----------------------------------------------------------------
# Si queremos que el mensaje muestre varias opciones hacemos uso de confirm():

# Botones.
CERRAR = "Sí, cerrar"
GUARDAR = "Guardar todo y cerrar"
NOGUARDAR = "No, seguir trabajando"
# Crear el mensaje.
opt = pyautogui.confirm(
    # Mensaje en pantalla
    "¿Desea cerrar el programa?", 
    # Titulo de la Ventana
    "Confirmación",
    [CERRAR, GUARDAR, NOGUARDAR]
)
# Tomar decisión en base al botón presionado.
if opt == CERRAR:
    pass
elif opt == GUARDAR:
    pass
elif opt == NOGUARDAR:
    pass
#------------------------------------------------------------------

# Para solicitar que el usuario ingrese un texto el módulo provee la función prompt.
# La función retorna None si se cerró la ventana o presionó "Cancel".
user = pyautogui.prompt("Mensaje", "Titulo ventana")


# Es posible indicar un valor por defecto y un tiempo límite en milisegundos, 
# de modo que una vez transcurrido se cerrará el diálogo automáticamente.
# Valor por defecto "usuario1" y cerrar a los 5 segundos.
# Si se cierra automaticamente retorna Timeout
user = pyautogui.prompt("Mensaje", "Titulo Ventana", default="usuario1", timeout=5000)


# Capturar imagen de la pantalla
screenshot = pyautogui.screenshot()
# Capturar una porción de la pantalla
# region es una tupla con la estructura (X, Y, Ancho, Alto).
screenshot = pyautogui.screenshot(region=(50, 50, 400, 300))


# Para saber si un píxel equivale a cierto color, puedes usar
# Funciona con la estructura (x, y, (R, G, B,)) 
pyautogui.pixelMatchesColor(500, 400, (225, 228, 229))
# Obtener el color de un píxel como una tupla (R, G, B)
screenshot.getpixel((500, 400))


# si Si bien este código es similar a 
# screenshot.getpixel((500, 400)) == (225, 228, 229), 
# tiene un ingrediente extra llamado tolerance que indica 
# cuánto puede variar el color para que la búsqueda sea menos restrictiva.

# El color no coincide exactamente pero es cercano.
pyautogui.pixelMatchesColor(500, 400, (220, 230, 232), tolerance=10)

#--------------------------------------------------------------------------
# Ubicar una imagen dentro de la pantalla
# Retorna una tupla del tipo (X, Y, Ancho, Alto).
pyautogui.locateOnScreen("imagen.png")


# La función también acepta imagenes abiertas por Pillow
from PIL import Image
image = Image.open("imagen.png")
pyautogui.locateOnScreen(image)
# Retorna una tupla del tipo (X, Y, Ancho, Alto).


# Si la imagena aprece varias veces en la pantalla, 
# locateAllOnScreen() retorna un iterador con todas las coincidencias
list(pyautogui.locateAllOnScreen("imagen2.png"))
# Retorna [(1060, 629, 17, 20), (1177, 629, 17, 20)]
# (X, Y, Ancho, Alto).


# Ubicar una imagen dentro de una región de la pantalla
pyautogui.locateOnScreen("imagen.png", region=(0, 0, 1100, 300))
# Retorna (759, 44, 96, 48) que es (X, Y, Ancho, Alto).
# Especificar una región aumenta 
# considerablemente el tiempo de procesamiento de la función.


# Ubicar una imagen teniendo en cuenta únicamente la escala de grises
# También aplicable a locateAllOnScreen().
pyautogui.locateOnScreen("imagen.png", grayscale=True)
# Retorna (759, 44, 96, 48) que es (X, Y, Ancho, Alto).
grayscale=True # aumenta la velocidad de la función en alrededor de 30%.


# Obtener el tamaño de la pantalla
pyautogui.size()
# Determinar si un par de coordenadas están dentro de los límites
pyautogui.onScreen(100, 500)
# Retorna True o False



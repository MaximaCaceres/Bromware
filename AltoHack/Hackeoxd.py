import pyautogui
import time
import random # Agregamos esto para variar el mensaje

# --- CONFIGURACIÓN DE SEGURIDAD (MUY IMPORTANTE) ---
# Si necesitas detener esto rápidamente, mueve el ratón a una de las cuatro esquinas de la pantalla.
# Puedes desactivar esto, ¡pero NO lo recomiendo!
# pyautogui.FAILSAFE = False 

# Reducimos el tiempo de espera a lo mínimo.
SHORT_DELAY = 0.05 
# Aumentamos el número de iteraciones.
NUM_ITERATIONS = 50 

# Lista de mensajes variados para que no escriba lo mismo siempre
mensajes = [
    "TE HAN HACKEADO XD",
    "EL SISTEMA ESTA COMPROMETIDO",
    "PONTE A TRABAJAR!",
    "PYTHON RULES!",
    "PUTO EL QUE LEE" # Tu mensaje original
]

print(f"Iniciando ciclo de apertura y escritura: {NUM_ITERATIONS} veces.")

# 1. CICLO DE APERTURA Y ESCRITURA
for i in range(NUM_ITERATIONS):
    # 1. Usamos 'start' para ejecutar el programa (más directo que Win+R en algunos casos)
    pyautogui.hotkey('win', 'r') 
    time.sleep(SHORT_DELAY) 
    
    # 2. Escribe el comando para abrir el Bloc de Notas
    pyautogui.write('notepad')
    time.sleep(SHORT_DELAY) 
    pyautogui.press('enter')
    
    # 3. Esperamos un poco más para que la ventana SÍ se abra antes de escribir
    time.sleep(0.2) 
    
    # 4. Escribimos un mensaje aleatorio para variar la broma
    pyautogui.write(random.choice(mensajes))
    
    # Opcional: Escribir algo más y presionar Enter
    # pyautogui.press('enter')
    # pyautogui.write('Esto es demasiado HARD')
    
    # 5. Espera mínima antes de la siguiente repetición
    time.sleep(SHORT_DELAY)

print("Ciclo de apertura terminado. Iniciando ciclo de cierre.")

# 2. CICLO DE CIERRE HARDCORE
# Este ciclo es el más peligroso si es demasiado rápido, ya que cierra TODO.
for j in range(NUM_ITERATIONS): 
    # 1. Cierra la ventana actual (Alt + F4)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(SHORT_DELAY) 
    
    # 2. Navega al botón "No guardar" (asumiendo que está a la derecha en el diálogo de Notepad)
    pyautogui.press('right')
    time.sleep(SHORT_DELAY) 
    
    # 3. Presiona Enter para confirmar "No guardar"
    pyautogui.press('enter')
    
    # Espera mínima antes de intentar cerrar la siguiente ventana
    time.sleep(SHORT_DELAY)
    
print("Proceso COMPLETADO. ¡Qué desastre! 😈")
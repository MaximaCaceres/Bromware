import pyautogui
import time
import random
import subprocess # Necesitas esta librería para ejecutar comandos del sistema

# --- CONFIGURACIÓN DE SEGURIDAD (¡DESACTIVADA PARA EL MÁXIMO CAOS!) ---
# Para detener el script, MUEVE EL RATÓN a la esquina superior izquierda si tienes 'FAILSAFE = True' (por defecto)
# O simplemente apaga la PC del botón de encendido si está fuera de control.
# pyautogui.FAILSAFE = False # Peligroso, no recomendado para un entorno de trabajo.

SHORT_DELAY = 0.05 
NUM_ITERATIONS = 50 

mensajes = [
    "TE HAN HACKEADO XD",
    "EL SISTEMA ESTA COMPROMETIDO",
    "PONTE A TRABAJAR!",
    "PYTHON RULES!",
    "PUTO EL QUE LEE" 
]

print(f"Iniciando ciclo de apertura y escritura: {NUM_ITERATIONS} veces. ¡Alerta Roja!")
time.sleep(3) # Pausa de 3 segundos para que puedas prepararte

# 1. CICLO DE APERTURA Y ESCRITURA CAÓTICA
for i in range(NUM_ITERATIONS):
    pyautogui.hotkey('win', 'r') 
    time.sleep(SHORT_DELAY) 
    
    pyautogui.write('notepad')
    time.sleep(SHORT_DELAY) 
    pyautogui.press('enter')
    
    # Esperamos un poco para que la ventana SÍ se abra
    time.sleep(0.2) 
    
    pyautogui.write(random.choice(mensajes))
    
    # Mueve el ratón para aumentar la distracción visual
    pyautogui.moveTo(random.randint(100, 800), random.randint(100, 600), duration=0.1)
    
    time.sleep(SHORT_DELAY)

print("Ciclo de apertura terminado. Iniciando ciclo de cierre.")

# 2. CICLO DE CIERRE HARDCORE
for j in range(NUM_ITERATIONS): 
    pyautogui.hotkey('alt', 'f4')
    time.sleep(SHORT_DELAY) 
    
    # Intenta ir a "No Guardar"
    pyautogui.press('right')
    time.sleep(SHORT_DELAY) 
    pyautogui.press('enter')
    
    time.sleep(SHORT_DELAY)
    
print("Proceso de caos principal completado.")

# ---------------------------------------------
# 3. ETAPA FINAL: BLOQUEO Y REINICIO
# ---------------------------------------------

# A. Bloqueo de Sesión (Win + L)
# Esto bloquea la PC inmediatamente, mostrando la pantalla de login.
print("Bloqueando sesión en 3 segundos...")
time.sleep(3) 
pyautogui.hotkey('win', 'l') 
print("¡Sesión Bloqueada!")

# B. Reinicio Forzado
# Usamos el módulo 'subprocess' para ejecutar el comando de Windows 'shutdown'.
# El comando es: 'shutdown /r /t 0'
# /r = Reiciar
# /t 0 = Tiempo de espera 0 segundos (inmediato)
print("Reiniciando sistema en 5 segundos...")
time.sleep(5) 

# Ejecuta el comando de reinicio
# Nota: Necesitarás permisos de administrador para que esto funcione en algunas configuraciones.
try:
    subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
    print("Comando de reinicio ejecutado. ¡Adiós!")
except Exception as e:
    print(f"Error al intentar reiniciar (posiblemente por falta de permisos): {e}")

# Si el comando de reinicio fallara, se podría intentar el bloqueo de sesión nuevamente
# o simplemente dejar el sistema bloqueado para que la víctima lo vea al regresar.
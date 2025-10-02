import pyautogui
import time
import os
import subprocess

# --- Importación de la función de la lectora ---
# ASUMIENDO que la función 'eject_dvd_drive' está en el archivo 'prueba.py'
# y que 'prueba.py' está en el mismo directorio.
from prueba import eject_dvd_drive 

# --- Configuración ---
DRIVE_LETTER = 'D'  # ¡Asegúrate de que esta sea la letra correcta de tu lectora!

print("Iniciando el ciclo de apertura de Chrome y expulsión de lectora...")

# Usamos un bucle 'for' para repetir la acción 5 veces
for i in range(2):
    print(f"\n--- Ciclo {i + 1} de 5 ---")
    
    # 1. Simula presionar la tecla Windows y la 'r' (Win + R) para abrir 'Ejecutar'.
    pyautogui.hotkey('win', 'r')
    
    # 2. Espera un momento para que el diálogo 'Ejecutar' se abra
    time.sleep(0.1) 
    
    # 3. Escribe "chrome" en el diálogo 'Ejecutar'
    pyautogui.write('chrome')
    
    # 4. Simula presionar la tecla Enter para ejecutar el comando y abrir Chrome
    pyautogui.press('enter')
    
    # 5. Espera un tiempo para que Chrome se abra y tome el foco
    time.sleep(0.5) 
    
    # 6. --- ¡NUEVO! Expulsar la lectora de CD/DVD ---
    print(f"Llamando a eject_dvd_drive('{DRIVE_LETTER}')")
    eject_dvd_drive(DRIVE_LETTER) # Llama a la función de 'prueba.py'

    # 7. Simula la escritura del texto
    pyautogui.write('PUTO EL QUE LEE', interval=0.1)
    
    # 8. Espera un momento antes de empezar a cerrar las ventanas
    time.sleep(1)

print("\n--- Cerrando las 5 ventanas de Chrome ---")

# Bucle para cerrar 5 ventanas (asumiendo que son las 5 instancias de Chrome)
for j in range(2):
    # Simula Alt + F4 para cerrar la ventana activa
    pyautogui.hotkey('alt', 'f4')
    
    # Espera para dar tiempo al cierre y evitar que se cierre la ventana equivocada
    time.sleep(0.5) 
    
    # Si Chrome te pregunta "¿Quieres cerrar todas las pestañas?", este código no lo manejará. 
    # Si eso pasa, puedes agregar pyautogui.press('enter') aquí.
        # 5. Espera un tiempo para que Chrome se abra y tome el foco
    time.sleep(1.5) 
    
    # 6. --- ¡NUEVO! Expulsar la lectora de CD/DVD ---
    print(f"Llamando a eject_dvd_drive('{DRIVE_LETTER}')")
    eject_dvd_drive(DRIVE_LETTER) # Llama a la función de 'prueba.py'
    
print("Proceso finalizado.")
    
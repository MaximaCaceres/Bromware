import time
# Asumiendo que 'eject_dvd_drive' está importada de 'prueba.py'
from prueba import eject_dvd_drive 

DRIVE_LETTER = 'D'

print("¡Modo BUCLE INFINITO activado! Presiona Ctrl+C para detener.")

while True:
    # 1. Expulsar la bandeja
    eject_dvd_drive(DRIVE_LETTER)
    
    # 2. Esperar un instante antes de volver a intentar
    time.sleep(0.5)
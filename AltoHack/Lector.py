import os
import subprocess
import platform

def abrir_lectora_comando(drive_letter='D'):
    """
    Abre la bandeja de la lectora de CD/DVD ejecutando un comando de sistema.
    :param drive_letter: La letra de la unidad en Windows (ej. 'D').
    """
    sistema = platform.system()
    
    try:
        if sistema == "Windows":
            # Comando de PowerShell: usa la clase WMI para enviar el comando de expulsión
            # 'D' es la letra de la unidad.
            #command = f"powershell (New-Object -comobject 'WMPlayer.OCX.7').CDROMs.Item(0).Eject()"
            # Nota: Algunos sistemas pueden requerir 'cdrom.Eject()' en lugar de 'CDROMs.Item(0).Eject()'
            
            # Puedes usar este comando más simple, pero la letra de la unidad no siempre funciona
            command = f"PowerShell (Get-WmiObject -Class Win32_StorageExtent | Where-Object {{ $_.Name -like '*{drive_letter}*' }}).Eject()"
            
            subprocess.run(command, shell=True, check=True)
            print(f"Bandeja de la unidad abierta en Windows.")

        elif sistema in ["Linux", "Darwin"]: # Darwin es macOS
            # Comando universal en sistemas Unix/Linux/macOS
            subprocess.run(['eject'], check=True)
            print("Comando 'eject' ejecutado con éxito.")

        else:
            print(f"Sistema operativo '{sistema}' no soportado para este comando.")

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando. Asegúrate de que la unidad exista o que tienes permisos. Error: {e}")
    except FileNotFoundError:
        print("El comando de sistema (powershell o eject) no fue encontrado.")

# Ejemplo de uso:
# En Windows, cambia 'D' por la letra de tu unidad
abrir_lectora_comando('D')
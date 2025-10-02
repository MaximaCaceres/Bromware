import ctypes
from ctypes import wintypes
import sys

# --- 1. Definiciones de la API de Windows ---
# Cargamos la librería del kernel de Windows
try:
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
except FileNotFoundError:
    print("Error: No se puede cargar kernel32.dll. ¿Estás en Windows?")
    sys.exit()

# Constantes necesarias para abrir el dispositivo y expulsarlo
GENERIC_READ = 0x80000000
GENERIC_WRITE = 0x40000000
OPEN_EXISTING = 3
IOCTL_STORAGE_EJECT_MEDIA = 0x2D4808 # Código de control de expulsión

# Declaración de funciones (para asegurar el tipo de argumentos)
# (Esto hace que el código sea largo, pero es vital para la estabilidad)
CreateFile = kernel32.CreateFileA
CreateFile.argtypes = [
    wintypes.LPCSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE
]
CreateFile.restype = wintypes.HANDLE

DeviceIoControl = kernel32.DeviceIoControl
DeviceIoControl.argtypes = [
    wintypes.HANDLE, wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD, wintypes.LPDWORD, wintypes.LPVOID
]
DeviceIoControl.restype = wintypes.BOOL 

# -----------------------------------------------------------------------------------------

def eject_dvd_drive(drive_letter: str = 'D'):
    """Envía la señal directa de expulsión a la unidad usando la API de Windows (ctypes)."""
    
    # La ruta al dispositivo debe ser en el formato especial \\.\D:
    device_path = f"\\\\.\\{drive_letter}:"
    handle = wintypes.HANDLE(-1).value # Inicializar Handle inválido

    try:
        # 1. Obtener un "handle" (identificador) al dispositivo
        handle = CreateFile(
            device_path.encode('ascii'), # La ruta debe ser en formato bytes
            GENERIC_READ | GENERIC_WRITE,
            0, None, OPEN_EXISTING, 0, None 
        )

        if handle == wintypes.HANDLE(-1).value:
            error_code = ctypes.get_last_error()
            print(f"Error al obtener acceso a {drive_letter}:. Código: {error_code}")
            print("Posiblemente la unidad está siendo usada o la letra es incorrecta.")
            return

        # 2. Enviar el comando IOCTL_STORAGE_EJECT_MEDIA
        bytes_returned = wintypes.DWORD(0)
        success = DeviceIoControl(
            handle,
            IOCTL_STORAGE_EJECT_MEDIA, # El código de expulsión
            None, 0, None, 0, ctypes.byref(bytes_returned), None
        )
        
        if success:
            print(f"¡Expulsión exitosa de la unidad {drive_letter}:! (Usando ctypes)")
        else:
            error_code = ctypes.get_last_error()
            print(f"Error al enviar la señal de expulsión. Código de Windows: {error_code}")
            print("La unidad no pudo expulsar el disco (puede estar vacía o bloqueada).")

    finally:
        # 3. Cerrar el "handle" si se abrió correctamente
        if handle != wintypes.HANDLE(-1).value:
            kernel32.CloseHandle(handle)

# Ejecuta el código. Si esto falla, el problema es físico o de permisos muy estrictos.
eject_dvd_drive('D')
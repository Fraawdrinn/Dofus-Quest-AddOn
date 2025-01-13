import ctypes
import tkinter as tk

import win32con
import win32gui
from use_data import Data

# Tkinter init
root = tk.Tk()
root.title("Overlay Example")
root.resizable(False, False)  # noqa: FBT003
WIDTH = 300
HEIGHT = 400
root.geometry(f"{WIDTH}x{HEIGHT}+500+300") # Adding 500 and 300 for window pos

# Assure la mise à jour complète de la fenêtre avant toute interaction
root.update_idletasks()
# Récupère le handle de la fenêtre actuellement au premier plan
hwnd = ctypes.windll.user32.GetForegroundWindow()
# Garder la fenêtre en haut avec Tkinter
root.attributes("-topmost", True)  # noqa: FBT003
# Appliquer l'overlay avec pywin32
ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(
    hwnd,
    win32con.GWL_EXSTYLE,
    ex_style | win32con.WS_EX_LAYERED | win32con.WS_EX_TOPMOST,
    )
# Ajuster la transparence si nécessaire (par exemple : 255 pour opaque)
win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)

data_dir: str = "quests"
data_to_fetch: str = "quests_1653.json"
file_path: str = f"projet-py/outputs/{data_dir}/{data_to_fetch}"
extractor: Data = Data(file_path)
#unique coordinates
unique_coordinates: list = extractor.get_unique_coordinates()
print("coordinates : ", unique_coordinates)

# Fonction pour configurer l'overlay
def create_overlay():
    """Displays the window and the collected informations."""
    # Ajouter un widget pour afficher un texte
    for coord in unique_coordinates:
        label = tk.Label(root, text=coord, font=("Arial", 14))
        label.pack(pady=5)

    # Exécuter l'interface Tkinter
    root.mainloop()

def main():
    create_overlay()
    return

if __name__ == "__main__":
    main()

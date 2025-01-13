import ctypes
import tkinter as tk

import win32con
import win32gui

# Tkinter init
root = tk.Tk()
root.title("Overlay Example")
root.resizable(False, False)  # noqa: FBT003
root.geometry("300x200+500+300")

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



# Fonction pour configurer l'overlay
def create_overlay():
    """Displays the window and the collected informations."""
    # Ajouter un widget pour afficher un texte
    label = tk.Label(root, text="This is an overlay window", font=("Arial", 14))
    label.pack(pady=50)

    # Exécuter l'interface Tkinter
    root.mainloop()


def main():
    create_overlay()
    return

if __name__ == "__main__":
    main()

import tkinter as tk
import win32gui
import win32con
import ctypes

# Fonction pour configurer l'overlay
def create_overlay():
    root = tk.Tk()
    root.title("Overlay Example")
    
    # Empêche la fenêtre d'être redimensionnée
    root.resizable(False, False)

    # Dimensions et position de la fenêtre
    root.geometry("300x200+500+300")

    # Ajouter un widget pour afficher un texte
    label = tk.Label(root, text="This is an overlay window", font=("Arial", 14))
    label.pack(pady=50)

    # Obtenir le handle de la fenêtre Tkinter (HWND)
    root.update_idletasks()  # S'assurer que la fenêtre est créée
    hwnd = ctypes.windll.user32.GetForegroundWindow()  # Utiliser ctypes pour obtenir le handle valide
    
    # Appliquer l'overlay avec pywin32
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style | win32con.WS_EX_LAYERED | win32con.WS_EX_TOPMOST)
    
    # Ajuster la transparence si nécessaire (par exemple : 255 pour opaque)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)

    # Garder la fenêtre en haut avec Tkinter
    root.attributes("-topmost", True)
    
    # Exécuter l'interface Tkinter
    root.mainloop()

# Lancer la fonction pour créer l'overlay
create_overlay()

import tkinter as tk
import win32gui
import win32con

# Création de la fenêtre Tkinter
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

    # Appliquer l'overlay avec pywin32
    hwnd = win32gui.GetHWND(root.winfo_id())  # Obtenir le handle de la fenêtre Tkinter
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    # Exécuter l'interface Tkinter
    root.mainloop()

# Lancer la fonction pour créer l'overlay
create_overlay()

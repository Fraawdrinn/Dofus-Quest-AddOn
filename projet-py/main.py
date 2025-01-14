import tkinter as tk

from use_data import Data

# Tkinter init
root = tk.Tk()
root.title("Overlay Example")
root.resizable(width=False, height=False)
WIDTH = 300
HEIGHT = 400
POSX = 1500
POSY = 300
root.geometry(f"{WIDTH}x{HEIGHT}+{POSX}+{POSY}")  # Set window size and position

# Assure la mise à jour complète de la fenêtre avant toute interaction
root.update_idletasks()

# Keep the window on top
root.attributes("-topmost", True)  # noqa: FBT003

# Make the window transparent (optional)
root.attributes("-alpha", 0.9)  # Adjust alpha for transparency (1.0 = opaque)

# Remove window decorations for an overlay effect
root.overrideredirect(boolean=True)

data_dir: str = "quests"
data_to_fetch: str = "quests_1653.json"
file_path: str = f"projet-py/outputs/{data_dir}/{data_to_fetch}"
extractor: Data = Data(file_path)

# Get unique coordinates from the data
unique_coordinates: list = extractor.get_unique_coordinates()
print("coordinates : ", unique_coordinates)

# Function to configure the overlay
def create_overlay() -> None:
    """Display the window and the collected information."""
    # Add a widget to display text
    for coord in unique_coordinates:
        label = tk.Label(root, text=coord, font=("Arial", 14), bg="white")
        label.pack(pady=5)

    # Run the Tkinter interface
    root.mainloop()

def main() -> None:
    """Execute the main functions."""
    create_overlay()

if __name__ == "__main__":
    main()


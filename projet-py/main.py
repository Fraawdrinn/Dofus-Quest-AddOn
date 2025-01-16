import sys  # noqa: D100

from PyQt5 import QtCore, QtGui, QtWidgets
from use_data import Data


class OverlayApp(QtWidgets.QWidget):
    """Overlay App using Qt."""

    def __init__(self, unique_coordinates: list) -> None:
        """Init Overlay App."""
        super().__init__()
        self.unique_coordinates = unique_coordinates
        self.init_ui()

    def init_ui(self) -> None:
        """Init window."""
        # Set window properties
        self.setWindowTitle("Overlay Example")
        self.setFixedSize(300, 400)
        self.setGeometry(1500, 300, 300, 400)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint,
            #| QtCore.Qt.FramelessWindowHint
            #| QtCore.Qt.Tool,  # Ensures no taskbar icon
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.9)  # Transparency (1.0 = opaque)

        # Layout and label setup
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        # Add labels for coordinates
        for coord in self.unique_coordinates:
            label = QtWidgets.QLabel(str(coord), self)
            label.setFont(QtGui.QFont("Arial", 14))
            label.setStyleSheet("""
                background-color: white;
                padding: 5px;
            """)
            label.setAlignment(QtCore.Qt.AlignCenter)
            layout.addWidget(label)

        self.setLayout(layout)


def main() -> None:
    """Execute main program."""
    # Load data
    data_dir: str = "quests"
    data_to_fetch: str = "quests_1653.json"
    file_path: str = f"projet-py/outputs/{data_dir}/{data_to_fetch}"

    extractor = Data(file_path)
    unique_coordinates = extractor.get_unique_coordinates()

    # Create and run the application
    app = QtWidgets.QApplication(sys.argv)
    overlay = OverlayApp(unique_coordinates)
    overlay.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

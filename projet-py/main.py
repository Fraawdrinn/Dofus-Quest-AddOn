import sys  # noqa: D100

from PyQt5 import QtCore, QtGui, QtWidgets
from use_data import Data


def create_main_menu_button(switch_menu) -> QtWidgets:
  """Create a main menu button for navigation."""
  main_menu_button = QtWidgets.QPushButton("Main Menu")
  main_menu_button.setStyleSheet("padding: 5px; font-size: 12px;")
  main_menu_button.setFixedSize(100, 30)
  main_menu_button.clicked.connect(lambda: switch_menu("main"))
  return main_menu_button

class OverlayMenu(QtWidgets.QWidget):
  """Overlay Menu Widget."""

  def __init__(self, unique_coordinates:list, switch_menu) -> None:
    super().__init__()
    self.unique_coordinates = unique_coordinates
    self.init_ui(switch_menu)

  def init_ui(self, switch_menu) -> None:
    """Init Overlay UI."""
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

    # Add main menu button
    main_menu_button = create_main_menu_button(switch_menu)
    layout.addWidget(main_menu_button, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)

    self.setLayout(layout)


class SearchMenu(QtWidgets.QWidget):
  """Search Menu Widget."""

  def __init__(self, switch_menu):
      super().__init__()
      self.init_ui(switch_menu)

  def init_ui(self, switch_menu) -> None:
      """Init Search Menu UI."""
      layout = QtWidgets.QVBoxLayout(self)
      label = QtWidgets.QLabel("Search Menu: Add functionality here")
      label.setAlignment(QtCore.Qt.AlignCenter)
      layout.addWidget(label)

      # Add main menu button
      main_menu_button = create_main_menu_button(switch_menu)
      layout.addWidget(main_menu_button, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)

      self.setLayout(layout)


class AboutMenu(QtWidgets.QWidget):
  """About Menu Widget."""

  def __init__(self, switch_menu) -> None:
      """."""
      super().__init__()
      self.init_ui(switch_menu)

  def init_ui(self, switch_menu) -> None:
      """Init About Menu UI."""
      layout = QtWidgets.QVBoxLayout(self)
      label = QtWidgets.QLabel("About Menu: Add details here")
      label.setAlignment(QtCore.Qt.AlignCenter)
      layout.addWidget(label)

      # Add main menu button
      main_menu_button = create_main_menu_button(switch_menu)
      layout.addWidget(main_menu_button, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)

      self.setLayout(layout)

class MainMenu(QtWidgets.QStackedWidget):
  """Main Menu managing multiple menus."""

  def __init__(self, unique_coordinates: list) -> None:
    """Display main window opening as menu."""
    super().__init__()
    self.setWindowTitle("Multi-Menu Application")
    self.setGeometry(100, 100, 400, 300)

    # Create menus
    self.main_menu = self.create_main_menu()
    self.overlay_menu = OverlayMenu(unique_coordinates, self.switch_menu)
    self.search_menu = SearchMenu(self.switch_menu)
    self.about_menu = AboutMenu(self.switch_menu)

    # Add menus to the stack
    self.addWidget(self.main_menu)
    self.addWidget(self.overlay_menu)
    self.addWidget(self.search_menu)
    self.addWidget(self.about_menu)

    # Set the main menu as the default
    self.switch_menu("main")

  def create_main_menu(self) -> None:
    """Create the main menu widget."""
    widget = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(widget)

    # Navigation buttons
    search_button = QtWidgets.QPushButton("Search Menu")
    search_button.clicked.connect(lambda: self.switch_menu("search"))
    layout.addWidget(search_button)

    overlay_button = QtWidgets.QPushButton("Overlay Menu")
    overlay_button.clicked.connect(lambda: self.switch_menu("overlay"))
    layout.addWidget(overlay_button)

    about_button = QtWidgets.QPushButton("About Menu")
    about_button.clicked.connect(lambda: self.switch_menu("about"))
    layout.addWidget(about_button)

    widget.setLayout(layout)
    return widget

  def switch_menu(self, menu_name: str) -> None:
    """Switch between menus based on menu_name."""
    if menu_name == "main":
        self.setCurrentWidget(self.main_menu)
    elif menu_name == "search":
        self.setCurrentWidget(self.search_menu)
    elif menu_name == "overlay":
        self.setCurrentWidget(self.overlay_menu)
    elif menu_name == "about":
        self.setCurrentWidget(self.about_menu)


def main() -> None:
    """Execute main program."""
    # Load data
    data_dir: str = "quests"
    data_to_fetch: str = "1653.json"
    file_path: str = f"Database/{data_dir}/{data_to_fetch}"

    extractor = Data(file_path)
    unique_coordinates = extractor.get_unique_coordinates()

    # Create and run the application
    app = QtWidgets.QApplication(sys.argv)
    main_menu = MainMenu(unique_coordinates)
    main_menu.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

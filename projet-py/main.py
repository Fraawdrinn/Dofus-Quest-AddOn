import json
import sys
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
  QApplication,
  QDesktopWidget,
  QLabel,
  QLineEdit,
  QListWidget,
  QMainWindow,
  QPushButton,
  QStackedWidget,
  QVBoxLayout,
  QWidget,
)
from use_data import Data


def create_main_menu_button(switch_menu) -> QPushButton:
  """Create a main menu button for navigation."""
  main_menu_button = QPushButton("Main Menu")
  main_menu_button.setStyleSheet("padding: 5px; font-size: 12px;")
  main_menu_button.setFixedSize(100, 30)
  main_menu_button.clicked.connect(lambda: switch_menu("main"))
  return main_menu_button


class OverlayMenu(QWidget):
  """Overlay Menu Widget."""

  def __init__(self, unique_coordinates: list, switch_menu):
    """."""
    super().__init__()
    self.unique_coordinates = unique_coordinates
    self.init_ui(switch_menu)

  def init_ui(self, switch_menu) -> None:
    """Init Overlay UI."""
    layout = QVBoxLayout(self)
    layout.setContentsMargins(10, 10, 10, 10)

    # Add labels for coordinates
    for coord in self.unique_coordinates:
      label = QLabel(str(coord), self)
      label.setFont(QFont("Arial", 14))
      label.setStyleSheet("background-color: gray;padding: 5px;")
      label.setAlignment(Qt.AlignCenter)
      layout.addWidget(label)

    # Add main menu button
    main_menu_button = create_main_menu_button(switch_menu)
    layout.addWidget(main_menu_button, alignment=Qt.AlignTop | Qt.AlignRight)

    self.setLayout(layout)


class SearchMenu(QWidget):
  """Search Menu Widget for quests."""

  def __init__(self, switch_menu):
    """Initialize the SearchMenu."""
    super().__init__()
    self.switch_menu = switch_menu
    self.db_file = "Database/other/all.json"
    self.data = self.load_data()
    self.filtered_results = []
    self.init_ui()

  def init_ui(self):
    """."""
    layout = QVBoxLayout(self)
    self.search_input = QLineEdit(self)
    self.search_input.setPlaceholderText("Recherchez une quête...")
    self.search_input.textChanged.connect(self.update_search_query)
    self.results_list = QListWidget(self)

    layout.addWidget(self.search_input)
    layout.addWidget(self.results_list)
    layout.addWidget(create_main_menu_button(self.switch_menu))
    self.setLayout(layout)

  def load_data(self):
    try:
      with Path(self.db_file).open(encoding="utf-8") as f:
        return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
      return {}

  def update_search_query(self):
    query = self.search_input.text()
    self.filtered_results = [
      (name, quest_id) for name, quest_id in self.data.items()
      if query.lower() in name.lower()
    ]
    self.update_results_list()

  def update_results_list(self):
    self.results_list.clear()
    for name, quest_id in self.filtered_results:
      self.results_list.addItem(f"{name} - ID: {quest_id}")
    if not self.filtered_results:
      self.results_list.addItem("Aucune quête trouvée.")


class AboutMenu(QWidget):
  """About Menu Widget."""

  def __init__(self, switch_menu) -> None:
    """."""
    super().__init__()
    self.init_ui(switch_menu)

  def init_ui(self, switch_menu) -> None:
    """Init About Menu UI."""
    layout = QVBoxLayout(self)
    label = QLabel("About Menu: Add details here")
    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label)

    # Add main menu button
    main_menu_button = create_main_menu_button(switch_menu)
    layout.addWidget(main_menu_button, alignment=Qt.AlignTop | Qt.AlignRight)

    self.setLayout(layout)


class MainWindow(QMainWindow):
  """Main Window using QMainWindow."""

  def __init__(self, unique_coordinates: list) -> None:
    """Initialize Main Window."""
    super().__init__()

    # Get the screen size
    screen_size = QDesktopWidget().screenGeometry()
    width, height = 400, 300
    posx, posy = screen_size.width(), screen_size.height()

    self.setWindowTitle("Multi-Menu Application")
    self.setGeometry(posx//2-width, posy//2-height, width, height)

    # Window Flags: Movable, Overlay
    self.setWindowFlags(self.windowFlags() & ~Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    # Create the stacked widget to manage menus
    self.stacked_widget = QStackedWidget(self)
    self.setCentralWidget(self.stacked_widget)

    # Create the menus
    self.main_menu = self.create_main_menu()
    self.overlay_menu = OverlayMenu(unique_coordinates, self.switch_menu)
    self.search_menu = SearchMenu(self.switch_menu)
    self.about_menu = AboutMenu(self.switch_menu)

    # Add menus to the stacked widget
    self.stacked_widget.addWidget(self.main_menu)
    self.stacked_widget.addWidget(self.overlay_menu)
    self.stacked_widget.addWidget(self.search_menu)
    self.stacked_widget.addWidget(self.about_menu)

    # Set the initial menu to main
    self.switch_menu("main")

  def create_main_menu(self) -> QWidget:
    """Create the main menu widget."""
    widget = QWidget()
    layout = QVBoxLayout(widget)

    # Navigation buttons
    search_button = QPushButton("Search Menu")
    search_button.clicked.connect(lambda: self.switch_menu("search"))
    layout.addWidget(search_button)

    overlay_button = QPushButton("Overlay Menu")
    overlay_button.clicked.connect(lambda: self.switch_menu("overlay"))
    layout.addWidget(overlay_button)

    about_button = QPushButton("About Menu")
    about_button.clicked.connect(lambda: self.switch_menu("about"))
    layout.addWidget(about_button)

    widget.setLayout(layout)
    return widget

  def switch_menu(self, menu_name: str) -> None:
    """Switch between menus based on menu_name."""
    if menu_name == "main":
        self.stacked_widget.setCurrentWidget(self.main_menu)
    elif menu_name == "search":
        self.stacked_widget.setCurrentWidget(self.search_menu)
    elif menu_name == "overlay":
        self.stacked_widget.setCurrentWidget(self.overlay_menu)
    elif menu_name == "about":
        self.stacked_widget.setCurrentWidget(self.about_menu)


def main() -> None:
  """Execute main program."""
  # Load data
  data_dir: str = "quests"
  data_to_fetch: str = "1653.json"
  file_path: str = f"Database/{data_dir}/{data_to_fetch}"

  extractor = Data(file_path)
  unique_coordinates = extractor.get_unique_coordinates()

  # Create and run the application
  app = QApplication(sys.argv)
  main_window = MainWindow(unique_coordinates)
  main_window.show()
  # print(main_window.screen_size)
  sys.exit(app.exec_())


if __name__ == "__main__":
  main()

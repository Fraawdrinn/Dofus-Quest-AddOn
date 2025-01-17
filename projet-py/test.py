import json
from pathlib import Path

from PyQt5.QtWidgets import QLineEdit, QListWidget, QMainWindow, QVBoxLayout, QWidget


class SearchMenu(QMainWindow):
    """."""

    def __init__(self):
        """."""
        super().__init__()

        # Initialize the UI
        self.setWindowTitle("Search Menu")
        self.setGeometry(100, 100, 400, 300)

        # Load the quest data
        self.db_file = "Databse/quests/1653.json"
        self.data = self.load_data()

        # Set up UI components
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search quests...")
        self.search_input.textChanged.connect(self.update_search_query)

        self.results_list = QListWidget(self)

        layout = QVBoxLayout()
        layout.addWidget(self.search_input)
        layout.addWidget(self.results_list)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.filtered_results = []

    def load_data(self):
        """Load the quest data from the JSON file."""
        try:
            with Path(self.db_file).open() as f:
                return json.load(f)
        except FileNotFoundError:
            print("Database file not found!")
            return {}

    def update_search_query(self):
        """Update the search query and filters results."""
        query = self.search_input.text()
        self.filtered_results = self.search_quests(query)
        self.update_results_list()

    def search_quests(self, query):
        """Filter the quest data based on the search query."""
        # Simple case-insensitive search for quests containing the query
        return [
            (name, quest_id) for name, quest_id in self.data.items()
            if query.lower() in name.lower()
        ]

    def update_results_list(self):
        """Update the list widget with filtered results."""
        self.results_list.clear()  # Clear previous results
        for name, quest_id in self.filtered_results:
            self.results_list.addItem(f"{name} - ID: {quest_id}")

# Example usage
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    search_menu = SearchMenu()
    search_menu.show()
    app.exec_()

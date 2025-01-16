import json
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QListWidget, QVBoxLayout, QWidget

class SearchMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the UI
        self.setWindowTitle("Search Menu")
        self.setGeometry(100, 100, 400, 300)

        # Load the quest data
        self.db_file = 'quests.json'  # Path to your JSON file
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

        self.filtered_results = []  # List to store filtered results

    def load_data(self):
        """Loads the quest data from the JSON file."""
        try:
            with open(self.db_file, 'r') as f:
                return json.load(f)  # Assuming the file contains a dictionary of quest names and IDs
        except FileNotFoundError:
            print("Database file not found!")
            return {}

    def update_search_query(self):
        """Updates the search query and filters results."""
        query = self.search_input.text()
        self.filtered_results = self.search_quests(query)
        self.update_results_list()

    def search_quests(self, query):
        """Filters the quest data based on the search query."""
        # Simple case-insensitive search for quests containing the query
        return [
            (name, quest_id) for name, quest_id in self.data.items()
            if query.lower() in name.lower()
        ]

    def update_results_list(self):
        """Updates the list widget with filtered results."""
        self.results_list.clear()  # Clear previous results
        for name, quest_id in self.filtered_results:
            self.results_list.addItem(f"{name} - ID: {quest_id}")

# Example usage
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    search_menu = SearchMenu()
    search_menu.show()
    app.exec_()

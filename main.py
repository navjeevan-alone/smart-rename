import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog, QLabel, QMessageBox

class FileRenamerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Renamer Tool")
        self.setGeometry(200, 200, 400, 200)
        
        self.folder_path = ""
        
        # Layout and Widgets
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Folder Selection
        self.folder_label = QLabel("Selected Folder:")
        self.layout.addWidget(self.folder_label)
        
        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_folder_button)

        # Pattern Input
        self.pattern_label = QLabel("Enter Prefix Pattern:")
        self.layout.addWidget(self.pattern_label)
        
        self.pattern_input = QLineEdit()
        self.pattern_input.setPlaceholderText("Enter prefix pattern (e.g., 'file_')")
        self.layout.addWidget(self.pattern_input)

        # Rename Button
        self.rename_button = QPushButton("Rename Files")
        self.rename_button.clicked.connect(self.rename_files)
        self.layout.addWidget(self.rename_button)

    def select_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.folder_label.setText(f"Selected Folder: {self.folder_path}")

    def rename_files(self):
        if not self.folder_path:
            QMessageBox.warning(self, "Warning", "Please select a folder.")
            return

        prefix_pattern = self.pattern_input.text().strip()
        if not prefix_pattern:
            QMessageBox.warning(self, "Warning", "Please enter a prefix pattern.")
            return

        try:
            for count, filename in enumerate(os.listdir(self.folder_path), start=1):
                file_path = os.path.join(self.folder_path, filename)
                if os.path.isfile(file_path):
                    file_extension = os.path.splitext(filename)[1]
                    new_name = f"{prefix_pattern}{count}{file_extension}"
                    new_path = os.path.join(self.folder_path, new_name)
                    os.rename(file_path, new_path)

            QMessageBox.information(self, "Success", "Files renamed successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = QApplication([])
    window = FileRenamerApp()
    window.show()
    app.exec_()

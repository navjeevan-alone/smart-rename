import os
import logging
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton,
                             QFileDialog, QLabel, QMessageBox, QCheckBox, QHBoxLayout,
                             QGroupBox, QTextEdit)

from file_operations import count_files, copy_files
from renamer import FileRenamer  # Import only FileRenamer class to avoid circular import
from logger import setup_logging
from PyQt5.QtGui import QFont
from utils import load_stylesheet 

class FileRenamerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rename Genie")
        self.setGeometry(200, 200, 600, 400)

        self.setStyleSheet(load_stylesheet("styles.css"))
        setup_logging()  # Setup logging
        self.folder_path = ""
        self.output_path = ""

        # Layout and Widgets
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        font = QFont("Arial", 16)

        # Folder Selection
        self.folder_label = QLabel("Selected Folder:")
        self.folder_label.setFont(font)
        
        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.clicked.connect(self.select_folder)
        
        # Horizontal Layout for Folder Selection
        folder_layout = QHBoxLayout()
        folder_layout.addWidget(self.folder_label)
        folder_layout.addWidget(self.select_folder_button)
        self.layout.addLayout(folder_layout)

        # Output Path Selection
        self.output_label = QLabel("Selected Output Folder (Optional):")
        self.select_output_button = QPushButton("Select Output Folder")
        self.select_output_button.clicked.connect(self.select_output_path)
        
        # Horizontal Layout for Output Path Selection
        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.select_output_button)
        self.layout.addLayout(output_layout)

        # Pattern Input
        self.pattern_label = QLabel("Enter Prefix Pattern:")
        self.pattern_input = QLineEdit()
        self.pattern_input.setPlaceholderText("Enter prefix pattern (e.g., 'file_')")

        # Horizontal Layout for Pattern Input
        pattern_layout = QHBoxLayout()
        pattern_layout.addWidget(self.pattern_label)
        pattern_layout.addWidget(self.pattern_input)
        self.layout.addLayout(pattern_layout)

        # Start Index Input
        self.start_index_label = QLabel("Start Index:")
        self.start_index_input = QLineEdit()
        self.start_index_input.setPlaceholderText("Enter start index (default is 1)")

        # Horizontal Layout for Start Index Input
        start_index_layout = QHBoxLayout()
        start_index_layout.addWidget(self.start_index_label)
        start_index_layout.addWidget(self.start_index_input)
        self.layout.addLayout(start_index_layout)

        # Smart Rename Checkbox
        self.smart_rename_checkbox = QCheckBox("Smart Rename")
        self.layout.addWidget(self.smart_rename_checkbox)

        # Rename Button
        self.rename_button = QPushButton("Rename Files")
        self.rename_button.clicked.connect(self.rename_files)
        self.layout.addWidget(self.rename_button)

        # File Count Button
        self.file_count_button = QPushButton("Count Files")
        self.file_count_button.clicked.connect(self.count_files)
        self.layout.addWidget(self.file_count_button)

        self.file_count_label = QLabel("Number of files: 0")
        self.layout.addWidget(self.file_count_label)

        # Log Panel
        self.log_group = QGroupBox("Logs")
        self.layout.addWidget(self.log_group)

        self.log_layout = QVBoxLayout()
        self.log_group.setLayout(self.log_layout)

        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_layout.addWidget(self.log_text)

# The rest of your application code goes here

    def select_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.folder_label.setText(f"Selected Folder: {self.folder_path}")

    def select_output_path(self):
        self.output_path = QFileDialog.getExistingDirectory(self, "Select Output Path")
        self.output_label.setText(f"Selected Output Path: {self.output_path}")

    def count_files(self):
        if self.folder_path:
            num_files = count_files(self.folder_path)
            self.file_count_label.setText(f"Number of files: {num_files}")
            logging.info(f"Number of files in directory: {num_files}")

    def rename_files(self):
        if not self.folder_path:
            QMessageBox.warning(self, "Warning", "Please select a folder.")
            return

        prefix_pattern = self.pattern_input.text().strip()
        start_index = self.start_index_input.text().strip()
        start_index = int(start_index) if start_index.isdigit() else 1

        if not prefix_pattern:
            QMessageBox.warning(self, "Warning", "Please enter a prefix ")
            return

        renamer = FileRenamer(self.folder_path, prefix_pattern, start_index, self.smart_rename_checkbox.isChecked(), self.output_path)
        
        try:
            renamer.rename_files()
            self.log_text.setPlainText("\n".join(renamer.logs))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

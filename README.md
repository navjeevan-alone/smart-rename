# Smart Rename  

## Overview
**Smart Rename** is a Python application designed to facilitate the renaming of multiple files in a selected folder. With user-friendly features, it allows users to specify prefix patterns, start indices, and includes a "Smart Rename" option to avoid renaming files that already conform to specified naming patterns. The application also provides an optional output path for the renamed files.

## Features
- **Folder Selection:** Allows users to choose a folder containing the files to rename.
- **Output Path Selection:** Optional feature to set a destination folder for renamed files.
- **Prefix Pattern Input:** Users can specify a prefix pattern for the renamed files.
- **Start Index Input:** Allows users to define the starting index for renaming.
- **Smart Rename Option:** Automatically skips renaming for files that:
  - Already have the specified prefix.
  - Do not conform to common naming conventions (e.g., `img00xxx`).
- **File Counting:** Users can count the number of files in the selected directory.
- **Log Panel:** Displays logs of operations for better tracking.

## Installation
To run the Smart Rename application, ensure you have Python installed along with the following packages:
- PyQt5
- Any other dependencies specified in the `requirements.txt`

You can install the required packages using pip:

```bash
pip install PyQt5
```

## Usage
1. **Launch the Application:** Run the main Python script (`main.py`).
2. **Select Folder:**
   - Click the **"Select Folder"** button to choose the folder containing the files you want to rename.
3. **Optional Output Path:**
   - Click the **"Select Output Path (Optional)"** button to choose a destination for renamed files.
4. **Enter Prefix Pattern:**
   - Input a prefix pattern in the **"Enter Prefix Pattern"** field (e.g., `file_`).
5. **Set Start Index:**
   - Enter a starting index in the **"Start Index"** field (default is 1).
6. **Enable Smart Rename:**
   - Check the **"Smart Rename"** checkbox to activate this feature.
7. **Rename Files:**
   - Click the **"Rename Files"** button to execute the renaming process.
8. **Count Files:**
   - Click the **"Count Files"** button to display the number of files in the selected directory.
9. **View Logs:**
   - Check the **Logs** panel to see the details of the renaming operations and any skipped files.

## Code Structure
The application is organized into modules to ensure modularity and ease of maintenance. The key components include:
- **`main.py`**: The main entry point for the application.
- **`gui.py`**: Contains the user interface components and layout setup.
- **`styles.css`**: Defines the visual styling for the application.
- **`logger.py`**: Manages logging functionality to track application events and errors.

### Sample Code
Below is a snippet from the `gui.py` file showcasing how the layout is organized:

```python
# Import necessary modules
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, 
    QLabel, QPushButton, QLineEdit, QCheckBox, 
    QGroupBox, QTextEdit, QHBoxLayout
)
from PyQt5.QtGui import QFont

class FileRenamerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rename Genie")
        self.setGeometry(200, 200, 600, 400)
        # Set layout and widgets...

        # Example of folder selection layout
        folder_layout = QHBoxLayout()
        folder_layout.addWidget(self.folder_label)
        folder_layout.addWidget(self.select_folder_button)
        self.layout.addLayout(folder_layout)
```

## License
This project is open-source and available under the [MIT License](LICENSE).

## Conclusion
The **Smart Rename** application offers a simple and efficient way to manage file renaming with flexibility and ease of use. For further inquiries or contributions, feel free to contact the maintainer.
 
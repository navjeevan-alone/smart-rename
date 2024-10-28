import os
import logging
from file_operations import copy_files

class FileRenamer:
    def __init__(self, folder_path, prefix_pattern, start_index, smart_rename, output_path):
        self.folder_path = folder_path
        self.prefix_pattern = prefix_pattern
        self.start_index = start_index
        self.smart_rename = smart_rename
        self.output_path = output_path
        self.logs = []

    def rename_files(self):
        # Copy files to output path if specified
        if self.output_path:
            copy_files(self.folder_path, self.output_path)
            self.folder_path = self.output_path

        for count, filename in enumerate(os.listdir(self.folder_path), start=self.start_index):
            file_path = os.path.join(self.folder_path, filename)

            # Skip directories
            if os.path.isdir(file_path):
                continue

            # Smart rename checks
            if self.smart_rename and self.is_file_renamed(filename):
                logging.info(f"Skipping {filename} as it is already renamed.")
                continue

            file_extension = os.path.splitext(filename)[1]
            new_name = f"{self.prefix_pattern}{count}{file_extension}"
            new_path = os.path.join(self.folder_path, new_name)

            os.rename(file_path, new_path)
            self.logs.append(f"Renamed: {filename} -> {new_name}")
            logging.info(f"Renamed: {filename} -> {new_name}")

    def is_file_renamed(self, filename):
        standard_formats = ['img', 'photo', 'file']
        return any(filename.startswith(fmt) for fmt in standard_formats)

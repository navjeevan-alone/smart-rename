import os
import shutil
import logging

def count_files(folder_path):
    return sum([len(files) for r, d, files in os.walk(folder_path)])

def copy_files(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        logging.info(f"Created output directory: {dest_folder}")

    for filename in os.listdir(src_folder):
        file_path = os.path.join(src_folder, filename)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest_folder)
            logging.info(f"Copied: {filename} to {dest_folder}")

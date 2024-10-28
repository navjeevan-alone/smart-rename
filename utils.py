# Load styles from the CSS file
def load_stylesheet(filename):
    with open(filename, "r") as file:
        return file.read()

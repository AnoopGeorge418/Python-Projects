import pathlib
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def fetch_path():
    """This function helps to get the path that the user wants to organize and return it."""
    return input('Paste your directory path that you want to organize: ').strip()

def scan_folder_files(path):
    """This function helps to scan all the files and folders in the given path."""
    scan = pathlib.Path(path)
    files = []
    if not any(scan.iterdir()):
        print(f'There are no files or folders to be found in {path} path.. Check your File Explorer and try again!')
        return files
        
    for item in scan.iterdir():
        if item.is_dir():
            print(f'{item} - Folder')
        else:
            print(f'{item} - File')
            files.append(item)
    return files

def creating_folders(base_path):
    """This function helps to check if the folders exist in the given path. If not, creates folders."""
    FILE_CATEGORIES = {
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".tar.gz"],
        "Others": []
    }
    
    # Create directories for each file category
    for category in FILE_CATEGORIES.keys():
        category_path = pathlib.Path(base_path) / category
        if not category_path.exists():
            category_path.mkdir(parents=True)
            print(f"Created folder: {category_path}")
        else:
            print(f"Folder already exists: {category_path}")

    return FILE_CATEGORIES

def assign_files(base_path, files, FILE_CATEGORIES):
    """This function helps to assign files to respective folders."""
    for file in files:
        file_extension = file.suffix
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                dest_path = pathlib.Path(base_path) / category / file.name
                shutil.move(str(file), dest_path)
                print(f'Moved {file} to {dest_path}')
                moved = True
                break
        if not moved:
            dest_path = pathlib.Path(base_path) / "Others" / file.name
            shutil.move(str(file), dest_path)
            print(f'Moved {file} to {dest_path}')

class Watcher:
    """Class to watch for new files and reorganize them."""
    def __init__(self, directory, FILE_CATEGORIES):
        self.directory = directory
        self.FILE_CATEGORIES = FILE_CATEGORIES
        self.event_handler = Handler(self.directory, self.FILE_CATEGORIES)
        self.observer = Observer()

    def run(self):
        self.observer.schedule(self.event_handler, self.directory, recursive=True)
        self.observer.start()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    """Class to handle the events."""
    def __init__(self, directory, FILE_CATEGORIES):
        self.directory = directory
        self.FILE_CATEGORIES = FILE_CATEGORIES

    def on_modified(self, event):
        files = scan_folder_files(self.directory)
        assign_files(self.directory, files, self.FILE_CATEGORIES)

if __name__ == '__main__':
    base_path = fetch_path()
    FILE_CATEGORIES = creating_folders(base_path)
    files = scan_folder_files(base_path)
    assign_files(base_path, files, FILE_CATEGORIES)
    
    watcher = Watcher(base_path, FILE_CATEGORIES)
    watcher.run()
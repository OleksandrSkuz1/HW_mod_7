import sys
from pathlib import Path
import zipfile
import tarfile
import os
import shutil



CATEGORIES = {"Audio": [".mp3",],
              "Video": [".mp4"],
              "Fotos": [".jpg"],
              "Docs": [".rtf", ".txt", ".bmp", '.pdf'],
              "Arhives": [".zip", ".tar"]}
              
                

def get_categories(file:Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat                
    return "Other"  

def move_file(file: Path, category: str, root_dir: Path) -> None:
    
    target_dir = root_dir.joinpath(category)
    print(target_dir.exists())
    if not target_dir.exists():
        target_dir.mkdir()
        
    file.replace(target_dir.joinpath(file.name))      
    
          
def sort_folder(path:Path) -> None:
    
    for element in path.glob("**/*"):
        if element.is_file():
            category = get_categories(element)
            move_file(element, category, path)
            
     # Видаляємо порожні папки      
       
    for dir_path in path.glob('**/*'):
        if dir_path.is_dir() and not any(dir_path.iterdir()):
            dir_path.rmdir()        
            
            
# Функція для розпакування архівів та переміщення їх вмісту до папки "Arhives"

# def move_archives(file, destination_folder):
#     file_extension = file.suffix.lower()
#     if CATEGORIES == '.zip':
#         with zipfile.open(file, 'rb') as Arhives:
#             Arhives.extractall(destination_folder)

#     elif CATEGORIES == '.tar':
#         with tarfile.open(file, 'rb') as Arhives:
#             Arhives.extractall(destination_folder)


def extract_and_move_archives(file_path, destination_folder):
    file_extension = file_path.suffix.lower()
    if Arhives == '.zip':
        with zipfile.open(file_path, 'rb') as zip_ref:
            zip_ref.extractall(destination_folder)
            # Переносимо файли з архіву до папки 'archive_files'
            archive_files = destination_folder / 'archive_files'
            for item in zip_ref.namelist():
                item_path = archive_files / Path(item).name
                zip_ref.extract(item, archive_files)
                Path(destination_folder / item).replace(item_path)
    
       
    
# def move_archives(path:Path) -> None:
    
#     for element in path.joinpath("Arhives").glob("**/*"):
#         if element.is_file() and (element.suffix == ".zip"):
#             shutil.unpack_archive(path.joinpath(element.name), path.joinpath(element.stem))           
        # if element.is_file() and (element.suffix == ".tar"):
        #     shutil.unpack_archive(path.joinpath(element.name), path.joinpath(element.stem))    
                                            
def main() -> str:
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"
                
    if not path.exists():
        return "Folder dos not exists"
    
    sort_folder(path)
                
    return "All ok"

if __name__ == "__main__":
    print(main())
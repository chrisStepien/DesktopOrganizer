# Python program to organize files on the desktop into folders

# importing os module
from pathlib import Path

# importing shutil module
import shutil

# desktop path
origin_path = Path('C:/Users/chris/OneDrive/Desktop')
destination_path = Path('C:/Users/chris/OneDrive/Desktop')

def main():
    
   unsorted_files = sorting_path_files(origin_path)
   print(unsorted_files) 
    
def sorting_path_files(directory: Path):     
    
    file_list = []
    
    for item in directory.iterdir():
        if item.is_file():
            
            file_list.append(item)
    
    return file_list
    
# create folders function

# import files into folders    

if __name__ == "__main__":
    main()    
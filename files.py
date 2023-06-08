# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line
import os
from zipfile import ZipFile as zf


#Option 1, I have to use 'files\cache'.
#Visual Code sees C:\Users\nienk\Documents\Administratie\Data Analysis\WINC Data Analytics with Python\Winc as the directory, so does not include files
def clean_cache():
    if os.path.exists('files\cache') == False:
        os.makedirs('files\cache')   
    elif os.path.exists('files\cache'):
        file_list = os.listdir('files\cache')
        for file in file_list:
            os.remove(f'files\cache\{file}')

#Option 2, I still have to use files/cache, but in case the directory I am working in is not clear:
def clean_cache():
    current_path = os.getcwd()
    full_path = os.path.join(current_path, "files\cache")
    if os.path.exists(full_path) == False:
        os.makedirs(full_path)   
    elif os.path.exists(full_path):
        file_list = os.listdir(full_path)
        for file in file_list:
            os.remove(os.path.join(full_path, file))

#Cache-zip repeats the previous code to create/empty the cache folder. It then unpack the zip_file into cache. 
#Again, I have to deine files\cache for it to work, just 'cache', without files, does not work. [Errno 2] No such file or directory: 'data.zip'
def cache_zip(zip_file_path, cache_dir_path):
    if os.path.exists('files\cache') == False:
        os.makedirs('files\cache')   
    elif os.path.exists('files\cache'):
        file_list = os.listdir('files\cache')
        for file in file_list:
            os.remove(f'files\cache\{file}')   
    with zf(zip_file_path, "r") as f:
        f.extractall(cache_dir_path)

#creates a list of files in the cache, uses absolute path.
def cached_files():
    list_absolute = []
    current_path = os.getcwd()
    full_path = os.path.join(current_path, "files\cache")
    file_list = os.listdir(full_path)
    for file in file_list:
        absolute_file = os.path.join(full_path, f"{file}")
        list_absolute.append(absolute_file)
    return list_absolute
    
#In order to seperate the password, which is in the middle of the file, use split.
#Split will add the seperated parts in list.
#You can do a second split on the part of the list that is relevant.
def find_password(list_absolute = cached_files()):
    for file_path in list_absolute:
        with open(file_path, 'r') as file:
            content = file.read() 
            if "password" in content:
                seperate_password = content.split(" ")[1]
                final_result = seperate_password.split("\n")[0]
                return final_result

print(clean_cache())
print(cache_zip("files\data.zip", "files\cache"))
print(cached_files())
print(find_password())

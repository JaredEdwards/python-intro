import os

def rename_files():
    #read
    path = "/Users/Jaredsfiles/Desktop/Udacity/python/prank/"
    file_list = os.listdir(path)
    print(file_list)

    #rename files
    
    for file_name in file_list:
        file_name = os.rename(path+file_name, path+file_name.translate(None,"0123456789"))
        print(file_list)
    
rename_files()

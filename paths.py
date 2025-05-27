import os
from config import ydl_opts, downloads

def final_destination():
    '''
    Ask user for download final file destination
    Default is downloads folder
    '''
    user_destination = ""

    destination_choice = input("Default download location is Downloads folder, Proceed? (y/n): ").strip().lower()
    make_new_folder = input("Would you like to create a new folder for this download? (y/n): ").strip().lower()
      
    if destination_choice == "y":
        print(f"Downloading to {downloads}...")
        user_destination = downloads
    elif destination_choice == "n":
        user_destination = input("Where would you like to save your file?: Ex: /Users/....\n(Exclude new folder name)\n").strip()
        print(f'Downloading to {user_destination}...')
        if not os.path.exists(user_destination):
            print("Directory does not exist. Please enter a valid path.")
            exit()
    ##### Create new folder if user wants to
    if make_new_folder == "y":
        new_folder_name = input("Enter name for new folder: ").strip()
        user_destination = os.path.join(downloads, new_folder_name)
        if not os.path.exists(user_destination):
            os.makedirs(user_destination)
            print(f"New folder created: {user_destination}")
        else:
            print(f"Folder already exists: {user_destination}")

    if not os.path.exists(user_destination):
        print("Directory does not exist. Please enter a valid path.")
        exit()

    full_file_name = os.path.join(user_destination, "%(title)s.%(ext)s")
    ydl_opts.update({'outtmpl': full_file_name})

    return user_destination
import os
from config import ydl_opts, downloads

def final_destination():
    '''
    Ask user for download final file destination
    Default is downloads folder
    '''

    destination_choice = input("Default download location is Downloads folder, Proceed? (y/n): ").strip().lower()

    if destination_choice == "y":
        print(f"Downloading to {downloads}...")
        print("=" * 50)
        user_destination = downloads
    elif destination_choice == "n":
        user_destination = input("Where would you like to save your file?: ")
        print(f'Downloading to {user_destination}...')
        print("=" * 50)

    if not os.path.exists(user_destination):
        print("Directory does not exist. Please enter a valid path.")
        exit()

    full_file_name = os.path.join(user_destination, "%(title)s.%(ext)s")
    ydl_opts.update({'outtmpl': full_file_name})

    return user_destination
from config import ydl_opts, downloads

def initial_choice():
    '''Ask user if they want to download a playlist or a video
    return selected option, then run the appropriate function
    '''
    choice = input("Do you want to download a YouTube playlist or a single video? (p/v): ").strip().lower()
    playlist_or_video = ''
    if choice == "p":
        return get_playlist_input
    elif choice == "v":
        return get_user_input
    else:
        print("Invalid choice. Please enter 'p' for playlist or 'v' for video.")
        exit()



def get_playlist_input():
    '''Get user input for playlist URL
    '''
    url = ""
    file_type = ""
    url = input("Enter a YouTube playlist URL: ").strip()
    file_choice = input("Do you want to download the playlist as video or audio? (v/a): ").strip().lower()
    if file_choice == "v":
        file_type = "mp4"
        ydl_opts.update({'merge_output_format': 'mp4', 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',})
    elif file_choice == "a":
        file_type = "mp3"
        ydl_opts.update({
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'extractaudio': True,
        'keepvideo': False,
        'format': 'bestaudio/best',})
    else:
        print("Invalid choice. Please enter 'v' for video or 'a' for audio.")
        exit()

    return url, file_type



def get_user_input():
    '''Get user input for video/audio URL and file type
    Ask for download location.
    '''
    url = ""
    file_type = ""
    choice = input("Do you want to download a YouTube video or an audio? (v/a): ").strip().lower()

    if choice == "v":
        url = input("Enter a YouTube video URL(MP4): ").strip()
        file_type = "mp4"
        ydl_opts.update({'merge_output_format': 'mp4', 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',})
    elif choice == "a":
        url = input("Enter a YouTube audio URL(MP3): ").strip()
        file_type = "mp3"
        ydl_opts.update({
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'extractaudio': True,
        'keepvideo': False,
        'format': 'bestaudio/best',})
    else:
        print("Invalid choice. Please enter 'v' for video or 'a' for audio.")
        exit()
    return url, file_type
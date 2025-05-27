from config import ydl_opts, downloads


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
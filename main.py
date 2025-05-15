from downloader import download_video
from config import ydl_opts, downloads
from inputs import get_user_input
from paths import final_destination

def main():
    print("YouTube Video Downloader----YouTube Audio Extractor")
    print("========================================")
    print("This script downloads videos or audio using yt-dlp, into mp3 or mp4 format. (YouTube, TikTok, etc.)")

    user_url, file_type = get_user_input()
    final_destination()
    download_video(user_url,file_type)

if __name__ == "__main__":
    main()

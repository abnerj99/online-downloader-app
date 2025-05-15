
import yt_dlp
import os
from config import ydl_opts, downloads

def download_video(url,file_type):
    '''
    Requires yt-dlp and ffmpeg:
    Download video or extract audio from YouTube using yt-dlp
    Converted to mp3 or mp4 with ffmpeg
    Fetch Video Data then proceed with download
    '''

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url, download=False)
        print(f"Title: {video_info['title']}")
        print(f"Duration: {video_info['duration']} seconds")
        print(f'View Count: {video_info['view_count']}')
        try:
            # Download the video
            print(f"One Moment...")
            ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            print(f"Download failed: {e}")
        except yt_dlp.utils.ExtractorError as e:
            print(f"Extractor error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        ## Get File Size

        final_file = os.path.join(ydl.prepare_filename(video_info))
        final_file = final_file.replace('.webm', f'.{file_type}')

        if os.path.exists(final_file):
            file_size = os.path.getsize(final_file)
            print(f"Success. Downloaded file size: {file_size / 1_000_000:.2f} MB")  # Display in MB
        else:
            print(f"File not found: {final_file}")

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
            
        # Display video information
        minutes, seconds = divmod(video_info['duration'], 60)
        print("----------------------")
        print(f"Title: {video_info['title']}")
        print(f"Duration: {minutes} minutes and {seconds} seconds")
        print(f'View Count: {video_info['view_count']}')
        ## Get File Size

        file_path = os.path.join(ydl.prepare_filename(video_info))
        #### Always ensure file has correct extension
        final_file = file_path.rsplit('.', 1)[0] + f'.{file_type}'

        if os.path.exists(final_file):
            file_size = os.path.getsize(final_file)
            print(f"Success. Downloaded file size: {file_size / 1_000_000:.2f} MB")  # Display in MB
        else:
            print(f"File not found: {final_file}")
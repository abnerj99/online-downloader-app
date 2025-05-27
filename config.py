import yt_dlp
import os
from pathlib import Path

# Global variables
# Set default download location to the user's Downloads folder

home = Path.home()
downloads = home / "Downloads"
ydl_opts = {
        'quiet': False, #Display downloading info
        'no_warnings': True,
        'noplaylist': True, #No playlist is the default option, single video
    }

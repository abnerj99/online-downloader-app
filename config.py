import yt_dlp
import os
from pathlib import Path

# Global variables
# Set the default download location to the user's Downloads folder

home = Path.home()
downloads = home / "Downloads"
ydl_opts = {
        'quiet': False, #Display downloading info
        'noplaylist': True, #No playlist, single video
    }

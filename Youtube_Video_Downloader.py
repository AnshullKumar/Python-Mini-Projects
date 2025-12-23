

# ------------------------
# Youtube Video Downloader
# ------------------------

# Creating a simple Youtube video downloader ...
# For personal use, where Ill create a Terminal function to call this script ...
# And save it in the .ps1 folder to have quick access ...
# So that I can download any youtube video by just providing the link, for my ease of use ...
# Suppose, I call this in my terminal ...
# DownloadYT "<youtube link>"
# It will download the youtube video in the provided directory ...
# Which ill be able to watch later (offline) ...


from pytubefix import YouTube
import sys

if len(sys.argv) < 2:
    print("Usage: python test.py <youtube_link>")
    sys.exit(1)

link = sys.argv[1]
yt = YouTube(link)

print("Title :", yt.title)
print("Views :", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("X:\Downloads\Youtube Downloads")  # Path directed to where you would like to store the downloaded video...

print("Downloaded Successfully into the specified directory...")


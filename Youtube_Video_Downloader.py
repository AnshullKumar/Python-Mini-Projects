

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


from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)


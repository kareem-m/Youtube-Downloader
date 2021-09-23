"""A file with which you can download any video or playlist from YouTube in any quality you want
and the ability to download in mp3 or mp4 extension.
All you have to do is just put the link to the video or playlist"""
import ctypes
from os import startfile
from pytube import YouTube
from pytube import Playlist

# Add The Title Of File
ctypes.windll.kernel32.SetConsoleTitleW("Youtube Downloader")

# Add The Title To App
print(" Youtube Downloader ".center(40, "-"))
print("")

# Get The Video Link
yt_link = input("Enter The Video or Playlist Link Please: ")
if yt_link == "":
    print("The link is incorrect. Please try again")

# Get The Type Of Video
yt_split = yt_link.split("?", 1)
if yt_split[0] == "https://www.youtube.com/playlist":
    yt_type = "playlist"
elif yt_split[0] == "https://www.youtube.com/watch":
    yt_type = "video"

# Get The Path
video_path = input("Enter the path where you want to download the video: ")
if video_path == "":
    print("The video path is incorrect. Please try again")

# Download The Video
video_type = input("Choose the type of video you want (144p | 720p | mp3): ")

if yt_type == "video":
    yt = YouTube(yt_link)
    while True:
        if video_type == "144p":
            yt.streams.get_lowest_resolution().download(output_path=f"{video_path}")

        elif video_type == "720p":
            yt.streams.get_highest_resolution().download(output_path=f"{video_path}")

        elif video_type == "mp3":
            yt.streams.get_by_itag(251).download(output_path=f"{video_path}")

        else:
            print("The video type you selected is incorrect. Please try again")
            break

        # Add The Progress callback
        def progress_callback():
            """function allowed to add progress callback"""
            i = 0
            while i <= 10:
                print("#", end=" ")
                i+=1
        yt.register_on_progress_callback(progress_callback())

        # print successful message
        def download_done():
            """function allowed to add message when the video downloaded"""
            print("\nSuccessful Download")
            if video_type == "144p" or video_type == "720p":
                startfile(f"{yt.title}.mp4")
            elif video_type == "mp3":
                startfile(f"{yt.title}.webm")
        yt.register_on_complete_callback(download_done())
        break
elif yt_type == "playlist":
    pl = Playlist(yt_link)
    for video in pl.videos:
        while True:
            if video_type == "144p":
                video.streams.get_lowest_resolution().download(output_path=f"{video_path}")

            elif video_type == "720p":
                video.streams.get_highest_resolution().download(output_path=f"{video_path}")

            elif video_type == "mp3":
                video.streams.get_by_itag(251).download(output_path=f"{video_path}")

            else:
                print("The video type you selected is incorrect. Please try again")
                break

            # Add The Progress callback
            def progress_callback():
                """function allowed to add progress callback"""
                i = 0
                while i <= 10:
                    print("#", end=" ")
                    i+=1
            video.register_on_progress_callback(progress_callback())

            # print successful message
            def download_done():
                """function allowed to add message when the video downloaded"""
                print("\nSuccessful Download")
                if video_type == "144p" or video_type == "720p":
                    startfile(f"{video.title}.mp4")
                elif video_type == "mp3":
                    startfile(f"{video.title}.webm")
            video.register_on_complete_callback(download_done())
            break

# To keep the file always open
input("")

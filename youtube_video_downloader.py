#Difficulty: Meduim
#What's the point a python script to download youtube videos
#################################################################################################
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_vid(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res = streams.get_highest_resolution()
        highest_res.download(output_path=save_path)
        print("Video downloaded successfully")
    except Exception as e:
        print(e)

def select_path():
    root = tk.Tk()
    root.withdraw()  
    save_path = filedialog.askdirectory()
    return save_path

if __name__ == "__main__":
    save_path = select_path()

    while True:
        url = input('Could you please provide me with the YouTube URL (or press q to quit) :')

        if url == 'q':
            break
        else:
            download_vid(url, save_path)

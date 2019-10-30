import os
import sys
import colorama
from colorama import Fore
import pyfiglet
import youtube_dl


def main():
    music = input(Fore.CYAN + "> Enter url: ")
    while not music:
        print(Fore.RED + "> Not entered")
        music = input(Fore.CYAN + "> Enter url: ")
    save_dir = "./music/"
    outtmpl = "%(title)s.%(ext)s"

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    ydl_opts = {
        "outtmpl": save_dir + outtmpl,
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print(Fore.WHITE + "> Downloading ...")
        ydl.download([music])
        print(Fore.GREEN + "\n> Download Complete")

if __name__ == "__main__":
    figlet = pyfiglet.figlet_format("YDL Music")
    print(Fore.LIGHTRED_EX + figlet)
    print("Youtube, SoundCloud, Bandcamp, etc...\n")
    try: 
        main()
    except KeyboardInterrupt:
        print(Fore.LIGHTGREEN_EX + "\n> Exit program")
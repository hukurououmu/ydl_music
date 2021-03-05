import os
import sys
import pyfiglet
import youtube_dl
from colorama import Fore

save_dir = "./music/"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
outtmpl = "%(title)s.%(ext)s"

ydl_opts = {
    "outtmpl": save_dir + outtmpl,
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
}


def download(url):
    try:
        print("> Downloading ...")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(">" + Fore.LIGHTGREEN_EX + " Download complete!" + Fore.RESET)
    except Exception as e:
        raise e


def main():
    try:
        url = input("\n> Enter url : ")
        while not url:
            print(">" + Fore.RED + " Not entered" + Fore.RESET)
            url = input("> Enter url : ")
        download(url)
    except youtube_dl.utils.DownloadError:
        print(">" + Fore.RED + " The URL is incorrect or does not exist. Please enter the correct URL." + Fore.RESET)




if __name__ == "__main__":
    figlet = pyfiglet.figlet_format("YDL Music")
    print(Fore.LIGHTRED_EX + figlet)
    print("・Youtube, SoundCloud, Bandcamp, etc...\n")
    print("・Ctrl + C to exit the program")
    print("---------------------------------------------\n" + Fore.RESET)
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\n>" + Fore.GREEN + " Exit program")
        sys.exit()

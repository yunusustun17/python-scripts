from classes.color import colors
import os
import pyfiglet
import codecs
import subprocess
from pytube.cli import on_progress
from pytube import YouTube, Playlist


class youtubeDownloader:
    def __init__(self):
        self.mime = None
        self.link = None
        self.yt = None
        self.destination = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        while True:
            self.printMime()
            self.printUsage()

    # returning input value
    def enterInput(self):
        return input("""
    Enter your input:
    -> """)

    # downloading media from mime type
    def download(self):
        for i in range(17):
            try:
                self.yt = YouTube(self.link, on_progress_callback=on_progress)
                print(f"\n\n{self.yt.title} downloading..")
                if self.mime == "1":
                    self.yt.streams.filter(only_audio=True).order_by("abr").desc().first().download(self.destination)
                    os.chdir(self.destination)
                    oldest_file = max(os.listdir(), key=os.path.getctime)
                    try:
                        os.rename(oldest_file, f"{self.yt.title}.mp3")
                    except:
                        pass
                    break
                elif self.mime == "2":
                    self.yt.streams.get_highest_resolution().download(self.destination)
                    print()
                    break
            except:
                if i == 16:
                    print(f"{colors.FAIL}download failed{colors.ENDC}")

    def playlistDownload(self):
        playlist = Playlist(self.link).video_urls
        for j in playlist:
            self.link = j
            self.download()

    def fileDownload(self):
        file = codecs.open(self.link, "r+")
        txt = file.readlines()
        file.close()
        txt = list(filter(None, txt))
        for i, j in enumerate(txt):
            txt[i] = txt[i].replace("\n", "")
            txt[i] = txt[i].replace("\r", "")
        for j in txt:
            self.link = j
            self.download()

    def printFiglet(self):
        subprocess.call(["cls"], shell=True)
        figlet = pyfiglet.figlet_format("Youtube Downloader")
        print(f"""
            {colors.OKGREEN}{figlet}{colors.ENDC}""")

    def printMime(self):
        self.printFiglet()
        print(f"""
        [1] music
        [2] video
    
        [0] exit""")

        while True:
            self.mime = self.enterInput()
            if self.mime == "0":
                exit("""
    see you soon :)
                    """)
            elif self.mime == "1" or self.mime == "2":
                break
            else:
                print(f"""
    {colors.FAIL}invalid input. check your input and try again{colors.ENDC}""")

    def printUsage(self):
        self.printFiglet()
        print(f"""
        USAGE:
        -> C:\\Users\\Desktop\\qwerty.txt
        -> https://www.youtube.com/watch?v=qwerty
        -> https://www.youtube.com/playlist?list=qwerty
    """)
        while True:
            self.link = self.enterInput()
            if os.path.isfile(self.link):
                self.fileDownload()
                break
            else:
                if 'watch' in self.link:
                    self.download()
                    break
                elif 'playlist' in self.link:
                    self.playlistDownload()
                    break
                else:
                    print(f"""
    {colors.FAIL}invalid input. check your input and try again{colors.ENDC}""")

        input(f"""
        
    {colors.OKGREEN}press ENTER to exit..{colors.ENDC}""")

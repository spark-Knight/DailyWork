# YaHooo!!!
**I have made a Video downloader in python**

It's very simple to understand

First it Takes input from InputName

_InputName = str(input())_

After that it find the video on youtube
and get high resolution fro us

_videoName = kit.playonyt(InputName) 
youtube = pytube.YouTube(videoName)  
video = youtube.streams.get_highest_resolution()_

After video statement It starts the downloading.....

_video.download('C:\\Users\\dna83\\OneDrive\\Desktop\\Your dad\\download files')_
Give your Download path to where to save the downloaded video




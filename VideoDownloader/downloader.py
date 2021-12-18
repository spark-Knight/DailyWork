import pywhatkit as kit
import pytube 
import os


print("Name of video You want to Download")
# Here we input video name  
InputName = str(input())
videoName = kit.playonyt(InputName) 
# this is statement close chrome beacause it's open the video on chrome
os.system("TASKKILL /F /im chrome.exe ")   
youtube = pytube.YouTube(videoName)  
# It's give good resolution of video which want
video = youtube.streams.get_highest_resolution()  
print("Downloading video...")
video.download('C:\\Users\\dna83\\OneDrive\\Desktop\\Your dad\\download files')  
print("video downloaded successfully")



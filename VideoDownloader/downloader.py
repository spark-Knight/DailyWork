import pywhatkit as kit
import pytube 
import keyboard as key


print("Name of video You want to Download")
# Here we input video name  
InputName = str(input())
videoName = kit.playonyt(InputName) 
# this is statement close chrome beacause it's open the video on chrome
youtube = pytube.YouTube(videoName)  
key.press_and_release("Alt+F4")
# It's give good resolution of video which want
video = youtube.streams.get_highest_resolution()  
print("Downloading video...")
video.download('C:\\Users\\dna83\\OneDrive\\Desktop\\Your dad\\download files')  
print("video downloaded successfully")



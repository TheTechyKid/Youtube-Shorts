from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip, ImageClip, CompositeVideoClip, CompositeAudioClip, afx
from reddit_info import create_file
from random import randint

create_file()

video_lists = [
    r"C:\Users\name\Desktop\python books\critters\videos\Minecraft Parkor.mp4",
    r"C:\Users\name\Desktop\python books\critters\videos\Minecraft Parkor 2.mp4"
]

PATH_to_title = r"C:\Users\name\Desktop\python books\critters\titletop.png"
PATH_to_reddit = r"C:/Users/name/Desktop/python books/critters/reddit.mp3"
PATH_to_bgmusic = r"C:\Users\name\Desktop\python books\critters\videos\🍬 Chill Vlog Happy Lofi Beat No Copyright Free Background Music for Video Marshmallow by Lukrembo (128 kbps) (Snap2s.com).mp3"

ran_data = {
    "video":r"C:\Users\name\Desktop\python books\critters\videos\Minecraft3.mp4", #choice(video_lists)
    "seconds":randint(0, 476)
}

speach = AudioFileClip(PATH_to_reddit)
duration_in_seconds = speach.duration
music = AudioFileClip(PATH_to_bgmusic)
gmusic = CompositeAudioClip([music]).subclip(0, duration_in_seconds)
bgmusic = gmusic.subclip(0, duration_in_seconds).fx(afx.volumex, 0.1)

duration = bgmusic.duration
chunk_length = duration_in_seconds
chunks = []

clip1 = VideoFileClip(ran_data["video"]).subclip(ran_data["seconds"], duration_in_seconds+ran_data["seconds"])
image = ImageClip(PATH_to_title)

resized_image = image.resize(width=1080)

resized_image = resized_image.set_duration(duration_in_seconds)

combined = concatenate_videoclips([clip1])

speach.volumex(2)
bgmusic.volumex(0.3)

new_audioclip = CompositeAudioClip([speach, bgmusic])
final = CompositeVideoClip([combined, resized_image.set_position(("center", 0))])

final = final.set_audio(new_audioclip)
final.write_videofile("video.mp4", codec='libx264')
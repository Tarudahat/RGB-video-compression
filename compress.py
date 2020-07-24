from moviepy.editor import VideoFileClip, ImageSequenceClip, AudioFileClip
import numpy
import os
import shutil
import sys
import pathlib
import time
import math
from PIL import Image, ImageOps, ImageEnhance

output_array = []
output_array_ = []
print("Enter input video name:")
in_ = input()
video = VideoFileClip(in_)
path = os.path.normpath("./frames/of")
output_array_path = os.path.normpath("./frames")

frame_path = os.path.normpath("./frames")

frame_count = math.ceil(video.duration/(1/video.fps))

frame_time_delay = 1.0/video.fps

path__ = os.path.normpath("./frames/f")
print("Working on it,\nplease be patient...")

i = 0
i1 = 1
i2 = 2
i3 = 0
done = False

while not done:
    img = Image.fromarray(video.get_frame(
        frame_time_delay*i)).convert("L")  # 0,003333...|0.01998
    img1 = Image.fromarray(video.get_frame(
        frame_time_delay*i1)).convert("L")  # 0,00666...
    img2 = Image.fromarray(video.get_frame(
        frame_time_delay*i2)).convert("L")  # 0,00999...S

    img = ImageOps.colorize(img, black="black", white=(255, 0, 0))
    img1 = ImageOps.colorize(img1, black="black", white=(0, 255, 0))
    img2 = ImageOps.colorize(img2, black="black", white=(0, 0, 255))

    r = img.getchannel("R")
    g = img1.getchannel("G")
    b = img2.getchannel("B")

    img3 = Image.merge("RGB", (r, g, b))

    img3.save(path+str(i3)+".jpg", "JPEG")

    output_array_.append(path+str(i3)+".jpg")

    img.close()
    img1.close()
    img2.close()
    img3.close()

    i += 3
    i1 += 3
    i2 += 3
    i3 += 1

    if i3 == frame_count-1 or i >= frame_count or i1 >= frame_count or i2 >= frame_count:
        done = True

output_video = ImageSequenceClip(
    output_array_, fps=video.fps, load_images=False)

output_video.duration = video.duration/3

output_video.audio = video.audio
output_video.write_videofile("Compressed.mp4", fps=video.fps)

shutil.rmtree(output_array_path)
os.mkdir("frames")

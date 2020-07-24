from moviepy.editor import VideoFileClip, ImageSequenceClip, AudioFileClip
import numpy
import os
import shutil
import sys
import pathlib
import time
import math
from PIL import Image, ImageOps, ImageEnhance

print("Enter input video name:")
in_ = input()

video = VideoFileClip(in_)

path = os.path.normpath("./frames/of")
output_array_path = os.path.normpath("./frames")
frame_count = math.ceil(video.duration/(1/video.fps))

frame_time_delay = 1.0/video.fps


def makebw(image_):
    image_ = ImageOps.colorize(image_.convert(
        "L"), black="black", white="white")
    ce = ImageEnhance.Brightness(image_)
    image_ = ce.enhance(1.8)


output_array_ = []
print("Working on it,\nplease be patient...")

i = 0
i1 = 1
i2 = 2
i3 = 1
done = False

while not done:
    img = \
        Image.fromarray(
            video.get_frame(frame_time_delay*i3)
        ) \
        .convert("RGB")  # 0,003333...|0.01998
    r, g, b = img.split()

    img1 = Image.merge("RGB", (r, r, r))
    img2 = Image.merge("RGB", (g, g, g))
    img3 = Image.merge("RGB", (b, b, b))

    makebw(img1)
    makebw(img2)
    makebw(img3)

    img1.save(path+str(i)+".jpg", "JPEG")
    img2.save(path+str(i1)+".jpg", "JPEG")
    img3.save(path+str(i2)+".jpg", "JPEG")

    output_array_.append(path+str(i)+".jpg")
    output_array_.append(path+str(i1)+".jpg")
    output_array_.append(path+str(i2)+".jpg")

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

output_video.duration = video.duration

output_video.audio = video.audio
output_video.write_videofile("UnCompressed.mp4", fps=video.fps)

shutil.rmtree(output_array_path)
os.mkdir("frames")

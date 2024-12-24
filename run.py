import os

print("generating frames...")
os.system("python video_to_frames.py")
run = input("run? y/n")
if run == "y":
    os.system("python render.py")

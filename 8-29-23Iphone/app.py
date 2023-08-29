

#Author: Anthony Lee



import os
import subprocess

#the system level packages not related to python env are:
# ffmpeg # for extracting frames and creating time lapse
# mplayer
#

# Function to extract frames from the input video
def extract_frames(input_video, output_directory, frame_rate):
    os.makedirs(output_directory, exist_ok=True)
    subprocess.run(['ffmpeg', '-i', input_video, '-vf', f'fps={frame_rate}', f'{output_directory}/frame%04d.png'])

# Function to create the time-lapse video
def create_time_lapse(input_directory, output_video, frame_rate):
    subprocess.run(['ffmpeg', '-framerate', str(frame_rate), '-i', f'{input_directory}/frame%04d.png',
                    '-c:v', 'libx264', '-r', str(frame_rate), '-pix_fmt', 'yuv420p', output_video])

def main():
    input_video = 'my_video-8.mp4'
    output_frame_directory = 'output_frames'
    output_timelapse_video = 'output_timelapse.mp4'
    frame_rate = 1  

    install_packages()
    extract_frames(input_video, output_frame_directory, frame_rate)
    create_time_lapse(output_frame_directory, output_timelapse_video, frame_rate)

if __name__ == "__main__":
    main()

#Copiadissimo

import os
import sys
from moviepy.editor import VideoFileClip
from pydub import AudioSegment


def converter_to_wav(file, output_ext="wav"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""

    filename, ext = os.path.splitext(file)
    if(ext=='.mp4'):
        clip = VideoFileClip(file)
        clip.audio.write_audiofile(f"{filename}.{output_ext}")
    elif(ext=='.mp3'):
        sound = AudioSegment.from_mp3(file)
        sound.export(filename, format="wav") 


if __name__ == "__main__":
    vf = sys.argv[1]
    converter_to_wav(vf)
#!/usr/bin/env python3

import sys
import moviepy.editor as mpy


# Exemple:
# ./test.py /Users/vincent/Projets/exploits-editor-server/scripts/videos/king_george_outback_720.mp4 /tmp/toto_123.mp4

if len(sys.argv) < 3:
        print('Missing INFILE and OUTFILE parameters. Aborting.')
        quit()



clips = []

clip = mpy.VideoFileClip(sys.argv[1]).subclip(10.0, 12.0)
clips.append(clip)

mpy_video = mpy.concatenate_videoclips(clips)


def progress_callback(p: float):
    print(f"======= {p} =======")


mpy_video.write_videofile(sys.argv[2], progress_callback=progress_callback)


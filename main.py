#!/usr/bin/env python3
import argparse
import os
import sys
import yt_dlp


def progress(d):
    if d["status"] == "downloading":
        print(f"\r{d.get('_percent_str', '')} {d.get('_speed_str', '')}", end="", flush=True)
    elif d["status"] == "finished":
        print(f"\rDone: {d['filename']}")


parser = argparse.ArgumentParser()
parser.add_argument("url", help="YouTube video or playlist URL")
parser.add_argument("-d", "--dir", default=".", help="Target directory")
args = parser.parse_args()

opts = {
    "format": "best",
    "outtmpl": os.path.join(args.dir, "%(title)s.%(ext)s"),
    "progress_hooks": [progress],
}

try:
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([args.url])
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

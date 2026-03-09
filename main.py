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


parser = argparse.ArgumentParser(
    description="Download YouTube videos or playlists",
)
parser.add_argument("url", help="YouTube video or playlist URL")
parser.add_argument("-d", "--dir", default=".", help="Target directory")
parser.add_argument(
    "-f", "--format", default="best",
    help="Video format: best (default), bestvideo, worst, mp4, webm, or format code (e.g. 'bestvideo+bestaudio/best')"
)
args = parser.parse_args()

opts = {
    "format": args.format,
    "outtmpl": os.path.join(args.dir, "%(title)s.%(ext)s"),
    "progress_hooks": [progress],
}

try:
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([args.url])
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

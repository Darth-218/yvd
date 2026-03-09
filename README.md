# yt-vid-dl

Simple YouTube video/playlist downloader CLI.

## Usage

```bash
python main.py "https://youtube.com/watch?v=..."
python main.py "https://youtube.com/playlist?list=..." -d ~/Videos
python main.py "https://youtube.com/watch?v=..." -f mp4
```

## Options

- `-d, --dir` : Target directory (default: current directory)
- `-f, --format` : Video format (default: best)
  - `best` - best quality (default)
  - `worst` - lowest quality
  - `mp4`, `webm` - specific container
  - `bestvideo+bestaudio/best` - combined format

## Installation

### NixOS
```bash
nix-shell --run "python main.py <url>"
```

### Other
```bash
pip install yt-dlp
python main.py <url>
```

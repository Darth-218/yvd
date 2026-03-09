# yvd

Simple YouTube video/playlist downloader CLI.

## Usage

```bash
python main.py "https://youtube.com/watch?v=..."
python main.py "https://youtube.com/playlist?list=..." -d ~/Videos
```

## Options

- `-d, --dir` : Target directory (default: current directory)

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

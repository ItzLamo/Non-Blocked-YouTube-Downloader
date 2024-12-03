import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import subprocess

#########################################################################

def download_with_pytube(url, save_path):
    """Download YouTube video using pytube."""
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        highest_res_stream.download(output_path=save_path)
        messagebox.showinfo("Success", f"Video '{yt.title}' downloaded successfully to {save_path}")
    except Exception as e:
        print(f"pytube error: {e}")
        raise

def download_with_ytdlp(url, save_path):
    """Download YouTube video using yt-dlp."""
    try:
        command = [
            "yt-dlp",
            url,
            "-o", os.path.join(save_path, "%(title)s.%(ext)s"),
            "--format", "mp4"
        ]
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", f"Video downloaded successfully to {save_path}")
    except subprocess.CalledProcessError as e:
        print(f"yt-dlp error: {e}")
        messagebox.showerror("Error", f"An error occurred with yt-dlp: {e}")

def open_file_dialog():
    """Open folder selection dialog."""
    folder = filedialog.askdirectory(title="Select Download Folder")
    if folder:
        return folder
    else:
        messagebox.showwarning("Warning", "No folder selected.")
        return None

def main():
    """Main function to download video."""
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter the YouTube URL: ").strip()
    if not video_url:
        print("Invalid URL. Exiting.")
        return

    save_dir = open_file_dialog()
    if not save_dir:
        return

    try:
        print("Trying to download with pytube...")
        download_with_pytube(video_url, save_dir)
    except Exception:
        print("pytube failed. Falling back to yt-dlp...")
        download_with_ytdlp(video_url, save_dir)

if __name__ == "__main__":
    main()
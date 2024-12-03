# Non-Blocked-YouTube-Downloader
This Python script allows you to download YouTube videos using two different methods: pytube and yt-dlp. It features a simple graphical interface for folder selection and provides feedback messages during the download process.

Features:
YouTube Video Downloading: The script can download videos in MP4 format with the highest resolution available.
Two Download Methods: It first attempts to use pytube, and if that fails, it falls back to using yt-dlp as an alternative.
Graphical Folder Selection: The user can easily select the download location through a folder dialog box using Tkinter.
Error Handling: The script provides informative error and success messages using message boxes from Tkinter.
How It Works:
User Input: The user provides the YouTube URL via the terminal.
Folder Selection: A folder dialog allows the user to select the destination folder for the downloaded video.
Video Download: The script attempts to download the video using pytube. If that fails, it uses yt-dlp to download the video instead.
Notifications: The script shows success or error messages via pop-up message boxes.
Requirements:
pytube: A Python library for downloading YouTube videos.
yt-dlp: A command-line tool to download videos from YouTube and other websites (used as a fallback method).
Tkinter: A GUI library for creating simple desktop applications (used for the folder dialog and message boxes).
Installation:
To install the necessary libraries, run the following commands:
Run the bash script:-
pip install pytube yt-dlp

Usage:
Run the script.
Enter the YouTube URL when prompted in the terminal.
Select the destination folder using the file dialog.
Wait for the download to complete, and check the selected folder for the video.
This script is useful for those who want a simple, reliable way to download YouTube videos with the flexibility of two downloading methods.

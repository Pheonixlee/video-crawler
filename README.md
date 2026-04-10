# video-crawler
"First time learning m3u8 parsing!
For those who don't know what this is — check the referer field in the headers section of the code to see which website this is for.
How to run it:
First, run video_crawler.py. You can do this either through PyCharm, or by pressing Win+R to open CMD, navigating to your download path with cd path, then typing python video_crawler.py.
After running, a directory will be created containing 1,370 .ts files.
To merge them into one video:
You'll need to modify the code first. Run create_filenames.py and copy the output into filenames.txt — or just replace the paths inside my existing filenames.txt with your own .ts video paths. Then right-click the .bat file and select Edit. Copy the ffmpeg command, update the paths, open CMD, navigate to the correct directory, paste the command, and run it to merge the video.
Note: the result won't be watermark-free, because iQIYI is honestly quite tough to deal with

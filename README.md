# ffmpeg_concat
concat videos. Use ffmpeg to concat media files.

Usage :
There are many videos at directory D:\ToBigDisk\Bshit  for example video0.mp4 video1.mp4 video2.mp4 video3.mp4 ....
1. You can copy ffmpeg_concat.py to  D:\ToBigDisk\Bshit , and Run It ,and Generate default output video file : output.mp4
Or
2. You can :
   python3 ffmpeg_concat.py -i D:\ToBigDisk\Bshit    
       And you can get output.mp4 in D:\ToBigDisk\Bshit
Or 
3. you can set output direcotry/filename
   python3 ffmpeg_concat.py -i D:\ToBigDisk\Bshit   -o D:\   
       and you can get output.mp4 in D:\
   python3 ffmpeg_concat.py -i D:\ToBigDisk\Bshit   -o D:\  -n my.mp
       and you can get my.mp      in D:\
    

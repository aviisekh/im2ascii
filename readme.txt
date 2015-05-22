Example:  
Video
http://www.youtube.com/watch?v=yi5H_bnZzGc

[ Usage:  To convert a video file to ASCII video with no audio. ]

./ascii_movie_image_ver_1.py myvideo.mkv 4 15

“myvideo.mkv” is the name of your video file.  Supported video files are limited based on your system.
“4” is the density of ASCII characters.
“15” is the font size.

Changing the density and font size changes the look and feel of the video.

[ Usage:  To convert a image file to a ASCII image. ]

./ascii_movie_image_ver_1.py myimage.jpg 4 15

“myimage.jpg” is the name of your image file.  Supported image files are limited based on your system.
“4” is the density of ASCII characters.
“15” is the font size.

Changing the density and font size changes the look and feel of the image.

[ How To Modify ]

The following line: font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", fontsize, encoding="unic")

Is the path to the font being utilized.  If you encounter errors with the font location point this to a location where your system stores a fixed width truetype font. 

Modify any lines with “120,20,20” to change the background color of the image or video.
Modify any lines with “255,255,0” to change the font color.  

The color is expressed as an RGB triplet (r,g,b), each component of which can vary from 0 to 255. If all the components are at zero the result is black; if all are at maximum, the result is the brightest representable white.


External link to FFMEG:

Modify this line to your external ffmpeg source.

	subprocess.call(["./ffmpeg/ffmpeg", "-i", "%d.png", "-r",  frame_rate, "-y", "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-c:a", "copy", "-pix_fmt", "yuv420p", "output.mkv" ])


[ Important ]
Non fixed width fonts might distort the image.

I use a static ffmpeg build because it runs faster and creates a smaller higher quality video.  The ffmpeg commands I use is optimized for Youtube streaming.  You can download the latest from.  http://johnvansickle.com/ffmpeg/


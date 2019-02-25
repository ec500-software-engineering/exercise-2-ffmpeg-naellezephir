# FFMPEG with CI
Python CI template for EC500 Software Engineering

## Estimation
I did some trial and error for estimating how many threads I could have. I ran 4 processes at the same time and used 95% of my CPU so I decided to set the limit of threads to 3.

## Program
To run the ffmpeg.py file, you must run it with the path to your video folder as an argument. The main file then takes in that path and fills the queue with all the files in that folder. My conversion function takes in a the queue with the video files to be converted and as long as the queue isn't empty it converts to 720 then 480 printing to terminal when each conversion has started/ended. In my main code, 3 workers are deployed to start the conversions. 

## Unit Test
I added a unit test that creates a random video and checks to see that duration of the video after being converted is the same as the original video.

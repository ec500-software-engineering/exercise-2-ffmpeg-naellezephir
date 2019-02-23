# FFMPEG with CI
Python CI template for EC500 Software Engineering

## Estimation
I did some trial and error for estimating how many threads I could have. I ran 4 processes at the same time and used 95% of my CPU so I decided to set the limit of threads to 3.

## Program
My conversion function takes in a Queue with the video files to be converted and as long as the queue isn't empty it converts to 720 then 480 printing to terminal when each conversion has started/ended. I then have helper functions in my main code fills the queue with videos from a video folder and deploys 3 workers to start the conversions. 

## Unit Test
I added a unit test that creates a random video and checks to see that duration of the video after being converted is the same as the original video.

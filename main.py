import time
import subprocess

while (1):
  #save image from webcam to webcam_raw.jpeg
  subprocess.call("streamer -f jpeg -o ./webcam_raw.jpeg 2>/dev/null", shell=True)

  #process using libccv
  subprocess.call("./libccv/bbfdetect ./webcam_raw.jpeg ./samples/face"

  
  time.sleep(1)

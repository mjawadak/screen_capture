# Screen Capture
Capture screen images in linux-based environments

We can use ```ffmpeg``` to capture screenshots and save them to disk. The following command captures screenshots every one second and saves them to disk with the file names having the timestamp of the captured image.

```
ffmpeg -nostdin -video_size 1596x900 -framerate 1 -f x11grab -i :20.0+1,151 -strftime 1 img_%Y%m%d%H%M%S%z.png
```


Tested on a VM in GCP with Ubuntu as the underlying OS: 
Linux instance-2 5.4.0-1097-gcp #106~18.04.1-Ubuntu SMP Fri Dec 2 13:46:42 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux


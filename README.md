# screen_capture
Capture screen images in linux-based environments

We can use ```ffmpeg``` to capture screenshots and save them to disk. The following commands captures screenshots every one second and save them on disk with a names having the timestamp of the captured image.

```
ffmpeg -nostdin -video_size 1596x900 -framerate 1 -f x11grab -i :20.0+1,151 -strftime 1 img_%Y%m%d%H%M%S%z.png
```

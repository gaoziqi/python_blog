docker run -dt -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD/data:/data \
-e DISPLAY=unix$DISPLAY dwg /bin/bash
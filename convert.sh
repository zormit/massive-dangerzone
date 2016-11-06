#! /bin/bash
#
# Converts all MP4 files in the current directory to MP3s.
#
for f in *.mp4; do
 newname=`echo $f | tr ' ' '_' `
 mv "$f" $newname
 f=$newname
 mplayer $f -ao pcm:file=tmp.wav
 lame -b 128 -q 2 tmp.wav ${f/.mp4/.mp3}
 rm -f tmp.wav
done

#!/usr/bin/env bash
# Download auto-captions for every video into raw_transcripts/<id>.en.vtt
set -u
YT=~/.local/bin/yt-dlp
OUT=/home/john/repos/leaps/raw_transcripts
IDX=/home/john/repos/leaps/_video_index.txt
n=0; done=0; skip=0
total=$(wc -l < "$IDX")
while IFS='|' read -r id title dur; do
  n=$((n+1))
  if ls "$OUT/$id".*.vtt >/dev/null 2>&1; then skip=$((skip+1)); continue; fi
  $YT --skip-download --write-auto-subs --write-subs --sub-langs "en.*" --sub-format vtt \
      -o "$OUT/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >/dev/null 2>&1 \
      && done=$((done+1)) || echo "FAIL $id $title"
  sleep 1
done < "$IDX"
echo "DONE total=$total downloaded=$done skipped=$skip"

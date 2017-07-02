# VideoCaptureFromSocialText
   
Final Project of Multimedia System Course at NCHU 105 CS in-service master program.

Live webcast is a trend currently.
Many sport games and important shows are broadcast on network synchronize with broadcast on TV.
After the webcast, most of video share platform provide complete replay video on their platform.
These full video playback time are usually at least more than one hour.
We try to address an issue about "how to find a time period of a video which users concern".
We do text mining from PTT Bulletin Board System (PTT), and try to find a specific time period of a video for which users want to focus.
After finding the specific time period, we show the replay video on Youtube and specify the start time.


This implementation is based on Python 2.7.

Programs descriptions:
- pttparser.py: crawl live webcast articles.
- wordsplit.py: word segmentation.
- wordcountToDb.py: words frequency calculation.
- searchKeyWord.py: compute a specify time period from a keyword.

usa in command mode, the command is as follow:
python searchKeyWord.py your_keyword

for example:
python searchkeyWord.py 張雨生

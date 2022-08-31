from pytube import YouTube
import os
import youtube_dl

ydl_opts = {}
 
def yt(url):
 with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(
        url, download=False) 
    id1=meta['id']
    print(id1)
    linkgenerate='https://www.youtube.com/watch?v='+id1

 
 my_video1=YouTube(linkgenerate)
 title=my_video1.title
 return title,linkgenerate
def ytdwn(url):
 my_video=YouTube(url)
 stream=my_video.streams.filter(only_audio=True).first()
 out_file=stream.download(output_path='C:\\songs')
 base,ext=os.path.splitext(out_file) 
 new_file=base+".mp3"
 try:
  os.rename(out_file,new_file)
  print('downloaded...') 
 except:
     print('file alredy exist')
     os.remove(out_file)
 return new_file
 
 

from __future__ import unicode_literals
import youtube_dl,os,getpass,sys
from sys import argv
from win10toast import ToastNotifier

print('''
                                                                            
                                                                            ███╗   ███╗██████╗        ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗
                                                                            ████╗ ████║██╔══██╗       ██║   ██║██║██╔══██╗██║   ██║██╔════╝
                                                                            ██╔████╔██║██████╔╝       ██║   ██║██║██████╔╝██║   ██║███████╗
                                                                            ██║╚██╔╝██║██╔══██╗       ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║
                                                                            ██║ ╚═╝ ██║██║  ██║    ██╗ ╚████╔╝ ██║██║  ██║╚██████╔╝███████║
                                                                            ╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                                   
''')

cformat=''
cvfotmat=''
choice=''
caformat=''
ccaformat=''
bitrate=''
print("\n\nNote:\nAdd all YouTube links to Link.txt File[Accepts more than one link]!\nProgram will automatically Exit after Task completion!\n\n\nAuthor:Bhaskar\nCreated on:5/7/2018\nFeedback on:baskaran284@gmail.com\n")
path = input("Enter path to Save Files [Hit Enter for Default CWD]:\n")
if not path:
    path=os.getcwd()
    print("\n Your files will be save in YouTube Downloads\n")
    os.chdir(path)
if not os.path.exists('YouTube Downloads'):
    os.mkdir('YouTube Downloads')
else:
    os.chdir('YouTube Downloads')
print("Currently Working On:",os.getcwd())
Coriginal=input("\nNote:\n\nDASH Stream Will give separate Audio Video files(Useless)\nKeep original Files?<Y/N>[N]:")
if Coriginal=='y' or Coriginal=='Y':
    Ccoriginal=True
else:
    Ccoriginal=False  
      
qal=input("\nRestrict Quality By Height or size?<Y/N>[N]:\n")
if qal=='y' or qal=='Y':
    Hselect=input("Enter max Height<3840/2560/2160/1080/1024/720/480/144>:\n")
    Sselect=input("Enter the Max video size in MB<50/100/500/1000>:\n")
else:
    Hselect=8000
    Sselect=1000000
    print("Video will be downloaded at max Resolution Available\n")
    
class MyLogger(object):
    def debug(self, msg):
        print(msg,end='\r')
		
    def warning(self, msg):
        print(msgend='\r')
		
    def error(self, msg):
        print(msgend='\r')
		

def my_hook(d):
   # print(d['status']) 
    if d['status'] == 'finished':
       print('Done downloading, now converting ...')
vdownload_options = {
    'format':'bestvideo[height<=?'+str(Hselect)+']+bestaudio/best[filesize<'+str(Sselect)+'M]' ,
    #'format':'bestvideo+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'keepvideo':Ccoriginal,
    'geo_bypass':True,  
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat':'',
    }],
    #'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

adownload_options = {
    'format': 'bestaudio/best',
    'keepvideo':Ccoriginal,
    'embedthumbnail':True,
    'geo_bypass':True,
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec':'',
        'preferredquality': '',
    }],
    #'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
choi =True
while choi:    
        type=input("Enter Your Choice \n1.Video\n2.Audio\n")
        if type =='1':
            choice=vdownload_options
            choi=False
            loop=True
            while loop:
                cformat=input("Enter Your Choice \n1.Mp4\n2.MKV\n3.Webm\n4.FLV\n5.Ogg\n")
                if cformat=='1':
                    cvfotmat='mp4'  
                    loop=False
                elif cformat=='2':
                    cvfotmat='mkv' 
                    loop=False
                elif cformat=='3':
                    cvfotmat='webm' 
                    loop=False
                elif cformat=='4':
                    cvfotmat='flv' 
                    loop=False
                elif cformat=='5':
                    cvfotmat='ogg' 
                    loop=False
                else:
                    print("Invalid Input")
            t=vdownload_options['postprocessors']
            for i in t:
             i['preferedformat']= cvfotmat
                
        elif type =='2':
            choice=adownload_options
            choi=False  
            loop2=True
            while not input("Enter the bitrate[320/196/128/96/56/24]"):
                 bitrate='320'
                 break
      
            while loop2:
                
                caformat=input("1.Best Avilable\n2.AAC\n3.FLAC\n4.Mp3\n5.m4a\n6.OPUS\n7.VORBIS\n8.WAV\n")
                if caformat=='1':
                    ccaformat='best'  
                    loop2=False
                elif caformat=='2':
                    ccaformat='aac' 
                    loop2=False
                elif caformat=='3':
                    ccaformat='flac' 
                    loop2=False
                elif caformat=='4':
                    ccaformat='mp3' 
                    loop2=False
                elif caformat=='5':
                    ccaformat='m4a' 
                    loop2=False
                elif caformat=='6':
                    ccaformat='opus' 
                    loop2=False
                elif caformat=='7':
                    ccaformat='vorbis' 
                    loop2=False
                elif caformat=='8':
                    ccaformat='wav' 
                    loop2=False
                else:
                    print("Invalid Input")
                    
            s=adownload_options['postprocessors']
            for j in s:
             j['preferredcodec']= ccaformat
             j['preferredquality']= bitrate

with youtube_dl.YoutubeDL(choice) as dl:
    with open('links.txt','r') as f:
        for song_url in f:
            dl.download([song_url])
            if song_url:
                meta = dl.extract_info(song_url)
                print( 'upload date : %s' %(meta['upload_date']))
                print( 'uploader    : %s' %(meta['uploader']))
                print( 'views       : %d' %(meta['view_count']))
                print( 'likes       : %d' %(meta['like_count']))
                print( 'dislikes    : %d' %(meta['dislike_count']))
                print( 'id          : %s' %(meta['id']))
                print( 'format      : %s' %(meta['format']))
                print( 'duration    : %s' %(meta['duration']))
                print( 'title       : %s' %(meta['title']))
                print( 'description : %s' %(meta['description']))
          

toaster = ToastNotifier()
toaster.show_toast('Mr.Virus YT downloader',"Hey "+getpass.getuser()+" \nYour Files Are ready !!!",icon_path="logo.ico",threaded=True) 		
sys.exit()

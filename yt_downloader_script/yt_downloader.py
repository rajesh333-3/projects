# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:46:09 2020

@author: VenkataDurgaRajesh
"""
import string
import pandas as pd
import requests
import re
import os
from  pytube import YouTube
basepath='H:/Automated_Downloads/'#give your path

def ln(msg='*'):
    print('*'*20+msg+'*'*20)
def get_video_links_of_playlist(linkurl):
    url = linkurl
    playlist_id = re.findall(r'list=.+', url)
    playlist_id=playlist_id[0][5:]
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    print('Playlist::>',playlist_id)
    ln()
    try:
        playlist_name = re.findall(r'''"playlist":{"title":".+","contents":''', data)[0][21:-13]
        playlist_name = "".join([letter for letter in playlist_name if letter not in string.punctuation])#to remove special chars
    except:
        playlist_name = 'Rename folder'
    print('Playlist Name::>',playlist_name)
    ln()
    count_xtract=re.findall(r'''"totalVideos":\d+''', data)[0]
    start_of_int=count_xtract.find(':')+1#since the total count starts next to ':'
    count=int(count_xtract[start_of_int:])
    print("No of videos::>",count)      
    ln()
    # text_file = open("sample.txt", "w")
    # n = text_file.write(data)
    # text_file.close()
    # count=int(re.findall(r'''"totalVideos":\d+''', data)[0][-2:])
    # print(count)
    res = re.findall(r'''"url":"/watch?.*?\"''', data)
    #print(res)
    listform=list(set(res))
    video_ids=[]
    for i in range(1,count+1):
        for link in listform:
            
            link=link[:-1]
            #print(str(i),link[-(6+len(str(i))):])
            if('index='+str(i)==link[-(6+len(str(i))):]):
             #+str(link[-(len(str(i))):])   
                video_ids.append(link)
    return((video_ids),str(playlist_name),count)
def make_folder(path):
    try:
        os.mkdir(path)
    except:
        print('Folder already Exists..!')
        ln()
        pass
    print('Current Download path::>',path)    

def generate_playlist(extracted_links):
    downloadable_urls=[]
    for url in extracted_links:
        #print(url[16:27])
        downloadable_urls.append('https://www.youtube.com/watch?v='+url[16:27])
    return(downloadable_urls)

#Youtube_link='https://www.youtube.com/watch?v=yRM3sc57q0c&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V'
def ytplaylist_downloader(Youtube_link):
    urls_extracted,folder,total_count_=get_video_links_of_playlist(Youtube_link)
    #print(k)
    brk_val = input("How many videos to download out of :::> {} : ".format(total_count_))
    ln()
    path=basepath+folder+'/'
    make_folder(path)
    ln()
    download_links=generate_playlist(urls_extracted)
    loop_count=1
    for url in download_links: 
        try:
            YouTube(url).streams.first().download(path)
            print('   Completed Downloading...'+str(loop_count)+'/'+str(total_count_))
            loop_count+=1
            if(loop_count>int(brk_val)):
                break
        except Exception as ex:
            print(ex)
            try:
                print('      Trying again...')
                YouTube(url).streams.first().download(path)
                print('      Attempt successfull...! for video {}/{}'.format(str(loop_count),str(total_count_)))
            except:
                print('      Attempt Unsuccessfull...! for video {}/{}'.format(str(loop_count),str(total_count_)))
                pass 
            loop_count+=1                                                             
            pass
    print('Play list Downloaded..!')
def single_ytvideo_downloader(Youtube_link):
    yt=YouTube(Youtube_link)
    folder=str(yt.title)
    folder = "".join([letter for letter in folder if letter not in string.punctuation])
    try:
        path=basepath+folder+'/'
        
        make_folder(path)
    except:
        path=basepath+'please_rename/'
        make_folder(path)
    ln()    
    yt.streams.first().download(path)
    print(folder+'::> Download Completed..!')
  
#main
Youtube_link = input("Enter video link  :::> ")
ln()
if len(Youtube_link)>50:
    print('Playlist Detected...!')
    ln()
    ytplaylist_downloader(Youtube_link)
else:
    print('Single video Detected...!')
    ln()
    single_ytvideo_downloader(Youtube_link)


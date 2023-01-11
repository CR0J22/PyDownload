from pytube import YouTube,Playlist
from pytube.cli import on_progress

""" ("Cr0j") """

tipo = input("Baixar:\n1-Playlsit\n2-Video\n3-Audio\n4-Exit\n")

"""Playlist"""
if tipo == "1":
    link = input("Insira a url da playlsit:")

    yt = Playlist(link)

    for video in yt.videos:
        print(f"O download de {video} começou")
        video.streams.get_highest_resolution().download()
        print(f"O download de {video} acabou")

    print(f"O download de {link} acabou")

"""Video"""
if tipo == "2":
    link = input("Insira a url do video:")

    """ 22 """
    yt = YouTube(link)

    yt.streams.get_highest_resolution().download()

    print(f"O download de {link} acabou")

""" Audio """
if tipo == "3":
    link = input("Insira a url do video => audio:")

    """ 22 """
    yt = YouTube(link)

    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()

    print(f"O download de {link} acabou")
    
""" Teste de Barra de Progresso """  
if tipo =="4":
    link=input('enter url:')
    yt=YouTube(link,on_progress_callback=on_progress)
    videos=yt.streams.first()
    videos.download()
    print("(:")
    
else:
    exit
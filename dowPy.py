from pytube import YouTube,Playlist
from pytube.cli import on_progress

""" ("Cr0j") """

tipo = input("Você deseja Baixar:\n1-Playlsit\n2-Video\n3-Audio\n4-Via arquivo\n5-Sair\n")

"""Playlist"""
if tipo == "1":
    link = input("Insira a url da playlsit:")

    pl = Playlist(link)
    print("O numero de videos é: %s" % len(pl.video_urls))
    
    for url in pl.video_urls:
        video = YouTube(url,on_progress_callback=on_progress)
        video.streams.get_highest_resolution().download()
        print(f"O download de {url} acabou")
        
"""Video"""
if tipo == "2":
    link = input("Insira a url do video:")

    """ 22 """
    yt=YouTube(link,on_progress_callback=on_progress)

    yt.streams.get_highest_resolution().download()

    print(f"O download de {link} acabou")

""" Audio """
if tipo == "3":
    link = input("Insira a url do video => audio:")

    yt=YouTube(link,on_progress_callback=on_progress)

    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()

    print(f"O download de {link} acabou")
    
"""Via arquivo"""
if tipo == "4":
    """  arquivo = open('vid.txt') """
    """ print(arquivo.read()) """
    
    arq = open('vid.txt', 'r')
    texto = arq.readlines()
    for linha in texto :
        print("O download começou")
        yt=YouTube(linha,on_progress_callback=on_progress)
        yt.streams.get_highest_resolution().download()
        print(f"Download de {link} acabou!")
        
    arq.close()

    """ yt=YouTube(link,on_progress_callback=on_progress)

    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()

    print(f"O download de {link} acabou") """
   
else:
    exit
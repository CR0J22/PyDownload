from pytube import YouTube,Playlist
from pytube.cli import on_progress

""" ("Cr0j") """
print(" ____        ____                      _                 _ ")
print("|  _ \ _   _|  _ \  _____      ___ __ | | ___   __ _  __| |")
print("| |_) | | | | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |")
print("|  __/| |_| | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |")
print("|_|    \__, |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|")
print("       |___/                                               ")

tipo = input("Você deseja Baixar:\n1-Playlist\n2-Video\n3-Audio\n4-Playlist (Apenas Áudio)\n5-Via arquivo\n6-Sair\n")


"""Playlist"""
if tipo == "1":
    link = input("Insira a url da playlsit: ")

    pl = Playlist(link)
    print("O numero de videos é: %s" % len(pl.video_urls))
    
    for url in pl.video_urls:
        video = YouTube(url,on_progress_callback=on_progress)
        video.streams.get_highest_resolution().download()
        print(f"O download de {url} acabou")
        
"""Video"""
if tipo == "2":
    link = input("Insira a url do video: ")

    """ 22 """
    yt=YouTube(link,on_progress_callback=on_progress)

    yt.streams.get_highest_resolution().download()

    print(f"O download de {link} acabou")

""" Audio """
if tipo == "3":
    link = input("Insira a url do video => audio: ")

    yt=YouTube(link,on_progress_callback=on_progress)

    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()

    print(f"O download de {link} acabou")

""" Playlist (Apenas Áudio) """
if tipo == "4":
    link = input("Insira a URL da playlist: ")
    pl = Playlist(link)
    print("O número de vídeos é: %s" % len(pl.video_urls))
    
    for url in pl.video_urls:
      
        yt=YouTube(url,on_progress_callback=on_progress)
        audio = yt.streams.filter(only_audio=True)[0]
        audio.download()
        print(f"O download de {url} acabou")

      
       
    
"""Via arquivo"""
if tipo == "5":
    
    arq = open('vid.txt', 'r')
    texto = arq.readlines()
    for linha in texto :
        print("O download começou")
        yt=YouTube(linha,on_progress_callback=on_progress)
        yt.streams.get_highest_resolution().download()
        print(f"Download de {linha} acabou!")
        
    arq.close()

   
else:
    exit
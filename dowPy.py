from pytube import YouTube, Playlist
from pytube.cli import on_progress
from yt_dlp import YoutubeDL

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
    link = input("Insira a url da playlist: ")

    pl = Playlist(link)
    print("O numero de videos é: %s" % len(pl.video_urls))
    
    for url in pl.video_urls:
        video = YouTube(url, on_progress_callback=on_progress)
        video.streams.get_highest_resolution().download()
        print(f"O download de {url} acabou")

"""Video"""
if tipo == "2":
    link = input("Insira a url do video: ")

    yt = YouTube(link, on_progress_callback=on_progress)
    yt.streams.get_highest_resolution().download()

    print(f"O download de {link} acabou")

"""Audio"""
if tipo == "3":
    link = input("Insira a url do video => audio: ")

    yt = YouTube(link, on_progress_callback=on_progress)
    audio = yt.streams.filter(only_audio=True).first()
    if audio:
        audio.download()
        print(f"O download de {link} acabou")
    else:
        print("Erro ao obter o áudio.")

"""Playlist (Apenas Áudio)"""
if tipo == "4":
    link = input("Insira a URL da playlist: ")

    ydl_opts = {
        'format': 'bestaudio/best',  # Baixar o melhor áudio disponível
        'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo de saída
        'quiet': True,  # Não exibir logs desnecessários
        'postprocessors': [{  # Configuração para converter para MP3
            'key': 'FFmpegExtractAudio',  # Extrair áudio
            'preferredcodec': 'mp3',  # Formato MP3
            'preferredquality': '192',  # Qualidade do áudio (192 kbps)
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Download da playlist de áudio concluído e convertido para MP3!")

"""Via arquivo"""
if tipo == "5":
    arq = open('vid.txt', 'r')
    texto = arq.readlines()
    for linha in texto:
        print("O download começou")
        yt = YouTube(linha, on_progress_callback=on_progress)
        yt.streams.get_highest_resolution().download()
        print(f"Download de {linha} acabou!")
    arq.close()

"""Sair"""
if tipo == "6":
    exit()
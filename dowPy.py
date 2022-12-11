import pytube 

""" ("Cr0j") """

tipo = input("Baixar:\n1-Playlsit\n2-Video\n3-Exit\n")

if tipo == "1":
    link = input("Insira a url da playlsit:")

    yt = pytube.Playlist(link)

    for video in yt.videos:
        print(f"O download de {video} começou")
        video.streams.get_highest_resolution().download()
        print(f"O download de {video} acabou")

    print(f"O download de {link} acabou")
if tipo == "2":
    link = input("Insira a url do video:")

    """ 22 """
    yt = pytube.Playlist(link)

    yt.streams.get_highest_resolution().download()

    print(f"O download de {link} acabou")
else:
    exit
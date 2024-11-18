import yt_dlp
import os

def descargar_audio_video_youtube():
    # Pedir al usuario el enlace del video de YouTube
    url = input("Introduce el enlace del video de YouTube: ")

    # Opciones de descarga
    print("Elige el formato de descarga:")
    print("1. MP3 (solo audio)")
    print("2. MP4 (solo video)")
    print("3. Ambos (MP3 y MP4)")

    choice = input("Ingresa tu opción (1/2/3): ")

    # Configuración para descargar el audio o video según la elección
    ydl_opts_audio = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Nombre del archivo de salida
    }

    ydl_opts_video = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',  # Nombre del archivo de salida
    }

    try:
        with yt_dlp.YoutubeDL() as ydl:
            if choice == '1':
                # Descargar solo el audio en MP3
                print("Descargando audio en MP3...")
                ydl_opts_audio.update({'outtmpl': '%(title)s.%(ext)s'})  # actualiza el template
                ydl.download([url])
                print("Descarga de audio completada.")
            elif choice == '2':
                # Descargar solo el video en MP4
                print("Descargando video en MP4...")
                ydl.download([url])
                print("Descarga de video completada.")
            elif choice == '3':
                # Descargar tanto el audio en MP3 como el video en MP4
                print("Descargando audio en MP3 y video en MP4...")
                ydl.download([url])
                ydl_opts_audio.update({'outtmpl': '%(title)s_audio.%(ext)s'})  # actualiza el template para audio
                ydl.download([url])  # descarga el audio
                print("Descarga de audio y video completada.")
            else:
                print("Opción no válida. Por favor elige 1, 2 o 3.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejecutar la función
descargar_audio_video_youtube()


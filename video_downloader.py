#winget install "FFmpeg (Essentials Build)"
#pip install pytubefix

from pytubefix import YouTube
from pytubefix.cli import on_progress
import re
import os
import subprocess

url = "url"
path = "C:/mk-yt-video-downloader/"

yt = YouTube(url, on_progress_callback=on_progress)
safe_title = re.sub(r'[\\/*?:"<>|]', "", yt.title).replace(" ", "_").replace("ç","c").replace("ã","a")

# Baixando o vídeo
print(f"Fazendo download de: {safe_title}.mp4")
video_stream = yt.streams.filter(res="1080p").first().download(output_path=path, filename=f"{safe_title}.mp4")

# Baixando o áudio
print(f"Fazendo download de: {safe_title}.mp3")
audio_stream = yt.streams.get_audio_only().download(output_path=path, filename=f"{safe_title}.mp3")

# Utilizando ffmpeg para combinar o vídeo e o áudio
print(f"Combinando vídeo e áudio...")
input_video = os.path.join(path, f"{safe_title}.mp4")
input_audio = os.path.join(path, f"{safe_title}.mp3")
output_file = os.path.join(path, f"{safe_title}_com_audio.mp4")

command = f'ffmpeg -i "{input_video}" -i "{input_audio}" -c copy "{output_file}"'
#print(command)
subprocess.run(command)

# Remover o arquivo de áudio temporário
os.remove(input_audio)
os.remove(input_video)

print(f"Download e processamento realizados com sucesso em {output_file}")

import argparse
from pytubefix import YouTube
from pytubefix.cli import on_progress
import re
import os
import subprocess

# Configuração do argparse para receber a URL e a resolução
parser = argparse.ArgumentParser(description="Baixar vídeo e áudio do YouTube.")
parser.add_argument("url", help="URL do vídeo do YouTube")
parser.add_argument("--res", default="1080p", help="Resolução do vídeo (ex: 1080p, 720p, 480p). Padrão: 1080p")
args = parser.parse_args()

url = args.url
resolution = args.res
path = "C:/mk-yt-video-downloader/"

# Instância do YouTube
yt = YouTube(url, on_progress_callback=on_progress)

# Garante que o título do arquivo seja seguro para o sistema de arquivos
safe_title = re.sub(r'[\\/*?:"<>|]', "", yt.title).replace(" ", "_").replace("ç", "c").replace("ã", "a")

# Baixando o vídeo com a resolução especificada
print(f"Fazendo download de: {safe_title}.mp4 na resolução {resolution}")
video_stream = yt.streams.filter(res=resolution, file_extension="mp4").first()

if not video_stream:
    print(f"Resolução {resolution} não disponível. Tente outra resolução.")
    exit()

video_stream.download(output_path=path, filename=f"{safe_title}.mp4")

# Baixando o áudio
print(f"Fazendo download de: {safe_title}.mp3")
audio_stream = yt.streams.get_audio_only().download(output_path=path, filename=f"{safe_title}.mp3")

# Utilizando ffmpeg para combinar o vídeo e o áudio
print(f"Combinando vídeo e áudio...")
input_video = os.path.join(path, f"{safe_title}.mp4")
input_audio = os.path.join(path, f"{safe_title}.mp3")
output_file = os.path.join(path, f"{safe_title}_com_audio.mp4")

command = f'ffmpeg -i "{input_video}" -i "{input_audio}" -c copy "{output_file}"'
subprocess.run(command)

# Remover o arquivo de áudio temporário
os.remove(input_audio)
os.remove(input_video)

print(f"Download e processamento realizados com sucesso em {output_file}")

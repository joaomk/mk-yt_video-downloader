# YouTube Video and Audio Downloader

Este script Python foi desenvolvido para contornar uma limitação da biblioteca pytubefix, que não permite baixar vídeos do YouTube em alta resolução com áudio de forma combinada. O script realiza o download do vídeo e do áudio separadamente e, depois, utiliza o ffmpeg para combinar ambos em um único arquivo .mp4. Isso resolve o problema de não conseguir baixar vídeos com áudio diretamente.

## Pré-requisitos

Antes de executar este script, certifique-se de ter os seguintes itens instalados:

- Python 3.x
- Biblioteca `pytubefix`
- `ffmpeg` instalado no seu sistema e adicionado ao PATH do sistema

Para instalar a biblioteca `pytubefix`, utilize o `pip`:

```bash
pip install pytubefix
```

Certifique-se de que o ffmpeg está instalado corretamente. Você pode baixá-lo no site oficial do FFmpeg e seguir as instruções de instalação para o seu sistema operacional.

## Como Usar

1. Clone ou baixe este repositório para o seu computador local.
2. Navegue até a pasta onde você salvou o script.
3. Execute o script com o seguinte comando:

```bash
py download_youtube_video.py <YouTube_URL [--res <resolucao>]>
```
Substitua <YouTube_URL> pela URL do vídeo do YouTube que você deseja baixar.

Exemplo:

Baixar um vídeo em 1080p (resolução padrão):
```bash
py download_youtube_video.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
Baixar um vídeo em 720p:
```bash
py download_youtube_video.py https://www.youtube.com/watch?v=dQw4w9WgXcQ --res 720p
```

## Argumentos:
- **url**: A URL do YouTube do vídeo que você deseja baixar.
- `--res <resolucao>` é opcional e permite escolher a resolução do vídeo (ex.: 1080p, 720p, 480p). Se não for especificado, o script usará a resolução padrão de 1080p.

## Fluxo do Script

1. **Entrada da URL**: O script recebe a URL do YouTube como argumento da linha de comando.
2. **Baixar Vídeo**: Ele baixa o vídeo na resolução de 1080p como um arquivo `.mp4`.
3. **Baixar Áudio**: Ele baixa o áudio no melhor formato disponível como um arquivo `.mp3`.
4. **Combinar Vídeo e Áudio**: Usando o `ffmpeg`, ele combina o vídeo e o áudio em um único arquivo `.mp4`.
5. **Limpeza**: Os arquivos temporários de áudio e vídeo são removidos após a combinação.

## Exemplo de Saída

Após executar o script, você verá a seguinte saída no terminal:

```bash
Fazendo download de: video_title.mp4 na resolução 720p
Fazendo download de: video_title.mp3
Combinando vídeo e áudio...
Download e processamento realizados com sucesso em C:/mk-yt-video-downloader/video_title_com_audio.mp4
```

## Solução de Problemas

- **FFmpeg não encontrado**: Se você receber um erro dizendo que o `ffmpeg` não foi encontrado, certifique-se de que ele está instalado corretamente e adicionado ao PATH do sistema.
- **Vídeo não encontrado**: Caso a resolução do vídeo não esteja disponível (exemplo: sem 1080p), o script tentará automaticamente baixar o melhor stream disponível.

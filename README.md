# YouTube Video and Audio Downloader

Este script Python foi desenvolvido para contornar uma limitação da biblioteca `pytubefix`, que não consegue baixar vídeos do YouTube em alta resolução com áudio de forma combinada. O script realiza o download do vídeo e do áudio separadamente — o vídeo em resolução de 1080p e o áudio no melhor formato disponível. Após o download, ele utiliza o `ffmpeg` para combinar os arquivos de vídeo e áudio em um único arquivo `.mp4`, permitindo que o usuário tenha um arquivo final com alta qualidade de vídeo e som sincronizados. Isso resolve o problema de não conseguir baixar vídeos com áudio diretamente utilizando o `pytubefix`.

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
py download_youtube_video.py <YouTube_URL>
```
Substitua <YouTube_URL> pela URL do vídeo do YouTube que você deseja baixar.

Exemplo:

```bash
py download_youtube_video.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Argumentos:
- **url**: A URL do YouTube do vídeo que você deseja baixar.

## Fluxo do Script

1. **Entrada da URL**: O script recebe a URL do YouTube como argumento da linha de comando.
2. **Baixar Vídeo**: Ele baixa o vídeo na resolução de 1080p como um arquivo `.mp4`.
3. **Baixar Áudio**: Ele baixa o áudio no melhor formato disponível como um arquivo `.mp3`.
4. **Combinar Vídeo e Áudio**: Usando o `ffmpeg`, ele combina o vídeo e o áudio em um único arquivo `.mp4`.
5. **Limpeza**: Os arquivos temporários de áudio e vídeo são removidos após a combinação.

## Exemplo de Saída

Após executar o script, você verá a seguinte saída no terminal:

```bash
Fazendo download de: video_title.mp4
Fazendo download de: video_title.mp3
Combinando vídeo e áudio...
Download e processamento realizados com sucesso em C:/mk-yt-video-downloader/video_title_com_audio.mp4
```

## Solução de Problemas

- **FFmpeg não encontrado**: Se você receber um erro dizendo que o `ffmpeg` não foi encontrado, certifique-se de que ele está instalado corretamente e adicionado ao PATH do sistema.
- **Vídeo não encontrado**: Caso a resolução do vídeo não esteja disponível (exemplo: sem 1080p), o script tentará automaticamente baixar o melhor stream disponível.

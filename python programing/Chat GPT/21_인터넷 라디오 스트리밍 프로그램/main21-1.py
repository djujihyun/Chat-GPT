import requests
import ffmpeg

def fetch_stream_url(playlist_url):
    # HTTP GET 요청을 보내서 playlist 파일 내용을 가져옴
    response = requests.get(playlist_url)
    response.raise_for_status()  # 오류가 발생하면 예외 발생
    
    # m3u8 파일 내용을 문자열로 변환
    playlist = response.text
    
    # 스트리밍 URL 추출 (첫 번째 줄은 무시하고, 두 번째 줄을 사용)
    lines = playlist.strip().split('\n')
    stream_url = lines[1] if len(lines) > 1 else None
    
    return stream_url

def play_radio(stream_url):
    # ffmpeg을 사용하여 스트리밍을 재생
    ffmpeg.input(stream_url).output('output.mp3').run()

if __name__ == "__main__":
    playlist_url = "https://ebsonairiosaod.ebs.co.kr/fmradiobandiaod/bandiappaac/playlist.m3u8"
    
    # HLS 스트리밍 URL 가져오기
    stream_url = fetch_stream_url(playlist_url)
    
    if stream_url:
        print(f"Streaming URL: {stream_url}")
        
        # 스트리밍 재생
        play_radio(stream_url)
    else:
        print("Failed to fetch streaming URL.")

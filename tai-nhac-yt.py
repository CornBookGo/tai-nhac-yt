import yt_dlp

# Đặt URL của video bạn muốn tải
video_url = 'https://youtu.be/9jOLpL3oFeg?si=Ooe4rdqTmbZkG_bO'

# Thiết lập các tùy chọn để tải âm thanh
ydl_opts = {
    'format': 'bestaudio/best',  # Tải định dạng âm thanh tốt nhất
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # Chuyển đổi sang định dạng mp3
        'preferredquality': '192',  # Chất lượng âm thanh
    }],
}

# Tạo đối tượng yt-dlp và tải video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Tải nhạc thành công!")

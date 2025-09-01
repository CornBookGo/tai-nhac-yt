import yt_dlp
import tkinter as tk
from tkinter import messagebox, filedialog
import os
# Phải tải và đặt "ffmpeg" vào Path của Environment giống như Python.

def choose_directory():
    folder = filedialog.askdirectory()
    if folder:
        path_var.set(folder)

def download_audio():
    video_url = url_entry.get().strip()
    save_path = path_var.get().strip()

    if not video_url:
        messagebox.showerror("Lỗi", "Vui lòng nhập URL video!")
        return
    if not save_path:
        messagebox.showerror("Lỗi", "Vui lòng chọn thư mục lưu!")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),  # Lưu vào thư mục đã chọn
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        messagebox.showinfo("Thành công", "Tải nhạc thành công!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Tải thất bại: {str(e)}")

# Giao diện Tkinter
root = tk.Tk()
root.title("Tải nhạc từ YouTube")
root.geometry("500x250")

# Nhập URL
tk.Label(root, text="Nhập URL YouTube:", font=("Arial", 12)).pack(pady=5)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

# Chọn thư mục
path_var = tk.StringVar()
tk.Label(root, text="Chọn thư mục lưu:", font=("Arial", 12)).pack(pady=5)
path_frame = tk.Frame(root)
path_frame.pack(pady=5)
path_entry = tk.Entry(path_frame, textvariable=path_var, width=45)
path_entry.pack(side=tk.LEFT, padx=5)
browse_btn = tk.Button(path_frame, text="Chọn...", command=choose_directory)
browse_btn.pack(side=tk.LEFT)

# Nút tải
download_btn = tk.Button(root, text="Tải nhạc", font=("Arial", 12), command=download_audio)
download_btn.pack(pady=20)

root.mainloop()



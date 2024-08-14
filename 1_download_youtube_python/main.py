from yt_dlp import YoutubeDL

# Meminta pengguna memasukkan URL video YouTube
url = input("Masukkan URL video YouTube: ")

# Menentukan opsi unduhan
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Video terbaik + Audio terbaik
    'merge_output_format': 'mp4',  # Format output setelah digabungkan
    'outtmpl': '%(title)s.%(ext)s',  # Menyimpan dengan nama judul video
}

# Mendownload video
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download selesai!")


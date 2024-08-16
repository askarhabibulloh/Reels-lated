
---

# Download Video YouTube dengan Library Python yt-dlp

Ini adalah instruksi untuk melakukan download video YouTube dengan Python menggunakan library [yt-dlp](https://pypi.org/project/yt-dlp/). Berikut adalah langkah-langkah yang harus dilakukan:

- Melakukan instalasi Python
- **Menginstal FFmpeg**
- (Opsional) Mengaktifkan virtual environment
- Memasang library yt-dlp
- Unduh [skrip python](./main.py)
- Menjalankan program python

## Menginstal FFmpeg
1. Untuk memastikan video yang diunduh dapat diproses dengan benar, Anda perlu menginstal FFmpeg. Ikuti langkah-langkah di bawah ini sesuai dengan sistem operasi Anda:

    - **Windows:**
      1. Unduh FFmpeg dari [tautan ini](https://ffmpeg.org/download.html).
      2. Ekstrak file yang diunduh dan tambahkan direktori `bin` ke variabel lingkungan `PATH`.

    - **macOS:**
      ```bash
      brew install ffmpeg
      ```

    - **Linux (Ubuntu/Debian):**
      ```bash
      sudo apt update
      sudo apt install ffmpeg
      ```

2. Pastikan FFmpeg terinstal dengan benar dengan menjalankan perintah berikut di terminal atau command prompt:
    ```bash
    ffmpeg -version
    ```
   Perintah ini akan menampilkan versi FFmpeg yang terinstal.

## Melakukan Instalasi Python
1. Jika belum memiliki Python terinstal, unduh dan instal dari [situs resmi Python](https://www.python.org/downloads/).
2. Pastikan Python telah terinstal dengan benar dengan menjalankan perintah berikut di terminal atau command prompt:
    ```bash
    python --version
    ```
   atau
    ```bash
    python3 --version
    ```
   Perintah ini akan menampilkan versi Python yang terinstal.

## (Opsional) Mengaktifkan Virtual Environment
1. Membuat virtual environment baru untuk proyek ini:
    ```bash
    python -m venv myenv
    ```
2. Aktifkan virtual environment:
    - Di Windows:
        ```bash
        myenv\Scripts\activate
        ```
    - Di macOS/Linux:
        ```bash
        source myenv/bin/activate
        ```
3. Setelah diaktifkan, semua paket yang diinstal akan berada dalam lingkungan virtual ini, sehingga tidak mengganggu sistem Python utama.

## Memasang Library yt-dlp
1. Dengan Python sudah terinstal dan virtual environment aktif (jika digunakan), pasang library `yt-dlp` dengan menjalankan perintah:
    ```bash
    pip install yt-dlp
    ```
2. Pastikan pemasangan berhasil dengan menjalankan perintah:
    ```bash
    yt-dlp --version
    ```
   Ini akan menampilkan versi `yt-dlp` yang terinstal.

## Unduh Skrip Python
1. Unduh [skrip python](./main.py) yang berisi kode untuk mengunduh video YouTube.
2. Tempatkan skrip tersebut di dalam folder proyek Anda.

## Menjalankan Program Python
1. Jalankan skrip Python untuk mengunduh video dari YouTube dengan perintah berikut:
    ```bash
    python main.py
    ```
   atau
    ```bash
    python3 main.py
    ```
2. Skrip akan meminta URL video YouTube yang ingin Anda unduh. Masukkan URL yang diinginkan dan biarkan skrip bekerja.

3. Setelah selesai, video akan diunduh dan disimpan di folder yang sama dengan skrip Python atau lokasi yang ditentukan dalam skrip.

---
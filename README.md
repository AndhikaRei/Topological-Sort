# rancang.in ~ Pengambilan Mata Kuliah dengan Topological Sort
Dibuat Untuk Memenuhi Tugas Kecil-2 IF 2211 Strategi Algoritma Semester II 2020/2021. <br>
Created by: <br>
Reihan Andhika Putra 13519043

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [Python roman library](https://pypi.org/project/roman/)

## Installation
1. Install Python 3
2. Install library roman dengan command
```
pip install roman
```

## How to Use
#### Cara 1 (Cara biasa)
1. Clone/download project ini lalu buka folder src
2. Langsung klik "13519043_app.py"
3. Masukkan nama file yang berisi testcase yang ingin diuji, masukkan tanpa ekstensi
4. Tunggu hasil keluar
#### Cara 2 (Cara cmd windows)
1. Clone/download project ini
2. Buka folder hasil donwload/clone lalu masuk ke folder src
3. Buka cmd dan ketikkan command
```
python 13519043_app.py ATAU python3 13519043_app.py   (Mengikuti versi python yang anda install)
```
4. Masukkan nama file yang berisi testcase yang ingin diuji, masukkan tanpa ekstensi
5. Tunggu hasil keluar
#### Cara 3 (Menggunakan cmd code editor)
1. Pastikan anda ada di direktori yang sama dengan source code "../src/{13519043_app.py}" :exclamation: 
2. Run program python sesuai cara yang code editor kalian lakukan
3. Masukkan nama file yang berisi testcase yang ingin diuji, masukkan tanpa ekstensi
4. Tunggu hasil keluar
#### Cara 4 (Idle python)
Bukalah 13519043_app.py menggunakan editor bawaan python (IDLE). Run program dengan mengklik run lalu klik run module

# Note
1. File testcase yang diterima hanya file dengan ekstensi .txt
2. Untuk contoh file testcase yang benar silahkan contoh file yang ada di folder test
3. Input yang boleh dimasukkan dalam testcase adalah singkatan/kode mata kuliah, lebih lanjut lihat "test/List Matkul.txt"(jangan sampai salah juga dalam menuliskan huruf besar dan huruf kecil saat membuat testcase)
4. List Mata Kuliah bisa ditambah, dikurangi, maupun dirubah sesuka hati (Perhatikan bahwa formatnya adalah <Singkatan>-<Nama Mata Kuliah>, tidak boleh ada "-" di nama mata kuliah)
5. Selamat mencoba, tips : lebih mudah menggunakan code editor karena aplikasi tidak langsung close 
6. Apabila tidak bisa membaca file coba liat cara 3 langkah ke-1
7. Output hanya akan ditampilkan di layar cmd  
8. Cara kerja algoritma decrease and conquer dapat dilihat langsung pada source codenya langsung yang sudah diberi komentar dan penjelasan untuk tiap fungsi. Penjelasan singkat dengan notasi algoritmik adalah sebagai berikut:
```
L ← list kosong penampung simpul terurut 
S ← himpunan simpul yang tidak mempunyai sisi yang masuk 
while S not-empty do 
    ambil simpul n dari S 
    masukkan n ke L 
    for each simpul m dengan sisi e dari n ke m do 
        hilangkan sisi e dari graf 
        if m tidak punya sisi masuk lagi then 
            masukkan m ke dalam S 
if graf memiliki sisi then 
    return error (graf memiliki setidaknya satu siklus) 
else 
    return L (keterurutan secara topologi diperoleh)
```
9. Apabila masih tidak bisa run silahkan hubungi pembuat


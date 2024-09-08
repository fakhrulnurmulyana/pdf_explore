# menggunakan library PyPDF2

# PyPDF2 adalah pustaka populer untuk membaca dan memanipulasi file PDF. 
# Meskipun kemampuan ekstraksi teksnya terbatas, ia dapat digunakan untuk 
# mendapatkan informasi dasar dari PDF, seperti metadata, jumlah halaman, 
# dan konten teks.

import PyPDF2

# Membuka file PDF
with open('T-GEMPRO-B-m2-l1-en-file-2.en.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Menampilkan jumlah halaman
    print(f"Jumlah halaman: {len(reader.pages)}")
    
    # Menampilkan teks dari halaman pertama
    page = reader.pages[0]
    # text = page.extract_text()
    print(page)

# Ekstrak file ke format .txt
# with open('PyPDF2.txt', 'w', encoding='utf-8', errors='ignore') as file:
#     file.write(text)

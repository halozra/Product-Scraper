import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Menyiapkan opsi untuk Chrome
options = Options()
options.headless = True  # Untuk menjalankan browser tanpa tampilan GUI
options.add_argument("--start-maximized")

# Inisialisasi WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL target
link = "https://www.tokopedia.com/search?st=&q=seblak&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="

# Akses halaman dengan Selenium
driver.get(link)

# Fungsi untuk scroll ke bawah hingga elemen berhenti bertambah
def scroll_to_load_all_products(driver, wait_time=10, scroll_speed=1):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll bertahap untuk kecepatan tertentu
        for i in range(1, 11):  # Scroll dalam 10 langkah
            driver.execute_script(f"window.scrollBy(0, {last_height // 10});")
            time.sleep(scroll_speed)  # Waktu jeda antara langkah

        # Tunggu setelah scrolling selesai
        time.sleep(wait_time)

        # Periksa apakah tinggi halaman bertambah
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # Tidak ada perubahan, berhenti scrolling
            break
        last_height = new_height


# Tunggu halaman memuat dan scroll ke bawah
try:
    scroll_to_load_all_products(driver)

    # Ambil HTML setelah semua produk dimuat
    html = driver.page_source

    # Parsing HTML menggunakan BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')

    # Ambil semua elemen produk
    products = soup.find_all("div", class_="css-5wh65g")

    if products:
        # Simpan data ke dalam CSV
        with open('produk_tokopedia.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Menulis header
            writer.writerow(['Judul Produk','Harga Normal','Harga Diskon', 'Rating', 'Terjual', 'Nama Toko', 'Lokasi Toko'])

            # Loop melalui setiap produk
            for product in products:
                # Judul produk
                title = product.find("div", class_="_6+OpBPVGAgqnmycna+bWIw==")
                title_text = title.text.strip() if title else "Tidak ada judul"

                # Info penjualan
                listInfoSell = product.find("div", class_="Lrp+JcoWPuzTgMQ41Mkg3w==")
                if listInfoSell:
                    rating = listInfoSell.find("span", class_="_9jWGz3C-GX7Myq-32zWG9w==")
                    rating_text = rating.text.strip() if rating else "Tidak ada rating"

                    sold = listInfoSell.find("span", class_="se8WAnkjbVXZNA8mT+Veuw==")
                    sold_text = sold.text.strip().replace("+", " ").replace("terjual", " ").replace(" ","") if sold else "Tidak ada informasi penjualan"

                    if "rb" in sold_text:
                        sold_text = sold_text.replace("rb", "000")  # Mengubah "1rb" menjadi "1000"

                else:
                    rating_text = "Tidak ada rating"
                    sold_text = "Tidak ada informasi penjualan"

                # Info toko
                listInfoStore = product.find("div", class_="bi73OIBbtCeigSPpdXXfdw==")
                if listInfoStore:
                    storeName = listInfoStore.find("span", class_="T0rpy-LEwYNQifsgB-3SQw== pC8DMVkBZGW7-egObcWMFQ== flip")
                    storeName_text = storeName.text.strip() if storeName else "Tidak ada nama toko"

                    storeLocation = listInfoStore.find("span", class_="pC8DMVkBZGW7-egObcWMFQ== flip")
                    storeLocation_text = storeLocation.text.strip() if storeLocation else "Tidak ada lokasi toko"
                else:
                    storeName_text = "Tidak ada nama toko"
                    storeLocation_text = "Tidak ada lokasi toko"

                # Mencari elemen harga di dalam Listprice
                Listprice = product.find("div", class_="XvaCkHiisn2EZFq0THwVug==")
                if Listprice:
                    # Mencari harga normal terlebih dahulu
                    foundTwoPrice = Listprice.find("div", class_="hmtRf8oxRSR+n9OH5UxGoQ==")
                    if not foundTwoPrice:
                        # Jika hanya ada harga normal dan tidak ada harga diskon
                        priceNormal_text = Listprice.text.strip().replace("Rp", "").replace(",", "").replace(".", "").replace(" ", "")  # Menghapus "Rp" dan koma
                        priceNormal_text = int(priceNormal_text)*100
                        priceDisc_text = "Tidak ada harga diskon"
                    else:
                        # Jika ada harga diskon dan harga normal
                        priceNormal_text = foundTwoPrice.text.strip().replace("Rp", "").replace(",", "").replace(".", "").replace(" ", "")  # Menghapus "Rp" dan koma
                        priceNormal_text = int(priceNormal_text)*100
                        priceDisc = Listprice.find("div", class_="_67d6E1xDKIzw+i2D2L0tjw==")
                        priceDisc_text = priceDisc.text.strip().replace("Rp", "").replace(",", "").replace(".", "").replace(" ", "") if priceDisc else "Tidak ada harga diskon"
                        priceDisc_text = int(priceDisc_text)*100
                else:
                    # Jika Listprice tidak ditemukan
                    priceNormal_text = "Tidak ada harga normal"
                    priceDisc_text = "Tidak ada harga diskon"


                # Tulis data produk ke file CSV
                writer.writerow([title_text, priceNormal_text, priceDisc_text, rating_text, sold_text, storeName_text, storeLocation_text])

        print("Data berhasil disimpan ke produk_tokopedia.csv")
    else:
        print("Tidak ada produk yang ditemukan.")

finally:
    # Menutup browser
    driver.quit()

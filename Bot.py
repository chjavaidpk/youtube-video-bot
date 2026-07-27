import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def run_bot():
    # Chrome settings for cloud/headless running
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # بغیر اسکرین کے چلانے کے لیے
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    # 🛑 یہاں اپنی یوٹیوب ویڈیو کا لنک بدلیں 🛑
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 

    print("YouTube پر ویڈیو کھولی جا رہی ہے...")
    driver.get(video_url)

    # ویڈیو واچ ٹائم (مثلاً 120 سیکنڈ = 2 منٹ)
    time.sleep(120)

    print("ویدیو واچ مکمل ہو گئی۔")
    driver.quit()

if __name__ == "__main__":
    run_bot()


import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def run_bot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")

    driver = webdriver.Chrome(options=chrome_options)

    # آپ کا دیا ہوا لائیو ویڈیو لنک یہاں ایڈ کر دیا گیا ہے
    video_url = "https://www.youtube.com/live/BiRIHj5irIk" 

    print("YouTube پر لائیو ویڈیو کھولی جا رہی ہے...")
    driver.get(video_url)

    # 3600 سیکنڈ = 1 گھنٹہ (اگر آپ ٹائم اور بڑھانا چاہیں تو یہاں بڑھا سکتے ہیں)
    watch_time_seconds = 3600 

    start_time = time.time()
    while (time.time() - start_time) < watch_time_seconds:
        time.sleep(10)

    print("ویدیو واچ مکمل ہو گئی۔")
    driver.quit()

if __name__ == "__main__":
    run_bot()
    

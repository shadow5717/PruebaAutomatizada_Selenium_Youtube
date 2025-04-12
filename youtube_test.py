from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import webbrowser

def buscar_video_mrbeast():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.youtube.com")
        wait = WebDriverWait(driver, 10)

        search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
        search_box.send_keys("Ayudé A 2000 Personas A Caminar Otra Vez MrBeast")
        search_box.send_keys(Keys.RETURN)

        wait.until(EC.presence_of_element_located((By.ID, "video-title")))
        videos = driver.find_elements(By.ID, "video-title")

        video_encontrado = None
        for video in videos:
            titulo = video.get_attribute("title")
            link = video.get_attribute("href")
            if titulo and "Ayudé A 2000 Personas A Caminar Otra Vez" in titulo and "SM66GDRyIVY" in link:
                video_encontrado = (titulo, link)
                break

        if video_encontrado:
            print(" Video encontrado correctamente.")
            print("Título:", video_encontrado[0])
            print("Link:", video_encontrado[1])

            screenshot_path = os.path.join(os.getcwd(), "youtube_result.png")
            driver.save_screenshot(screenshot_path)
            print(" Captura guardada en:", screenshot_path)

            driver.quit()

            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" 
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))  
            webbrowser.get('chrome').open(video_encontrado[1])  

            print(" Video abierto en Google Chrome.")

        else:
            print("Video no encontrado.")

    except Exception as e:
        print(" Error durante la prueba:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    buscar_video_mrbeast()

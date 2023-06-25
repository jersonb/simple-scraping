import csv
import re
from playwright.sync_api import sync_playwright

def writerow_csv(data:list[str]):
    with open('data.csv', 'a') as f:
        writer = csv.writer(f,lineterminator='\n', delimiter=';')
        writer.writerow(data)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    root_link = 'https://www.youtube.com'
    page.goto(f'{root_link}/@MessiasBatista/videos')
    contents = page.locator('#contents').get_by_role('link').all()
    i = 1
    for content in contents:
        video_title = content.text_content()
        video_link =  f'{root_link}{content.get_attribute("href")}' 
        video_page = browser.new_page()
        video_page.goto(video_link)
        likes_count = video_page.get_by_role("button", name=re.compile("Marque este vídeo como*")).text_content()
        print(f'{i}/{len(contents)}')
        i+=1
        writerow_csv([video_title, video_link, likes_count])
       
    
    browser.close()

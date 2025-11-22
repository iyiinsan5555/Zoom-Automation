import schedule
import time
import webbrowser

ZOOM_LINK = "https://ieu-edu-tr.zoom.us/j/81846785900?pwd=3JimrVZsUzbTzjabCZ9UegqaZpkmtr.1"

def join_zoom():
    webbrowser.open(ZOOM_LINK)
    print("opening zoom")


schedule.every().monday.at("17:35").do(join_zoom)

while True:
    schedule.run_pending()
    print("waiting")
    time.sleep(5)
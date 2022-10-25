import time
from plyer import notification


if __name__ == '__main__':
    while True:
        title = "Hello!!!"
        message = "Take a break! It has been an hour!"
        notification.notify(title = title,  message = message, timeout = 10)
        time.sleep(3600)



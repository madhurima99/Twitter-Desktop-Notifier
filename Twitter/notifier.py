from plyer import notification
import time
import twitter1

#name, msg = twitter1.tweet()
msg = ""

while(True):

    name, new = twitter1.tweet()

    if msg != new:
        msg = new
        notification.notify(
            title="Twitter",
            message="@"+name + "\n" + msg,
            app_icon="twitter.ico",
            timeout=70
        )
    # sleep for 4hrs
    time.sleep(60*60*4)

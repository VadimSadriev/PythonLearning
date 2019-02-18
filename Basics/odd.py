from datetime import datetime
import os
import html
import time, random
odds = [1, 3, 5, 7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
for i in range(5):
    right_this_minute = datetime.today().minute

    if (right_this_minute in odds):
        print("This minute seems a little odd")
    else:
        print("Not an odd minute")
    time.sleep(random.randint(1, 5))

whereAmI = os.getcwd()
print(whereAmI)

print(os.environ)

print(os.getenv("APPDATA"))

print(datetime.today())

print(time.strftime("%I:%M"))

print(time.strftime("%A:%p"))

print(html.escape("This html fragment contains a <script>script</script> tag"))

print(html.unescape("I &hearts; Python's &lt;standard library &gt;."))

import time
from datetime import datetime as dt
hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com","www.twitter.com","twitter.com"]
print(dt.now())
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,2) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16) :
        print("Working Hours Only!")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun Hours")

    time.sleep(6)


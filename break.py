import time
import webbrowser


count= 1
total_breaks =3

print("The time the program started is: "+time.ctime())
while count <= total_breaks:
    time.sleep(5)
    webbrowser.open("http://sportscenter.com")
    count = count +1

print(time.ctime())

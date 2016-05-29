import urllib

def read_text():
    quotes = open("/Users/Jaredsfiles/Desktop/Udacity/python/movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check(contents)

def check(text):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    print(output)
    connection.close()
    
read_text()


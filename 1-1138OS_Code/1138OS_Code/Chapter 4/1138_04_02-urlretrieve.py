# Retrieve a file using urllib
import urllib
url = "https://geospatialpython.googlecode.com/files/hancock.zip"
fileName = "hancock.zip"
urllib.urlretrieve(url, fileName)

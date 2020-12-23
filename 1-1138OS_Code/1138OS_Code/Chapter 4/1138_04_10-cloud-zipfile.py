# Extract a zipped shapefile via a url
import urllib
import zipfile
import StringIO
import struct
url = "https://geospatialpython.googlecode.com/files/hancock.zip"
cloudshape = urllib.urlopen(url)
memoryshape = StringIO.StringIO(cloudshape.read())
zipshape = zipfile.ZipFile(memoryshape)
cloudshp = zipshape.read("hancock.shp")
# Access Python string as an array
struct.unpack("<dddd", cloudshp[36:68])

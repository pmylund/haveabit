import urllib2
import settings
from urlparse import urlparse
from google.appengine.api.images import Image

def downloadFile(url):
    data = urllib2.urlopen(url).read()
    return data

def getImageDimensions(file):
    img = Image(file)
    return img.width, img.height

def refreshImageDimensions(obj):
    # obj can be either Author or Quote
    if obj.img_url:
        obj.img_width, obj.img_height = getImageDimensions(downloadFile(obj.img_url))
        obj.put()
        return True

""" creates a url based on relative server.  Assumes that the images are all 
going to be stored in an images directory at the root.
"""
def get_image_url(request_url, rel_url):
    parsed = urlparse(request_url)
    new_url = parsed.scheme + '://' + parsed.netloc + '/images' + rel_url
    return new_url

def get_image_src(rel_url):
	return settings.base_image_dir + rel_url

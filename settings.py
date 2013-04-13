import os

""" Settings for the application that are used across different modules.
	In particular, to adapt this site template to your particular needs, 
	you must:
		1. change the hostname variable to your google apps hostname,
				ex. www.applicationname.appspot.com
		2. decide whether google analytics should be on or off
"""
hostname = 'www.71a278db-cc99-4c78-b6fa-3338a9.appspot.com' # your domain's hostname
gaq_on = False								 # True embeds google analytics into the site
gaq_account = 'UA-40104563-1'				 # set this to the analytics account #
											 # if gaq_on is True
base_image_dir = '/images'
use_strftime = False						 # If the birth & death dates should be
											 # in strftime_format
strftime_format = '%b %e, %Y'
cache_control = 'public, max-age=3600'       # Default browser Cache-Control for pages that might change
long_cache_control = 'public, max-age=7200'  # Default browser Cache-Control for pages that rarely change
page_cache_duration = 2591999                # How many seconds to cache (static) rendered pages (max: 2591999)
quotelist_cache_duration = 2591999           # How many seconds to cache lists of quotes (max: 2591999)

if os.environ.get('SERVER_SOFTWARE').startswith('Development'):
    hostname = os.environ['HTTP_HOST'] if os.environ.get('HTTP_HOST') else os.environ['SERVER_NAME']

address = 'http://' + hostname

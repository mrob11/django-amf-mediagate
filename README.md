# django-amf-mediagate

This is just a simple app used to send media files in a ByteArray with an MD5 hash. We use it at [Globacore](http://www.globacore.com) for sending files uploaded to CMS to our Flash-based touchscreen apps.

## Installation

Add `'mediagate'` to `INSTALLED_APPS` in your `settings.py` file, then include the mediagate urls in your url conf.

In your `settings.py` file add `GATEWAY_ROOT` and set it to the root path from which you want to search for files. Defaults to `MEDIA_ROOT` if you don't set it.
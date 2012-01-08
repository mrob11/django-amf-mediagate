from mediagate import settings
from pyamf.amf3 import ByteArray

import os, hashlib

def getfile(request, path, bytearray=None):
    """
    Returns a ByteArray of the file at the requested path and the md5 hash.
    """
    fp = open(os.path.join(settings.GATEWAY_ROOT, path), 'rb')
    content = fp.read()
    fp.close()
    
    ba = ByteArray()
    ba.write(content)
    
    m = hashlib.md5()
    m.update(content)
    md5 = m.hexdigest()
    
    return [path, ba, md5]

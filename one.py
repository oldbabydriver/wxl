# -*- coding: utf-8 -*-
import hashlib
s = 'asdfasdf'.encode('utf-8')
m = hashlib.md5()
m.update(s)
print(m.hexdigest())
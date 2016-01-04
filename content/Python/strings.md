Title: Python Unicode and Bytestrings
Tags: python 
Author: Charles
Summary: Python Strings
Date: 2015-05-08

Python Strings encoding.

One of the major transformations in Python from 2.X to 3.X is with Strings and how unicode data is handled. Ned Batchelder gave an excellent session about this on Pycon-2012. I will provide a brief summary about it in this blog post but I would urge you to watch the emmbedded video of the session given at the end of this blog.

* Python has two types of strings called byte-string and unicode and both subclass from type base-string.

* byte-string has series of bytes to represent strings which the computers can understand. The byte-strings are usually encoded in ascii by default. this default can be deduced by the below snippet

```
>>> import sys
>>> sys.getdefaultencoding()
'ascii'
```

* Unicode is not an encoding scheme like ASCII,UTF-8 or UTF-16. The latter provides a mapping between each character and the byte(s) that should be represented with. Whereas unicode provides an abstract concept called code points for each character symbols. for eg: the code point of pound symbol (£) is `\u00A3`. Computers cannot understand unicode code-points. They require encoding schemes like UTF-8,UTF-32 or iso-8859-1 (Latin1) encoding schemes that translates these code-points to bytestreams.

* Python unicode-string type is a string of unicode codepoints and byte-string is a string of byte array with a specific encoding. You can convert a unicode-string to a byte-string with encode function passing the encoding to be used as a parameter like this `u'ç'.encode('utf8')`. The unicode-string as an additional decode function but you will mostly never use it and hence ignore it for now.

* Similarly a byte-string can be converted to unicode-string with decode operation like this `'\xc3\xa7'.decode('utf8')`. The decode function takes the encoding to be used and it must be the same encoding which was used to encode this byte-string. Usually you wouldn't use the encode operation on byte string since it is already encoded but yet this function is available in byte-string.


* In Python 2.X the byte-string is the default string and when used along with unicode the byte-string would implicitly convert to unicode using the default encoding. In 3.X the unicode is the default string and you need to prefix bystrings with b prefix like this `b'Hello'`. In 3.X the conversion between unicode and bytestring is no longer implicit and must be handled by the programmer with `encode` and `decode` functions.


<iframe width="420" height="315" src="https://www.youtube.com/embed/sgHbC6udIqc" frameborder="0" allowfullscreen></iframe>

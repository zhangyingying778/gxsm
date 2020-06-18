@@ -1,7 +1,8 @@
  # -*- coding: utf-8 -*-
  # 获取网页上的内容

  import urllib2
 - file = urllib2.urlopen('http://helloworldbook.com/data/message.txt')
 +# file = urllib2.urlopen('http://helloworldbook.com/data/message.txt'
 +file = urllib2.urlopen('https://www.qq.com')
  message = file.read() 
  print message
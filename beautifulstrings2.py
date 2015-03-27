#!/usr/bin/python
 
import sys
import collections
import string
 
for line in open('helloworld.txt').readlines()[1:]:
  line = line.lower()
  l = collections.Counter(line)
 
  add = 26
  beauty = 0
  for key,value in l.most_common():
    if key in string.letters[:26]:
      beauty += value*add
      add -= 1
 
  print (beauty)

#!/usr/bin/python
# -*- coding: utf-8 -*-
'''LICENSE
Copyright (c) 2013-2015 bakyeono.net

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import locale
import datetime
import urllib
import urllib2
import json

locale.setlocale(locale.LC_ALL, 'ko_KR.utf-8')

'''Note on glosbe API

* WEBSITE
https://glosbe.com/a-api

* REQUEST
https://glosbe.com/gapi/translate?from=eng&dest=kor&format=json&pretty=true&phrase=phrase

* RESPONSE JSON STRUCTURE
js - from (source language)
   - dest (destination language)
   - result (ok)
   - tuc (list) - tuc item

tuc item
item - phrase - text
              - language
     - meanings (list) - meaning - language
                                 - text

'''

usage = '''Usage:   python glosbe.py SOURCE_LANGAGE DESTINATION_LANGUAGE PHRASE
Example: python glosbe.py eng kor text'''

def request_glosbe(src_lang, dst_lang, phrase) :
  glosbe_url = 'https://glosbe.com/gapi/translate'
  query_params = {
      'from'   : src_lang,
      'dest'   : dst_lang,
      'format' : 'json',
      'phrase' : phrase
      }
  query_url = urllib.urlencode(query_params)
  response = urllib2.urlopen(glosbe_url + '?' + query_url)
  return response.read()


def line_with_phrase(tuc_item) :
  return tuc_item['phrase']['text']

def line_with_phrase_and_meaning(tuc_item) :
  line = ''
  phrase = tuc_item.get('phrase')
  meanings = tuc_item.get('meanings')
  line += phrase['text']
  if (meanings and (0 < len(meanings))) :
    line += ' - '
    line += meanings[0]['text'] # use the first meaning only.
  return line

def extract_glosbe_response(js) :
  if (js['result'] != 'ok') :
    return None
  # lines = [line_with_phrase_and_meaning(i) for i in js['tuc'] if i.get('phrase')]
  lines = [line_with_phrase(i) for i in js['tuc'] if i.get('phrase')]
  if (len(lines) == 0) :
    return None
  return '\n'.join(lines).encode('utf-8').strip()

def dic(src_lang, dst_lang, phrase) :
  response = request_glosbe(src_lang, dst_lang, phrase)
  js = json.loads(response)
  lines = extract_glosbe_response(js)
  if (lines == None) :
    return (phrase + '? 그건 제 사전에 없어요.')
  return (phrase + '\n========\n' + lines)

def main() :
  if (len(sys.argv) < 4) :
    print(usage)
    return 1
  src_lang = sys.argv[1]
  dst_lang = sys.argv[2]
  phrase = ' '.join(sys.argv[3:])
  try :
    output = dic(src_lang, dst_lang, phrase)
  except Exception, e :
    print(e)
    return 2
  print(output)
  return 0

if (__name__ == '__main__') :
  main()


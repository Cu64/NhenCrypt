#!/usr/bin/env python3
import nhentai

codes = [290886, 235660, 236509, 201814, 244327, 177674, 250164, 198832, 185387, 205089, 255015, 140870, 297974]

def decrypt(msg):
    characters = msg.split(".")
    full_string = ""
    
    prev_code = ""
    prev_title = ""
    
    for character in characters:
        code = character[0:6]
        index = int(character[6:])
        if code != prev_code:
            d = nhentai.Doujinshi(int(code))
            print(d.name)
            character_decoded = d.name[index:index+1]
            full_string = full_string + character_decoded
            print(code + "   " + str(index) + "   " + character_decoded)
            prev_code = code
            prev_title = d.name
        elif code == prev_code:
            print(prev_title)
            character_decoded = prev_title[index:index+1]
            full_string = full_string + character_decoded
            print(code + "   " + str(index) + "   " + character_decoded)
    print("Decoded text: " + full_string)

decrypt("2908862.23566017.23650912.2443273.2018141.25016413.1408705")

#!/usr/bin/env python3
import nhentai
import json

codes = [290886, 235660, 236509, 201814, 244327, 177674, 250164, 198832, 185387, 205089, 255015, 140870, 297974]

def generate(codes):
    matrix = {}
    for code in codes:
        d = nhentai.Doujinshi(code)
        characters = list(d.name)
        for character in characters:
            if character in matrix:
                matrix[character].append(str(code) + str(characters.index(character)))
            else:
                matrix[character] = [str(code) + str(characters.index(character))]
    return matrix

def encrypt(msg):
    characters = list(msg)
    for character in characters:
        pass

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
            print(code + "   " + "{:6}".format(str(index)) + character_decoded)
            prev_code = code
            prev_title = d.name
        elif code == prev_code:
            print(prev_title)
            character_decoded = prev_title[index:index+1]
            full_string = full_string + character_decoded
            print(code + "   " + str(index) + "   " + character_decoded)
    print("Decoded text: " + full_string)

matrix = generate(codes)
print(matrix)
decrypt("2908862.23566017.23650912.2443273.2018141.25016413.1408705")

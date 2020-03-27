#!/usr/bin/env python3
import nhentai
import random

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

def encrypt(msg, matrix):
    characters = list(msg)
    full_string = []
    encrypted_string = ""
    for character in characters:
        character_encrypted = random.choice(matrix[character])
        full_string.append(character_encrypted)
    for character_encrypted in full_string:
        if character_encrypted == full_string[-1]:
            encrypted_string = encrypted_string + character_encrypted
        else:
            encrypted_string = encrypted_string + character_encrypted + "."
    return encrypted_string

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
    return full_string

matrix = generate(codes)
encrypted = encrypt("hoang is gay", matrix)
print("Encrypted string: " + encrypted)
print("Decrypted string: " + decrypt(encrypted))

# decode.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220L, Section 02
# Assignment:   LAB4
# Due Date:     02.11.15
#
# Description: A program to decode a message coded with a Caesar cipher

message = " "
x = raw_input("Enter the coded message you wish to be decoded: ")
key = input("Enter the key the message was encoded with: ")
for ch in x:
    y = ord(ch)
    z = y - key
    decoded = chr(z)
    message = message + decoded
print message

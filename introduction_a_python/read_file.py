#!/usr/bin/env python3.6

file = open('./hello_world.txt', 'r')
file_content = file.read()
print(file_content)
file.close()

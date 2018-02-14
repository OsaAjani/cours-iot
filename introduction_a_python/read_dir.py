#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
import os
command = os.popen('ls ./')
command_return = command.read()
print(command_return)

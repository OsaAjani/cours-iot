#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pirc522 import RFID
import time


rc522 = RFID()

while True :
    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()

    if not error :
        (error, uid) = rc522.anticoll()

        if not error :
            print('UID : {}'.format(uid))
            time.sleep(1)


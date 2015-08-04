#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rmt'

import random
import string
import sqlite3

class Gen():

    def __init__(self):
        pass


    def querydb(self, query, pathdb='../db/app.db'):
        """

        :type self: object
        """
        self.con = sqlite3.connect(pathdb)
        self.cur = self.con.cursor()
        self.cur.execute(query)
        self.con.commit()
        self.cur.close()


    def gen_idsession(self):
        self.ids = ''
        for i in range(10):
           self.ids += random.choice(string.ascii_lowercase)
        return self.ids


    def write_message(self, id, passwd, message):
        self.querydb("INSERT INTO messages (pass, idsession, message) VALUES('%s', '%s', '%s');" )
        # self.querydb("INSERT INTO messages (pass, idsession, message) VALUES(%s, %s, %s);" % (id, passwd, message))




    def read_message(self):
        pass
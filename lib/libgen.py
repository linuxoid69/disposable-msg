#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rmt'

import random
import string
import sqlite3


class Gen:
    def __init__(self):
        """

        :rtype : object
        """
        pass

    def querydb(self, query, pathdb='/home/rmt/PycharmProjects/disposable-msg/db/app.db'):
        """

        :type self: object
        """
        self.con = sqlite3.connect(pathdb)
        self.cur = self.con.cursor()
        self.cur.execute(query)
        self.fech = self.cur.fetchone()
        self.con.commit()
        self.cur.close()
        if self.fech:
           return self.fech[0]

    def gen_idsession(self):
        self.ids = ''
        for i in range(10):
            self.ids += random.choice(string.ascii_lowercase)
        return self.ids

    def write_message(self, passwd, idsession, message):
        self.querydb("INSERT INTO messages (pass, idsession, message) VALUES('%s', '%s', '%s')" % (passwd, idsession, message))

    def read_message(self, passwd, idsession):
        return self.querydb("SELECT message FROM messages WHERE pass='%s' AND idsession='%s'" % (passwd, idsession))

    def delete_message(self, passwd, idsession):
        self.querydb("DELETE FROM messages WHERE pass='%s' AND idsession='%s'" % (passwd, idsession))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rmt'

import sqlite3
import os


class Gen:
    def __init__(self):
        pass


    def querydb(self, query, pathdb=(os.path.realpath('./') + '/db/app.db')):
        '''
        :param query: запрос в базу
        :param pathdb: путь к базе
        :return: если select то возвращаем данные сообщения
        '''
        self.con = sqlite3.connect(pathdb)
        self.cur = self.con.cursor()
        self.cur.execute(query)
        self.fech = self.cur.fetchone()
        self.con.commit()
        self.cur.close()
        if self.fech:
           return self.fech[0]

    def write_message(self, passwd, idsession, message):
        '''
        Записывает данные в базу
        :param passwd: пароль полученный из формы
        :param idsession: сессия полученая из формы
        :param message: сообщение
        :return:
        '''
        self.querydb("INSERT INTO messages (pass, idsession, message) VALUES('%s', '%s', '%s')" % (passwd, idsession, message))

    def read_message(self, passwd, idsession):
        '''
        Читает данные из базы
        :param passwd: пароль полученные из get запроса
        :param idsession: idsession полученный из get запроса
        :return: возвращает сообщение
        '''
        return self.querydb("SELECT message FROM messages WHERE pass='%s' AND idsession='%s'" % (passwd, idsession))

    def delete_message(self, passwd, idsession):
        '''
        Удаляет сообщение после того как его просмотрели в браузере
        :param passwd: Пароль полученый и запроса get
        :param idsession: Idsession полученный из запроса get
        :return:
        '''
        self.querydb("DELETE FROM messages WHERE pass='%s' AND idsession='%s'" % (passwd, idsession))

    def create_db(self):
        '''
        Создаем базу если ее нет
        :return: True если успешно созданна
        '''
        create_table = """CREATE TABLE messages (
          id INTEGER PRIMARY KEY   AUTOINCREMENT,
          pass text  NOT NULL,
          idsession text  NOT NULL,
          message longtext  not null
        )"""
        self.querydb(create_table)
        return True
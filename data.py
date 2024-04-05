import mysql.connector

from utilities.config import getQuery


# def add_book(isbn):
#     book = {'name': 'sahasbook',
#      'isbn': isbn,
#      'aisle': '409',
#      'author': 'Saha'
#             }
#
#     return book



def add_book(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
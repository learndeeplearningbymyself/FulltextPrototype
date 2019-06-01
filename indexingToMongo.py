from pyvi import ViTokenizer, ViPosTagger
from pymongo import MongoClient
import re

client = MongoClient('mongodb://localhost:27017/')
db = client['ex-book']
collectionTermPhrase = db['term-phrase']
collectionBook = db['book']


def getBookWithPagination(page, size):
    results = collectionBook.find().skip(page * size).limit(size)
    payload = []
    for result in results:
        payload.append(result)
    return payload


def removeMungingInText(desc):
    descClean = re.sub(r'\*\[(.*?)\] | \((.*?)\)', '', desc)
    return descClean


def indexingTermPharseIntoDB(term):
    result = collectionTermPhrase.insert_one(term)
    print(result)


if __name__ == '__main__':
    count = collectionBook.count()
    size = 20
    for page in range(0, int(count / size) + 1, 1):
        bookPayload = getBookWithPagination(page, size)
        for book in bookPayload:
            desc = book.get('title') + book.get('description')
            desc = removeMungingInText(desc)
            print(ViTokenizer.tokenize(desc))

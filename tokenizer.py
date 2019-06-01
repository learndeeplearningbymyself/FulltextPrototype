from pyvi import ViTokenizer, ViPosTagger

documents = []

f = open("data.txt", "r")
for row in f:
    row = row.replace('\ n','')
    row = row.replace('\r','')
    row = row.replace('* * *','')
    row = row.replace('“','')
    row = row.replace('”','')
    row = row.replace('"','')
    row = row.replace('\\','')
    documents.append(ViTokenizer.tokenize(row.strip()))
f.close()

f = open("data.txt", "w")
for doc in documents:
    f.write(doc + "\n")
f.close()
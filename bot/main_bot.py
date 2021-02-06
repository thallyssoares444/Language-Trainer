import nltk
from nltk.stem.lancaster import LancasterStemmer
import tflearn
import numpy
import tensorflow
import random 
import json

stemmer = LancasterStemmer()

# pega o arquivo json
with open("bot/db_text.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

# pega os dados dos elementos do json e armazena ele em cada array
for chats in data["chat"]:
    for question in chats["quest"]:
        wrds = nltk.word_tokenize(question)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(chats["tag"])

    # pega o tema do chat 
    if chats["tag"] not in labels:
        labels.append(chats["tag"])

# coloca em minisculas pra não dar problema na verificação
words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

# faz a verificação das palavras e vê se ela esta na lista 
for x,doc in enumerate(docs_x):
    bag = []
    wrds = [stemmer.stem(w) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)
model.fit(training,output,n_epoch=1000,batch_size=8,show_metric=True)
model.save("model.tflearn")
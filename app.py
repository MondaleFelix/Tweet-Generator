from flask import Flask
from markov_chain import * 

app = Flask(__name__)



@app.route("/")
def hello_world():
	words_list = "one fish two fish red fish blue fish"	
	sentence = return_sentence(get_following_words(words_list), 10)
	print(sentence)
	return sentence



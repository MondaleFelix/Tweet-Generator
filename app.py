from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from markov_chain import * 

app = Flask(__name__)

text = get_clean_text("corpus.txt")


@app.route("/", methods=['GET'])
def hello_world():

	sentence = return_sentence(get_following_words(text), 10)

	return sentence


import numpy as np

EMOTION = 'fear'
#emotions list = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust']


def make_emotion_dict(filename):
	"""
	This function takes in an emotion lexicon and returns a dictionary where 
	the key is the word and the value is the score for that word for the given EMOTION.
	Each line on the file has 3 values. The first is the word, the second is an emotion, and the third is 
	a value (either 0 or 1) which explains if the word expresses that emotion. 
	In this function, you should create a dictionary for every word in the file and store its score 
	for the emotion that the emotion constant is equal to. 
	For example, the line 'memorable joy 1' would correspond to {'joy': 1} 
	whereas the line 'memorandum fear 0' would not correspond to any value in the dictionary because it is the wrong emotion.
	"""
	emotion_dict = {}
	for line in open(filename):
		splits = line.split()
		if splits[1] == EMOTION:
			curr_word = splits[0]
			value = int(splits[2])
			emotion_dict[curr_word] = value
	return emotion_dict

def sum_tweet(tweet, emotion_dict):
	"""
	This function goes over each word in the sentence and sums up their corresponding values in the dictionary. 
	If a word is not in the dictionary, it is ignored. Make sure that words can be any case. 
	It returns this sum. 

	>>> emotion_dict = {'happy':1, 'birthday':1}
    >>> sum_tweet(['Happy', 'Birthday', 'Brahm!'], emotion_dict)
    2
    """
	score = 0
	for word in tweet:
		if word.lower() in emotion_dict:
			score += emotion_dict[word.lower()]
	return score


def read_file(filename, emotion_dict, stoplist):
	"""
	This function reads in a file where each line is a fictional tweet. It should remove all stopwords 
	from a tweet and then calculate its sum. A stopword are short words that won't correctly impact
	the sentiment analysis of a tweet, so it is best practice to remove these before doing any classification. 
	Use the helpful remove_stopwords() function that we wrote for you. Don't forget to pass in stoplist. 
	This function should return the tweet with the highest score.  
	"""
	tweet = ""
	max_score = -1
	high_score = {}
	for line in open(filename):
		splits = line.strip().split()
		short_tweet = remove_stop_words(splits, stoplist)
		score = sum_tweet(short_tweet, emotion_dict)
		high_score.setdefault(score, [])
		high_score[score].append(line)
		"""if score >= max_score:
			max_score = score
			tweet = line"""

	return high_score

def main():
	#creates a list of all words that you want to remove from each tweet 
	stoplist = build_stop_list()

	emotion_dict = make_emotion_dict('emotion-lexicon.txt')
	top_score = read_file('random_sentences.txt', emotion_dict, stoplist)
	max_score = max(top_score.keys())
	min_score = min(top_score.keys())
	print(max_score, top_score[max_score])
	print(min_score, top_score[min_score])


#Feel free to call this function 
def remove_stop_words(line, stoplist):
	updated_tweet = []
	for word in line: 
		if word.lower() not in stoplist:
			updated_tweet.append(word)
	return updated_tweet

#build_stop_list has already been called for you 
def build_stop_list():
	stoplist = []
	f = open("english.stop")
	stoplist = f.readlines()
	return stoplist

if __name__ == "__main__":
	main()

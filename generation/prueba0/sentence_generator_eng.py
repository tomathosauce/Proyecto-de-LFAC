import argparse
from math import floor
import random
import operator
import os
from typing import Dict, List
from parser0_eng import parser
from lexer import lexer

def parse_grammar(file_path):
	"""
	Generate a grammar from a file describing the production rules.
	Note that the symbols are inferred from the production rules.

	For more information on the format of the file, please reffer to
	the README.md or the the sample grammars provided in this repository.

	:param file_path: Path to the file containing the description of the grammar.
	:returns: the grammar object and the starting symbol.
	"""
	with open(file_path) as f:
		content = f.read().splitlines()

	if len(content) <= 1:
		raise Exception('Grammar should have at least one production rule and a starting symbol')

	# First line should be the starting symbol
	start_symbol = content[0]

	grammar = {}
	for line in content[1:]:
		# Each line should be in the format:
		# X -> A B ... C
		symbols = line.split()
		if len(symbols) <= 2 or symbols[1] != '->':
			raise Exception('Each production line should be in the format: X -> A B ... C')

		if symbols[0] not in grammar:
			grammar[symbols[0]] = []

		grammar[symbols[0]].append(symbols[2:])

	if start_symbol not in grammar:
		raise Exception('Grammar should have at leats one production rule with the start_symbol.')

	return grammar, start_symbol


def find_terminals(grammar):
	"""
	For a given grammar, return a set of the terminal symbols.

	:param grammar: The grammar (set of productions rules).
	:return: set of terminal symbols.
	"""
	terminals = set()
	for key, val in grammar.items():
		for word_list in val:
			for word in word_list:
				if word not in grammar:
					terminals.add(word)
	return terminals

def analyze_stats(sentences):
	"""
	For a given set of sentences, print how many times each symbol appears,
	printing statistics sorted by occurrance.

	:param sentences: List of sentences.
	"""
	counts = {}
	for sentence in sentences:
		for element in sentence.split():
			if element not in counts:
				counts[element] = 1
			else:
				counts[element] += 1

	# print stats
	sorted_counts = sorted(counts.items(), key = operator.itemgetter(1))
	for key, val in sorted_counts:
		print("%5d %s" % (val, key))
  
def mutate_sentence(sentence: List[str], terminals: List[str]):
	pos = floor(random.random() * len(sentence))
	mutation_type = random.choice(['insert', 'delete', 'replace'])

	if len(sentence) < 2:
		mutation_type = random.choice(['insert', 'replace'])

	match mutation_type:
		case 'insert':
			sentence.insert(pos, random.choice(list(terminals)))
		case 'delete':
			sentence.pop(pos)
		case 'replace':
			sentence[pos] = random.choice(list(terminals))
	
	return sentence
	

def probability_of_terminal(sentence_length, a = 1, k=1, c=1):
	return 1 - a/(sentence_length/k + c)

def contains_non_terminal(rule: List[List[str]], terminals: List[str] = []):
	for instance in rule:
		if instance not in terminals:
			return False
			
	return True

def generate_random_sentence(grammar: Dict[str, List[List[str]]], start_symbol, print_sentence = True, terminals: List[str] = [], k=10, mutate=False):
	"""
	For a given grammar (set of production rules) and a starting symbol,
	randomly generate a sentence using the production rules.

	:param sentences: The grammar (set of productions rules).
	:param start_symbol: The starting symbol.
	:param print_sentence: Wether to print the generated sentence. Defaults to true.
	:returns: A randomly generated sentence.
	"""
	# Starting symbol must be a part of the grammar
	assert start_symbol in grammar
	
	sentence = [start_symbol]
	idx = 0
	while idx < len(sentence):
		if sentence[idx] in terminals:
			idx += 1
		else:
			choices = grammar[sentence[idx]]
   
			terminal_rules = [rule for rule in choices if contains_non_terminal(rule, terminals)]
			
			if random.random() < probability_of_terminal(len(sentence), k):
				choice = random.choice(terminal_rules)
			else:
				choice = random.choice(choices)
			sentence = sentence[:idx] + choice + sentence[idx+1:]
   

	if mutate:
		correct = True
		while correct and len(sentence) > 0:
			mutate_sentence(sentence, terminals)
			sentence_str = " ".join([word.upper() for word in sentence])
			try:
				parser.parse(sentence_str, lexer=lexer)
			except Exception as e:
				correct = False
				
	# sentence = " ".join([word.upper() for word in sentence])
	sentence = " ".join(sentence)
	if print_sentence:
		print(sentence)
	return sentence

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Grammar utils')
	parser.add_argument('--grammar', type=str, default='grammar.txt',
					  help='Path to grammar file.')
	parser.add_argument('--print_terminal_symbols', action='store_true',
					  help='Print the terminal symbols of the grammar.')
	parser.add_argument('-ns', '--num_sentences', type=int, default=5,
					  help='The number of random sentences to generate.')
	parser.add_argument('-k', '--k', type=int, default=10,
					  help='Number of tokens required to have a probability of a terminal to be 0.5.')
	parser.add_argument('-s', '--save', action='store_true')
	parser.add_argument('-sfn', '--save_filename', type=str, default="output.txt")
	parser.add_argument('-m', '--mutate', action='store_true')
	parser.add_argument('-csv', '--csv', action='store_true')

	args = parser.parse_args()

	grammar, start_symbol = parse_grammar(args.grammar)

	terminals = find_terminals(grammar)
	
	if args.print_terminal_symbols:
		for terminal in sorted(terminals):
			print(terminal)
		print('-----------------')
		print('There are', len(terminals), 'terminals')

	sentences = set()
	print('mutate', args.mutate)
	while len(sentences) < args.num_sentences:
		sentences.add(generate_random_sentence(grammar, start_symbol, False, terminals=terminals, k=args.k, mutate=args.mutate))

	if args.save:
		ext = '.txt'
		label = 1
		if args.csv:
			ext = '.csv'
		if args.mutate:
			label = 0
  
		with open(args.save_filename+ext, 'w') as f:
			if args.csv:
				f.write("sentence,label\n")
			for sentence in sentences:
				f.write("{},{}\n".format(sentence, label))
	else:
		for i in range(len(sentences)):
			print("%d. %s" % (i, sentences[i]))
import sys
from igraph import *
import os,glob
import spacy

nlp = spacy.load("en_core_web_sm")
nlp.max_length = 9000000 # increases nlp max lenght for analysis

def create_co_occurrence_graph(folder_path, is_directed, window_size, output_file):

    all_text = [] # Saves all documents in a list of lists
    for filename in glob.glob(os.path.join(folder_path, '*.txt')):
        with open(filename, 'r', encoding='utf8') as f:
            text = f.read()
            all_text.append(text.lower())
            #print (filename)
            #print (len(text))

    doc = nlp(' '.join(all_text))

    words = []

    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "ADJ":
            if token.text != '*' and len(token.text) > 1:
                words.append(str(token))

    g = Graph(directed = is_directed)

    g.add_vertices(words[0])
    for i in range(1,len(words)):
        if words[i] not in g.vs['name']:
            g.add_vertices(words[i])
        if not g.are_connected(words[i-1],words[i]):
            g.add_edge(words[i-1],words[i])

        #adding the connections for other window sizes
        if i > 1 and window_size > 1:
            if not g.are_connected(words[i-2],words[i]):
                g.add_edge(words[i-2],words[i])
        if i > 2 and window_size > 2:
            if not g.are_connected(words[i-3],words[i]):
                g.add_edge(words[i-3],words[i])
        if i > 3 and window_size > 3:
            if not g.are_connected(words[i-4],words[i]):
                g.add_edge(words[i-4],words[i])
        if i > 4 and window_size > 4:
            if not g.are_connected(words[i-5],words[i]):
                g.add_edge(words[i-5],words[i])
        if i > 5 and window_size > 5:
            if not g.are_connected(words[i-6],words[i]):
                g.add_edge(words[i-6],words[i])

    g.vs['id'] = g.vs['name']
    g.write_pajek(output_file)

if __name__ == '__main__':
    if len(sys.argv) < 5:
        sys.exit("Input format is wrong. Missing arguments.")

    direction = sys.argv[1]
    if direction == "-d": # directed
        is_directed = True
    elif direction == "-u": #undirected
        is_directed = False
    else:
        sys.exit("Input format is wrong. Expecting -d or -u")

    window_size = sys.argv[2]
    if(window_size.isdigit() == False or int(window_size) < 1 or int(window_size) > 5):
        sys.exit("Input format is wrong. Expecting 1, 2, 3, 4 or 5 for the window size.")

    input_data = sys.argv[3]
    #input_data = open(input_file).read().split()

    output_file = sys.argv[4]

    create_co_occurrence_graph(input_data, is_directed, int(window_size), output_file)
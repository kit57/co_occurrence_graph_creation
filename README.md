
# Create a co-ocurrence graph in Pajek format

This is a program that creates a graph with Pajek format with .txt files from a folder. Using SpaCy . In this case, it 
is used "en_core_web_sm" language model which is only 11 MB. You can visit 
<a href="https://spacy.io/usage/models">SpaCy</a> doc page if you want to download a larger model or choose another 
language model.

This graph is only taking into account words labelled as "NOUN" and "ADJ". You can modify this by editing line 24.


## Download python packages and language model

To install all the necessary dependencies run the next line:

```pip install -r requirements.txt```

Afterwards, we need to install the spaCy’s language model we want to use. 

```python -m spacy download en_core_web_sm```

## Running the program

Use:

```python get_coocurrence_graph.py -d|-u <window_size> <folder_path> <output_file>```

The parameters are defined as follows:

<ul><i>-d|-u</i>: directed or undirected graph</ul>
<ul><i>window_size</i>: The term window is a configurable parameter of the program, it is modified with window_size that \
 admits values from 1 to 3.</ul>
<ul><i>folder_path</i>: The directory where the .txt files are located.</ul>
<ul><i>output_file</i>: The directory and file name will have to be specified by the user in the variable</ul>

If there's a lot of files, this process might take some time. Be patient.

```
*Vertices 6007
1 "adaptive"
2 "resource"
3 "management"
4 "real"
5 "time"
6 "systems"
7 "challenging"
8 "problem"
9 "researchers"
10 "developers"
.
.
.
*Edges
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10
4 10
5 11
.
.
.
```
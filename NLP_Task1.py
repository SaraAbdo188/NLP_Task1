from nltk.tokenize import sent_tokenize , word_tokenize 

text =  input("Please inter your text\n")
number = int(input("\nPlease choose one of three choices:\nChoice number 1: print tokenized words\nChoice number 2: print tokenized sentences\nChoice number 3: print output using split function.\n"))
if number == 1 :
    print(word_tokenize(text))
elif number == 2 :
    print(sent_tokenize(text))
elif number == 3 :
    print(text.split())
    
    
    
    # NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project.
# Bangla text tokenizer(BNTT)
This tokenizer was trained by BengaliWikipediaArticles dataset using sentencepiece.
# Dependency
- python 3.6
- sentencepiece

# Dataset
[Dataset link](https://drive.google.com/open?id=1QYTBFyV6j1ys3L9JCSzYMnV4o34GnC7_)

# Tokenizer
 Please run ```bn_tokenizer.py```
### Input Text 
```
Hello! I am saiful , an artificial initelligence learner
```
### Output :

word tokenization - 
```
['Hello', '!', 'I', 'am', 'saiful', ',', 'an', 'artificial', 'initelligence', 'learner']

```
Bigrame- 
```
[('Hello', '!'), ('!', 'I'), ('I', 'am'), ('am', 'saiful'), ('saiful', ','), (',', 'an'), ('an', 'artificial'), ('artificial', 'initelligence'), ('initelligence', 'learner')]
```
Trigram-
```
[('Hello', '!', 'I'), ('!', 'I', 'am'), ('I', 'am', 'saiful'), ('am', 'saiful', ','), ('saiful', ',', 'an'), (',', 'an', 'artificial'), ('an', 'artificial', 'initelligence')]
```

Sentence Tokenization-
```
['Hello! I am saiful', 'an artificial initelligence learner']
```




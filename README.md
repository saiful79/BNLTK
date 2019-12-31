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
For Bangla
```
text = "আমার সোনার বাংলা. আমি ?তোমাই (*ভালোবাসি)। চিরদিন, তোমার # "
```
ngrame-
['আমার', 'সোনার', 'বাংলা', '.', 'আমি', '?', 'তোমাই', '(', '*', 'ভালোবাসি', ')', '।', 'চিরদিন', ',', 'তোমার', '#']

bigram-
[('আমার', 'সোনার'), ('সোনার', 'বাংলা'), ('বাংলা', '.'), ('.', 'আমি'), ('আমি', '?'), ('?', 'তোমাই'), ('তোমাই', '('), ('(', '*'), ('*', 'ভালোবাসি'), ('ভালোবাসি', ')'), (')', '।'), ('।', 'চিরদিন'), ('চিরদিন', ','), (',', 'তোমার'), ('তোমার', '#')]

trigram-
[('আমার', 'সোনার', 'বাংলা'), ('সোনার', 'বাংলা', '.'), ('বাংলা', '.', 'আমি'), ('.', 'আমি', '?'), ('আমি', '?', 'তোমাই'), ('?', 'তোমাই', '('), ('তোমাই', '(', '*'), ('(', '*', 'ভালোবাসি'), ('*', 'ভালোবাসি', ')'), ('ভালোবাসি', ')', '।'), (')', '।', 'চিরদিন'), ('।', 'চিরদিন', ','), ('চিরদিন', ',', 'তোমার')]

sentence token-
['আমার সোনার বাংলা', 'আমি', 'তোমাই (*ভালোবাসি)', 'চিরদিন', 'তোমার #']

For English
```
text="Hello! I am saiful , an artificial initelligence learner"
```
### Output :

```
ngram-['Hello', '!', 'I', 'am', 'saiful', ',', 'an', 'artificial', 'initelligence', 'learner']
Bigrame- [('Hello', '!'), ('!', 'I'), ('I', 'am'), ('am', 'saiful'), ('saiful', ','), (',', 'an'), ('an', 'artificial'), ('artificial', 'initelligence'), ('initelligence', 'learner')]
Trigram-[('Hello', '!', 'I'), ('!', 'I', 'am'), ('I', 'am', 'saiful'), ('am', 'saiful', ','), ('saiful', ',', 'an'), (',', 'an', 'artificial'), ('an', 'artificial', 'initelligence')]
Sentence Tokenization-
['Hello! I am saiful', 'an artificial initelligence learner']
```




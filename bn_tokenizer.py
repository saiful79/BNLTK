import sentencepiece as spm

sp = spm.SentencePieceProcessor()

sp.Load("bengali_lm.model")

def SentenceToken(text):
    text = text.replace('।', '.')
    text = text.replace('?', '.')
    text = text.replace(',', '.')
    text = text.replace('|', '.')
    text = text.replace(',', '.')
    sen_tok =[i.strip() for i in text.split(".")]
    # print(sen_tok)
    return sen_tok

def bigram(token_list):
    bigram_token=[]
    for i in range(len(token_list)-1):
        x = (token_list[i],token_list[i+1])
        bigram_token.append(x)
        # print(token_list[i])
    return bigram_token

def trigram(token_list):
    trigram_token=[]
    for i in range(len(token_list)-3):
        x = (token_list[i],token_list[i+1],token_list[i+2])
        trigram_token.append(x)
        # print(token_list[i])
    # print(trigram_token)
    return trigram_token


def main(text,tokenizer_type):
    # print(type(tokenizer_type))
    x = ''.join(sp.EncodeAsPieces(text))
    # print(x)
    token = x.split("▁")
    # print(token)
    p = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '।', "'"]
    def punction_replace(article):
        for key in p:
            article = article.replace(key, " "+key+" ");
        new_token=[]
        x = article.split(" ")
        for i in x:
            if len(i)>0:
                new_token.append(i)
        
        return new_token

    final_token=[]
    for tok in token:
        new = punction_replace(tok.strip())
        # print()
        if len(new)>1:
            for i in new:
                final_token.append(i)
        else:
            listToStr = ' '.join([str(elem) for elem in new]) 
            final_token.append(listToStr)

    # print(final_token)
    if tokenizer_type=='1':
        # word_token = final_token
        return final_token[1:] 
    elif tokenizer_type=='sentence':
        sentence_token = SentenceToken(text)
        return sentence_token
    elif tokenizer_type=='2':
       return bigram(final_token[1:])
    elif tokenizer_type=='3':
        return trigram(final_token[1:])
    else:
        print("Please make sure your token type")
        

if __name__ == "__main__":
    text = "আমার সোনার বাংলা. আমি ?তোমাই (*ভালোবাসি)। চিরদিন, তোমার # "
    input_text = input("please enter text :")
    tokenizer_type = input("type of tokenizer type 'sentence' for sentence tokenization or 1,2,3:")
    tokenization_output = main(input_text,tokenizer_type)
    print(tokenization_output)


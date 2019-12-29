
class BnTokenizer:
    def __init__(self, text):
        self.text = text

    def BnNgram(self):
        word = self.text.split()
        print(word)

    def BnSentence(self):
        split_text = self.text.split("।") or self.text.split("|")
        print(split_text)
        # for i in :
        #     print(i)
        # sentence = [i.strip() for i in self.text.split("|") or self.text("!")]
        # print(sentence)
    def BnBigram(self):
        #example
        # [('The', 'best'), ('best', 'performance'), ('performance', 'can'), ('can', 'bring'),
        # ('bring', 'in'), ('in', 'sky'), ('sky', 'high'), ('high', 'success'), ('success', '.')]
        bigram = []
        word = self.text.split()
        for i in range(len(word)-1):
            pair_text = (word[i],word[i+1])
            bigram.append(pair_text)
        print(bigram)

    def BnTrigram(self):
        #example
        # [('The', 'best'), ('best', 'performance'), ('performance', 'can'), ('can', 'bring'),
        # ('bring', 'in'), ('in', 'sky'), ('sky', 'high'), ('high', 'success'), ('success', '.')]
        Trigram = []
        word = self.text.split()
        for i in range(len(word)-2):
            pair_text = (word[i],word[i+1],word[i+2])
            Trigram.append(pair_text)
        print(Trigram)

# x = "\
#     অন্যরকম বিজয় উদযাপন দেখে মনটা! ভরে গেলো | সারাদেশ থেকে ৩১ লক্ষ প্লাস্টিকের বোতল কুড়িয়ে দেশটাকে ?একটু হলেই পরিষ্কার করেছে বিডি ক্লিন এর সদস্যরা |\
#     এটাই আসল দেশপ্রেম |অন্যরকম বিজয় উদযাপন দেখে মনটা ভরে গেলো | সারাদেশ থেকে ৩১, লক্ষ প্লাস্টিকের বোতল কুড়িয়ে দেশটাকে একটু হলেই পরিষ্কার করেছে \
#     বিডি ক্লিন এর সদস্যরা | এটাই আসল দেশপ্রেম |\অন্যরকম বিজয় উদযাপন দেখে মনটা ভরে গেলো | সারাদেশ থেকে ৩১ লক্ষ প্লাস্টিকের বোতল কুড়িয়ে দেশটাকে \
#     একটু হলেই পরিষ্কার করেছে বিডি ক্লিন এর সদস্যরা | এটাই আসল দেশপ্রেম |"

x = "আমি ভাত খাই। সে বাজারে| যায়।"
Bn_token = BnTokenizer(x)
# Bn_token.BnNgram()
Bn_token.BnSentence()
# Bn_token.BnBigram()
# Bn_token.BnTrigram()
# # BnWordToken(x):
# # BnSentenceToken(x):
# Bn_token.BnSentenceToken()
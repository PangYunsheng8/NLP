class ForwardMaxMatching:
    def __init__(self, dic, max_length):
        super(ForwardMaxMatching).__init__()
        self.dic = dic
        self.max_length = max_length

    def matching(self, sentence):
        line = sentence
        n = len(sentence)
        tokens = []

        while len(line) > 0:
            subwords = line[0: self.max_length]
            while subwords not in self.dic:
                if len(subwords) <= 1:
                    break
                subwords = subwords[:len(subwords) - 1]

            tokens.append(subwords)
            line = line[len(subwords):]
        return tokens


if __name__ == '__main__':
    sentence = "我们经常有意见分歧矛盾"
    dic = ["我们", "经常", "常有", "有意见", "有意", "意见", "分歧", "我", "们", "经", "常", "有", "意", "见"]
    max_length = 5

    forward_max_matching = ForwardMaxMatching(dic, max_length)
    tokens = forward_max_matching.matching(sentence)
    print(tokens)


import MeCab

if __name__ == '__main__':

    tagger = MeCab.Tagger("-O wakati")
    text = '日本語のテキストを解析して分割します'
    tagger.parse(text)

    print()
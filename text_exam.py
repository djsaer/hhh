Rewords = {"False", "None", "True", "and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in",
           "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"}


def gettext(text):
    txt = open(text,"r",errors='ignore').read()
    for ch in '!@#$%^&*()_+-=,./;:"|\`~':
        txt = txt.replace(ch, " ")
    return txt


def main():
    text = input("请输入文件名称")
    pytxt = gettext(text)
    words = pytxt.split()
    counts = {}
    for word in words:
        if word in Rewords:
            counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key = lambda x:x[1], reverse = True)
    for i in range(10):
        word, count = items[i]
        print ("{0:<10}{1:>5}".format(word, count))
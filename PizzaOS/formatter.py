import re

str1 = " foiwe f! !!   !   !!wfe  wdq fwe !f,,, ! wff !  e,2, wef w!!efw....ef,, 21,2fwe  wfe1,  fwe fwe 2121,,  ;;;; 2\n1,,,..."
# str1 = "hello !!! my name is ,wadk!!!  oh my god...  how are you???  ha-ha-ha. that's  ..."


def format_text(str_: str):
    print(str_)

    str_.replace('#', '')
    str_ = str_.replace('\n', '#')
    str_ = ' '.join(str_.split())
    str_ = str_.replace('#', '\n')

    for c in ".,;!?-_ ":
        str_ = str_.replace(f" {c}", f"{c}")
        while str_.find(c + c) != -1:
            str_ = str_.replace(f"{c}{c}", f"{c}")

    str_ = re.sub(r'(?<=[.,;!?])(?=[^\s])', r' ', str_)
    str_ = str_.capitalize()

    for i in range(0, len(str_) - 2):
        if str_[i] in "!?.":
            if str_[i + 1] == ' ':
                str_ = str_[:i + 2] + str_[i + 2:].capitalize()

    return str_


print(format_text(str1))

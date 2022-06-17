import re


class Links:

    def __init__(self, path=None):
        self._path = path
        with open(path, "r", encoding="utf8") as f:
            self._text = f.read()

    def __call__(self):
        return "\n".join(re.findall(r'href=\"([^\'\"]+)\"', self._text))


a = Links("../14-gen-and-magic/w3.html")

print(a())


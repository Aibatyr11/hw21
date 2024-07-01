class Text:
    def __init__(self,text=""):
        self._text = text

    def set_text(self,text = None):
        if text is not None:
            self._text = text
        else:
            self._text = "None"

    def get_text(self):
        return self._text
    
class Number(Text):
    def __init__(self, text="",number=0):
        super().__init__(text)
        self._number = number

    def set_number(self,number):
        self._number = number
    def get_number(self):
        return self._number
    
text1 = Text("Hello")
print(text1.get_text())

text1.set_text()
print(text1.get_text())

text2 = Number("h", 3)
print(text2.get_text())
print(text2.get_number())



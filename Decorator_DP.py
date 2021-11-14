class Text:
	"""Represents the Written text """

	def __init__(self, text):
		self._text = text

	def writeBack(self):
		return self._text

class Underline(Text):
	"""Wrapper to Underline the Text"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def writeBack(self):
		return "<u>{}</u>".format(self._wrapped.writeBack())

class Italic(Text):
	"""Wrapper to make Text italic"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def writeBack(self):
		return "<i>{}</i>".format(self._wrapped.writeBack())

class Bold(Text):
	"""Exitsting feature to make Text bold"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def writeBack(self):
		return "<b>{}</b>".format(self._wrapped.writeBack())


if __name__ == '__main__':

    text = Text("Hello World")
    textI = Italic(Text("Python"))    
    textU = Underline(Text("Python Wife"))
    
    print("Original :", text.writeBack())
    print("Italic :", textI.writeBack())
    print("Underlined:", textU.writeBack())

from wordcloud import WordCloud
from Parser import parser
from InfoParser import infoparser

ogg = parser()
ogg.leggi()
wordcloud = WordCloud().generate(text)

#image = wordcloud.to_image()
#image.show()

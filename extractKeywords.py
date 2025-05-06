#Import the key words
f = open('gazetteer.txt','r')
allKeywords = f.read().lower().split("\n")
f.close()

print(allKeywords)
print(len(allKeywords))

#Import the texts you want to search
f = open('text.txt','r')
allTexts = f.read().lower().split("\n")
f.close()

print(allTexts)
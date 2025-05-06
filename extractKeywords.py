#Import the key words
f = open('gazetteer.txt','r')
allKeywords = f.read().lower().split("\n")
f.close()

print(allKeywords)
print(len(allKeywords))

#Import the texts you want to search
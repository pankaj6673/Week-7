sentence1=input("Enter the first sentence ")
sentence2=input("Enter the second sentene ")
Sentences=sentence1+sentence2
print(Sentences)

lastsentencelist=[]
for i in range  (0,len(Sentences)):
    lastsentencelist.append(Sentences[i])
print(lastsentencelist)

lastsentencelist.sort()
print(lastsentencelist)

print(len(lastsentencelist))

lastsentencedictionary={}
count=0
for i in range (0,len(lastsentencelist)):
    for j in range(0,len(lastsentencelist)):
        if lastsentencelist[i]==lastsentencelist[j]:
            count +=1
    lastsentencedictionary[lastsentencelist[i]]=count
    count=0
print(lastsentencedictionary)

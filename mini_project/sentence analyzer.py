print("Sentence analyzer\n\n".center(140))

sentence=input("type your sentence : ").split()

#for no. of words
print("\n no. of words in the sentence are : ", len(sentence))

#for no. of charecters
char="".join(sentence)
print("\n no. oof charecters in the sentence is : " , len(char))

#for longest word 
print("\n the longest word in the sentence is : ", max(sentence,key=len))

#for shortest word
print("\n the shortest word in the sentence is : ", min(sentence,key=len))

#for frequency of each word
freq={}
for x in sentence:
  freq[x]=freq.get(x,0)+1
print(f"\n frequency of words are as follows : {freq}")

#sentence reversed (in word order) like India is beautiful -> beautiful is India # nnot like lufitueab ...... aas for this u can simply use [::-1] in simple sting case not with list
reverse=" ".join(sentence[::-1])
print(f"\n sentence in reverse order is : {reverse}")

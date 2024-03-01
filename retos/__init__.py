def e2(word, index=0):
  if(len(word) == index):
    return ""
  mid = len(word)//2
  if(index < mid):
    return word[index] + e2(word, index+1)
  else:
    return  e2(word, index+1) + word[index]

print(e2("adiospendejosdemierda"))
s="pythanoAFg"
vowels="aeiouAEIOU"
cnt={i:s.count(i) for i in vowels if i in s}
print(cnt)

#or
char_count={}
for i in s:
    if i in vowels:
        if(not i in char_count):
            char_count[i]=0
        char_count[i]+=1
print(char_count)
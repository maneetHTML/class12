word =input("Enter your word :")
char = input("enter you character :") 
count=0
for i in word:
    if i ==char:
        count=count+1
print(char, "is present",count,"times")
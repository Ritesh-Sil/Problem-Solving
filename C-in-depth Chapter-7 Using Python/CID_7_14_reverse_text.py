# Write a recursive function to enter a line of text and display it in reverse order, without sorting the text in an array

def rev_text(text):
    word_list = text.split(" ") #[I , am , a , good, boy]
    if word_list == []:
        print("")
    else:
        temp = word_list[0] #I
        rev_text(" ".join(word_list[2:]))
        print(temp,end='')



text = "I am a good boy"
rev_text(text)

# word_list=['I' , 'am' , 'a' , 'good', 'boy']
# print(' '.join(word_list[1:]))


def sent_maker(phrase):
    interogatives= ("how","when","why","where","what","what's","How's")
    capitalised= phrase.capitalize()  #capitalizes the starting letter 
    if phrase.startswith(interogatives):
        return "{}?".format(capitalised)  #To add '?' after the question
    else:
        return "{}.".format(capitalised)    #To add '.' after the sentence

messege=[]    #The empty list for carrying all the inputs from user
while True:    #creating a loop for taking user input
    user_input= input("Write something:")
    if(user_input== "end"):
        break
    else:
        messege.append(sent_maker(user_input))   # the input will be added in the empty list we created

print(" ".join(messege))   #join function joins all the sentenses
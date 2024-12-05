#def hello(name, age):
#    print("Hello " + name + ", you are " + str(age) + " years old")
    
#hello("Beau", 39)


#def test():
#    age = 8

#    print(age)
    
#print(age)
#test()

#Nestes Function
#def talk(phrase):
    #def say(word):
       # print(word)
        
#    words = phrase.split(' ') #create a list out of a string, print on a new line
 #   for word in words:
  #      say(word)
        
#talk('I am going to buy the milk')

def count():
    count = 0
    
    def increment():
        nonlocal count #allows us to access the variable count whihc was declared inside the func. count,  we can only access it due to the scope with calling it nonlacal
        count = count + 1
        print(count)

    increment()
    
count()

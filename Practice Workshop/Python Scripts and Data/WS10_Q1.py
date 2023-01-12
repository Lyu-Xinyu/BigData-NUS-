# a)	What is 8 to the power 4?
print(8 ** 4)
# b)	Split this string “Split this string”
s = "Split this string"
print(s.split())
# c)	Given the variables: planet = “Earth”, diameter = 12742, use .format() to print the following string “The diameter of Earth is 12742 kilometers.”
planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet, diameter))
# d)	Given the name list, use indexing to grab word “target”, the_list = [1,2,[3,4],[5,[100,200,['target']],23,11],1,7]
the_list = [1,2,[3,4],[5,[100,200,['target']],23,11],1,7]
print(the_list[3][1][2])
# e)	Given this nest dictionary grab the work “hello”. The_dic = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
The_dic = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(The_dic['k1'][3]['tricky'][3]['target'][3])
# f)	Create a basic function that returns True if the word 'elephant' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
def findElephant(st):
    return 'elephant' in st.lower().split()
result = findElephant('Is there an elephant there?')
print("result is: {}".format(result))
# g)	Create a function that counts the number of times the word "elephant" occurs in a string. Again ignore edge cases.
def countElephant(st):
    count = 0
    for word in st.lower().split():
        if word == 'elephant':
            count += 1
    return count
str = "This elephant is heavier than the other elephant dude!"
print(str.lower().split())
num = countElephant(str)
str = ()
print(num)

# h)	Write a function to return one of 3 possible results: "Low speed", "Medium speed", or "Fast speed".
# If your speed is 60 or less, the result is "Low speed". If speed is between 61 and 80 inclusive,
# the result is "Medium speed". If speed is 81 or more, the result is "Fast speed". Unless it is your birthday
# (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed

    if speeding > 80:
        return 'Fast speed'
    elif speeding > 60:
        return 'Medium speed'
    else:
        return 'Low speed'
caught_speeding(81,True)
caught_speeding(60,False)
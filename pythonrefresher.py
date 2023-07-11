#Pound sign for single line comments

"""3 quotation marks for 
multiline comments"""

age = 12
name = 'Nick'
isAdult = False

print(f'hello {name} you are {age} years old')

if age > 18:
    print('you are an adult')
    print('you can vote')
else:
    print('Underage')


def vote(name='Anonymous'):
    print(f'Thank you {name} for voting!')

vote(name)

def voteStatus(num):
    if num > 18:
        return 'Qualified'
    else:
        return 'Disqualified'

status = voteStatus(age)
print(status)

voters = ['Nick', 'Mark', 'Brad', True, 1234, 0.123]
voters[0] = 'John'
voters.insert(3, 'Jane')
print(voters, len(voters))
del(voters[0])
print(voters, len(voters))

for voter in voters:
    print(voter)
print('--------------')

for x in range(1,5):
    print(x)
print('--------------')

dogs = {'Husky': 5, 'Max': 8, 'Molly': 2}
print(dogs)
print(dogs['Max'])

dogs['Rocky'] = 1
dogs['Husky'] = 4
dogs['Harry'] = False
dogs['Billy'] = 'One'


class Dog:
    def bark(self):
        print('Bark!')

    def walk(self, str):
        print(f'Walking to the {str}')

myDog = Dog()
myDog.bark()
myDog.walk('mall')

myDog.name = 'Hulio'
myDog.age = 10


class Dog2:
    def __init__(self, name="", age=0, furcolor=""):
        self.name = name
        self.age = age
        self.furcolor = furcolor

myDog2 = Dog2('Puppy', 1, 'brown')

print(myDog2.name)
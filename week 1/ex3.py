# # problem
# print('Good morning!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good afternoon!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good evening!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')

# solution 1
def askFeeling():
    print('How are you feeling?')
    feeling = input()
    print('I am happy to hear that you are feeling ' + feeling + '.')


print('Good morning!')
askFeeling()
print('Good afternoon!')
askFeeling()
print('Good evening!')
askFeeling()

# solution 2
for timeOfDay in ['morning', 'afternoon', 'evening']:
    print('Good ' + timeOfDay + '!')
    print('How are you feeling?')
    feeling = input()
    print('I am happy to hear that you are feeling ' + feeling + '.')


    # solution 3
    def askFeeling(timeOfDay):
        print('Good ' + timeOfDay + '!')
        print('How are you feeling?')
        feeling = input()
        print('I am happy to hear that you are feeling ' + feeling + '.')


    for timeOfDay in ['morning', 'afternoon', 'evening']:
        askFeeling(timeOfDay)

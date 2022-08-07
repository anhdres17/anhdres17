import random
nums = int(input('How many random numbers would you like to generate? '))
range0 = int(input('Enter the start range: '))
range1 = int(input('Enter the end range: '))
ints = []

def rand_num(y1,y2):
     while len(ints) < nums:
        rand_nums = random.randint(y1,y2)
        if rand_nums not in ints:
                ints.append(rand_nums) #my name is Sam

rand_num(range0,range1)
print(f'Your number(s): {ints}')


#My first rng script on python, more to come. -7/30/22


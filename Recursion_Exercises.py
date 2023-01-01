#Exercise #1
#Filter out all of the empty strings from the list below
#Output: ['Argentina', 'San Diego', 'Boston', 'New York']
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

print(list(filter(lambda city: city.split(), places)))




#Exercise #2
#Write an anonymous function that sorts this list by the last name...
#Hint: Use the ".sort()" method and access the key"
#Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']


authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

authors.sort(key = lambda x: x.lower().split()[-1])


#Exercise #3
#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

#Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angeles', 111.2), ('Miami', 84.2)]

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angeles",44),("Miami",29)]


convert_farhenheit = list(map(lambda temp: (temp[0], temp[1] * 9/5 + 32), places))
print(convert_farhenheit)

#Exercise #4
#Write a recursion function to perform the fibonacci sequence up to the number passed in.
#Output for fib(5) => Iteration 0: 0 Iteration 1: 1 Iteration 2: 1 Iteration 3: 2 Iteration 4: 3 Iteration 5: 5 Iteration 6: 8


def fib_iter(num):
    previous = 1
    current = 0
    i = 0
    while i < num:
        yield current 
        previous, current = current, previous + current 
        i += num

for i,f in enumerate(fib_iter(20)):
    print(f"iteration {i}: {f}")


#Exercise #5
#Create a generator that takes a number argument and yields that number squared, then prints each number squared until zero is reached.

def num_squared(number):
    while number != 0:
        yield number **2
        number -= 1

for x in num_squared(5):
    print(x)

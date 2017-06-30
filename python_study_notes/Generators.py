import random
def luckydraw():
	for i in range(6):
		yield random.randint(1,40)
	yield random.randint(1,15)
for random_number in luckydraw():
	print("And the next number is ...%d!"%(random_number))
	
##the Fibonacci series
# fill in this function
def fib():
    #pass 
    #this is a null statement which does nothing when executed, useful as a placeholder.
    a,b=1,1
    while 1:
        yield a
        a,b=b,a+b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

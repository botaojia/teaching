#!/usr/bin/python3
def test_number():
	print("=================testing immutable - number===================")
	
	def f(local_name):
		print("local_name initial memory address:\t", id(local_name))
		local_name += 1
		print("local_name memory address after +1:\t", id(local_name))


	x = 123
	print("x value (before call f): ", x)
	print("x memory address(before call f): \t",id(x))
	f(x)
	print("x memory address(after call f): \t",id(x))
	print("x value (after call f): ", x)


def test_string():
    print("=================testing immutable - string===================")

    def f(local_name):
        print("local_name initial memory address:\t", id(local_name))
        local_name += '1'
        print("local_name memory address after +'1':\t", id(local_name))


    x = "message"
    print("x value (before call f): ", x)
    print("x memory address(before call f): \t",id(x))
    f(x)
    print("x memory address(after call f): \t",id(x))
    print("x value (after call f): ", x)

def test_tuple():
    print("=================testing immutable - tuple===================")

    def f(local_name):
        print("local_name initial memory address:\t", id(local_name))
        local_name += 4,5
        print("local_name memory address after +(4,5):\t", id(local_name))


    x = 1,2,3
    print("x value (before call f): ", x)
    print("x memory address(before call f): \t",id(x))
    f(x)
    print("x memory address(after call f): \t",id(x))
    print("x value (after call f): ", x)


def test_list():
    print("=================testing mutable - list===================")

    def f(local_name):
        print("local_name initial memory address:\t", id(local_name))
        local_name.append(1)
        print("local_name memory address after +1:\t", id(local_name))


    x = [0,1,2]
    print("x value (before call f): ", x)
    print("x memory address(before call f): \t",id(x))
    f(x)
    print("x memory address(after call f): \t",id(x))
    print("x value (after call f): ", x)

def test_set():
    print("=================testing mutable - set===================")

    def f(local_name):
        print("local_name initial memory address:\t", id(local_name))
        local_name.add(1)
        print("local_name memory address after +1:\t", id(local_name))


    x = {2,3,4}
    print("x value (before call f): ", x)
    print("x memory address(before call f): \t",id(x))
    f(x)
    print("x memory address(after call f): \t",id(x))
    print("x value (after call f): ", x)

def test_dictionary():
    print("=================testing mutable - dictionary===================")

    def f(local_name):
        print("local_name initial memory address:\t", id(local_name))
        local_name['added']=999
        print("local_name memory address after modify:\t", id(local_name))


    x = {'elem1': 111, 'elem2': 222, 'elem3': 333}
    print("x value (before call f): ", x)
    print("x memory address(before call f): \t",id(x))
    f(x)
    print("x memory address(after call f): \t",id(x))
    print("x value (after call f): ", x)

#immutable builtin
test_number()
test_string()
test_tuple()

#mutable builtin
test_list()
test_dictionary()
test_set()


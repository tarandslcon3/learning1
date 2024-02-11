# def least_difference(a, b, c):
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     return min(diff1, diff2, diff3)

# a  = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# print (a,b,c, sep='<')
# result = least_difference(a, b, c)
# print("The least difference is:", result)

# def greet(who="Colin"):
#     print("Hello,", who)
    
# greet()
# # greet(who="Kaggle")
# # (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
# # greet("world")


# def mult_by_five(x):
#     return 5 * x

# def call(fn, arg):
#     """Call fn on arg"""
#     return fn(arg)

# def squared_call(fn, arg):
#     """Call fn on the result of calling fn on arg"""
#     return fn(fn(arg))

# print(
#     call(mult_by_five, 1),
#     squared_call(mult_by_five, 1), 
#     sep='\n', # '\n' is the newline character - it starts a new line
# )

# def ruound_to_two_places(x=9.91999):
#     return round(x,2)

# a =ruound_to_two_places()
# print (a)


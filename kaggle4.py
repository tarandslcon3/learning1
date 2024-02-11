def to_smash(total_candies):
    print("Splitting", total_candies, "candies")
    return total_candies % 3

# Call the function with the argument 91
for x in range(5,13):

    return_value = to_smash(x)

# Check the return value
    if return_value == 1:
        print("Splitting 1 candy")
    else:
        print("Splitting", return_value, "candies")

# Here's a slightly more succinct solution using a conditional expression:
#print("Splitting", return_value, "candy" if return_value == 1 else "candies")

class PostiveNumberTuple(tuple):

    def __new__(cls, *numbers):
        skipped_values_count = 0
        positive_numbers = []
        for x in numbers:
            if x >=0:
                positive_numbers.append(x)
            else:
                skipped_values_count += 1

        instance = super().__new__(cls,tuple(positive_numbers))
        instance.skipped_values_count = skipped_values_count
        return instance

        #return super().__new__(cls,tuple(positive_numbers))

input_tuple = PostiveNumberTuple(-3,-2,-1,0,1,2,4,7,9)
print(input_tuple)
print(type(input_tuple))
print(input_tuple.skipped_values_count)
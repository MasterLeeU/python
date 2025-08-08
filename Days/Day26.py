# List and Dictionary Comprehension
import random
#numbers = [1,2,3]
#new_numbers = [n + 1 for n in numbers]
#squared_numbers = [n*n for n in numbers]
#evens = [en%2 ==0 for en in numbers]
#results = [num for num in numbers if num % 2 == 0]

#name ="Lee"
#letters_list =[letter for letter in name]
#range_list = [num * 2 for num in range(1,5)]
#names = ["Lee", "Dean", "Francis", "Matt", "Remith"]
#short_names =[name for name in names if len(name) <5]
#long_names = [name.upper() for name in names if len(name) >5]

#ith open("f1.txt") as f1:
 #  f1_list = f1.readlines()
   
#ith open("f2.txt") as f2:
#   f2_list = f2.readlines()
          
#esults = [int(num) for num in f1_list if num in f2_list]
#rint(results)

#scores = {name:random.randint(1, 100) for name in names}
#passed = {                    (names,scores) in scores.items()

import pandas

data = pandas.read_csv"nato_alpha.csv"


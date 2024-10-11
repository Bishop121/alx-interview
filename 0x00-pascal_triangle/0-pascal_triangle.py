#!/usr/bin/python3
    """function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """


def pascal_triangle(n):
  """
   Args
  n(int): length of triangle (assume n will be always an integer)
  return: list of lists representing the Pascal’s triangle of n  """
 if n <= 0:
 return []

 if n == 1:
 ret_list = pascal_triangle(0)
 ret_list.append([1])
 return ret_list

 if n == 2:
 ret_list = pascal_triangle(1)
 ret_list.append([1, 1])
 return ret_list

 if n > 2:
ret_list = pascal_triangle(2)
for i in range(n-2):    
new_row = []
last_row = ret_list[-1]
for index, value in enumerate(last_row):
if index == 0:
new_row.append(value)
next_value = last_row[index + 1]
new_row.append(value + next_value)

                                                                                                                                                                                                                    elif index == len(last_row)-1:                                                                                                                                                                                     new_row.append(value)

                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                    next_value = last_row[index + 1]
                                                                                                                                                                                                                    new_row.append(value + next_value)

                                                                                                                                                                                                                    ret_list.append(new_row)

                                                                                                                                                                                                                
return ret_list


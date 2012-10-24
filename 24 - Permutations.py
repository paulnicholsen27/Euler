import itertools
import math

perms = list(itertools.permutations(range(10)))
answer = perms[999999]
joined_answer = ''.join(str(i) for i in answer)
print joined_answer
# perms_list = [''.join(item) for item in str(perms)]
# print perms_list



# import itertools
# import math
# 
# answers = []
# perms = list(itertools.permutations(range(10)))
# for item in perms:
# 	joined_answer = ''.join(str(i) for i in item)
# 	ansers
# answer = perms[1000000]
# joined_answer = ''.join(str(i) for i in answer)
# print joined_answer
# # perms_list = [''.join(item) for item in str(perms)]
# # print perms_list

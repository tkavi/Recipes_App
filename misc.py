# # Guess the number game
# # 1. Allow user to guess the number in 7 chances
# # 2. If the number guessed by user is greater or smaller than the number generated notify user about it .
# # 3. If the user is able to guess the number correctly you need to congratulate the user and and you need to tell in
# #    how many attempt the user cracked it
# #    Congratulations !!! You cracked the number in 4 attempts
# # 4. If the user is not able to crack the number , you need to say all chances exhausted.
#
# import random
#
# comp_num = random.randint(1,100)
# # print("comp_num",comp_num)
#
# for i in range(1,8):
#     user_num = int(input("Enter Num btw 1 to 100: "))
#     if comp_num == user_num :
#         print("Congratulations !!! You cracked the number in "+str(i)+" attempts")
#         break
#     elif user_num > comp_num:
#         print("input is greater than comp_num")
#     else:
#         print("input is less than comp_num")
# else:
#     print("All chances exhausted,correct number is ",comp_num)
#

#to encrypt and verify password
from passlib.hash import pbkdf2_sha256

password = "hello"
hashed = pbkdf2_sha256.hash(password)
print(hashed)

if pbkdf2_sha256.verify("hello",hashed):
    print("Password match successfully")

else:
    print("Password doesnt match")
# count = 1
# while count <= 5:
#     print("dipendra")
#     count += 1

# ----------------------------

# i = 0
# names = ["dipendra", "khan", "choudhary"]
# while i <= len(names)-1:
#     print(names[i])
#     i += 1

# ----------------------------

# i = 5
# j = 1
#
# while i > 1:
#     print("telusko", end="")
#     while j <= 4:
#         print(" Rocks", end='')
#         j += 1
#     j = 1
#     i -= 1
#     print()

# ----------------------------

#
# x = ["naveen", 3, 5, 6, "test", 19.6]
# for i in x:
#     print(i)

# ----------------------------

# for i in range(1,21):
#     if (i%5!=0):
#         print(i)

# ----------------------------

# av = 5
# x = int(input("how many candies you need? "))
# i = 1
# while i <= x:
#     if i <= av:
#         print("Candy")
#     else:
#         print("Out of stock")
#         break
#     i = i + 1

# ----------------------------
#skip printing number disvsbkle of 3 or 5 using continue
# i = 1
# while i in range(101):
#     if i % 3 != 0:
#         print(i)
#     i = i + 1
#

#here contniue will just skip execution of remiang steps for that loop and but not break loop.
# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         continue
#     print(i)
#
# print("Bye")

# ----------------------------
#usinbg pass as we can left if block blank it will give issue.
for i in range(1,101):
    if (i%2!=0):
        pass
    else:
        print(i)
print("bye")
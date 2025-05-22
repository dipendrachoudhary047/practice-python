# #Solution1
#
# message = "i love my india very much"
# message_list = message.split(' ')
# reverse = message_list[::-1]
# final_string = ' '.join(reverse)
# print(final_string)


#Solution2
message = "i love my india very much"
message_list = message.split(' ')
reverse_list = []
for item in message_list:
    reverse_list = [item] + reverse_list

print(reverse_list)
string = ' '.join(reverse_list)
print(string)

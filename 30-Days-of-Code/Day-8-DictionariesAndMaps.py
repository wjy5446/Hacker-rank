number_name = int(input().strip())
dict_phone = {}

for i in range(number_name):
    name, phone = input().strip().split(" ")
    dict_phone[name] = phone

for i in range(number_name):
    query_name = input().strip()

    if query_name in dict_phone:
        print("{}={}".format(query_name, dict_phone[query_name]))
    else:
        print("Not found")

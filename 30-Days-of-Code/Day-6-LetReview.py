user_input = int(input())
list_st = []

for _ in range(user_input):
    list_st.append(input())

for s in list_st:
    st = ""
    # print odd
    for idx in range(0, len(s), 2):
        st += s[idx]

    st += " "

    # print even
    for idx in range(1, len(s), 2):
        st += s[idx]

    print(st)

import operator


def solution(test_list):

    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                poss_ans = ""
                for l in range(len(test_list)):
                    if l % 3 == 0:
                        temp_num = operator.xor(i, test_list[l])
                    elif l % 3 == 1:
                        temp_num = operator.xor(j, test_list[l])
                    else:
                        temp_num = operator.xor(k, test_list[l])
                    poss_ans += chr(temp_num)

                if "the" in poss_ans and "and" in poss_ans and "of" in poss_ans and "in" in poss_ans:
                    print(f"The code might be {chr(i)}{chr(j)}{chr(k)}")
                    ans_sum = sum(ord(ans) for ans in poss_ans)
                    print(ans_sum)


def compute():

    with open("../euler_files/p059_cipher.txt", "r") as file:

        our_list = []
        temp_char = ""
        for item in file.read():
            if item == ",":
                our_list.append(int(temp_char))
                temp_char = ""
            else:
                temp_char += item
        our_list.append(int(temp_char))

        solution(our_list)


if __name__ == '__main__':

    compute()

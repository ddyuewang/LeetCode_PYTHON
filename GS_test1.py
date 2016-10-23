def encode(input_string):
    count = 1
    prev = ''
    lst = ''
    for character in input_string:
        if character != prev:
            if prev:
                entry = str(count) + prev
                lst = lst + entry
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = str(count) + character
        lst = lst + entry
    return lst


def encode_1(input_string):

    res = {}
    res_name = []
    result = ''
    for character in input_string:
        if character in res.keys():
            res[character] += 1
        else:
            res[character] = 1
        res_name.append(character)
    for item in res_name:
        result = result + item + str(res[item])
    return result

# def decode(lst):
#     q = ""
#     for character, count in lst:
#         q += character * count
#     return q

if __name__ == "__main__":
    tmp = encode("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
    print(tmp)
    tmp1 = encode_1("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
    print(tmp1)

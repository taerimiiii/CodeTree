def shift(List) :
    lenth = len(List)
    temp = List[lenth - 1]
    for i in range(lenth - 1, 0, -1) :
        List[i] = List[i - 1]
    List[0] = temp
    return List

def run_length_encoding(List) :
    lenth = len(List)
    RLE_list = []
    count = 1
    for i in range(lenth - 1) :
        if i == lenth - 2 :
            if List[i] == List[i + 1] :
                count += 1
                RLE_list.append(List[i])
                RLE_list.append(count)
                if count == 10 :
                    RLE_list.append('0')
                break
            else :
                RLE_list.append(List[i])
                RLE_list.append(count)
                count = 1
                RLE_list.append(List[i + 1])
                RLE_list.append(count)
                break
        
        if List[i] == List[i + 1] :
            count += 1
        else :
            RLE_list.append(List[i])
            RLE_list.append(count)
            count = 1

    #print(RLE_list)
    RLE_len = len(RLE_list)
    return RLE_len

string_a = input()

lenth = len(string_a)
list_a = ['a'] * lenth
for i in range(lenth) :
    list_a[i] = string_a[i]

min_len = 20
for _ in range(lenth) :
    RLE_a_len = run_length_encoding(list_a)
    min_len = min(min_len, RLE_a_len)
    list_a = shift(list_a)

print(min_len)
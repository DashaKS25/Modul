def spam(number):
    return 'bulochka' * int(number)


def my_sum(list_of_numbers):
    result = 0
    for num in list_of_numbers:
        result += num
    return result



def shortener(string):
    words = string.split()
    for i in range(len(words)):
       if len(words[i]) > 6:
           words[i] = words[i][:6] + '*'
    return ' '.join(words)

def compare_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count
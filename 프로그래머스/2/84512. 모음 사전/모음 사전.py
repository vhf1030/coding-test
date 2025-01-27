def get_words_all(word_list: list) -> list:
    word_list_new = [word + next_word for word in word_list for next_word in 'AEIOU_']
    if len(word_list_new[0]) == 5:
        return word_list_new
    else:
        return get_words_all(word_list_new)

def solution(word):
    words_all = get_words_all([''])
    words_set = set([words.replace('_', '') for words in words_all])
    answer = sorted(list(words_set)).index(word)
    return answer


# A____  1
# AA___  2
# AAA__  3
# AAAA_  4
# AAAAA  5
# AAAAE  6
# AAAAI  7
# AAAAO  8
# AAAAU  9
# AAAE_  10
# AAAEA  11

# A____ : (5**4 + 5**3 + 5**2 + 5**1 + 5**0) * 0 + 1
# E____ : (5**4 + 5**3 + 5**2 + 5**1 + 5**0) * 1 + 1
# I____ : (5**4 + 5**3 + 5**2 + 5**1 + 5**0) * 2 + 1

def solution(word):
    vowels = "AEIOU"
    digit_weights = [
        5**4 + 5**3 + 5**2 + 5**1 + 5**0,
        5**3 + 5**2 + 5**1 + 5**0,
        5**2 + 5**1 + 5**0,
        5**1 + 5**0,
        5**0
    ]
    answer = 0
    for i, c in enumerate(word):
        idx_c = vowels.index(c)
        answer += digit_weights[i] * idx_c + 1
    
    return answer
    




def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    return ''.join([a for a in my_string if a not in vowel])
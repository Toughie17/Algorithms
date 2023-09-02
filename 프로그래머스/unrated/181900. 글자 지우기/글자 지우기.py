def solution(my_string, indices):
    # sol = ''
    # for i in range(len(my_string)):
    #     if i not in indices:
    #         sol += my_string[i]
    # return sol

    return ''.join([my_string[i] for i in range(len(my_string)) if i not in indices])
    
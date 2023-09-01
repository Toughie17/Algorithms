def solution(arr, delete_list):
    # result = []
    # for num in arr:
    #     if num not in delete_list:
    #         result.append(num)
    # return result

    # 빈 배열을 만들고, 해당 배열에 추가하는 로직은 리스트 컴프리헨션을 사용해 보자.
    
    return [ num for num in arr if num not in delete_list]
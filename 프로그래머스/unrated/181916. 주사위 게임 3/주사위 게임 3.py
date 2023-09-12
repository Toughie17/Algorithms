
def solution(a, b, c, d):
    dice_list = [a,b,c,d]
    no_dup = list(set(dice_list))
    
    if len(no_dup) == 1:
        return 1111 * no_dup[0]
    
    elif len(no_dup) == 2:
        for ele in dice_list:
        # 1개 3개인 경우
            if dice_list.count(ele) == 3:
                p = ele
                q = [x for x in no_dup if x != p][0]
                return (10 * p + q) ** 2
        # 2개 2개인 경우
            elif dice_list.count(ele) == 2:
                p = ele
                q = [x for x in no_dup if x != p][0]
                return (p + q) * (abs(p - q))
            
    elif len(no_dup) == 3:
        #1개, 1개, 2개인 경우
        for ele in dice_list:
            if dice_list.count(ele) == 2:
                pq_list = [x for x in no_dup if x != ele]
                return pq_list[0] * pq_list[1]
        
    elif len(no_dup) == 4:
        return min(no_dup)
    
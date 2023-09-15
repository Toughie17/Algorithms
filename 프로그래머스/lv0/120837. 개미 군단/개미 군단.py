def solution(hp):
    general = hp // 5
    soldier = (hp - 5 * general) // 3
    worker = (hp - 5 * general - 3 * soldier)
    
    return (general + soldier + worker)
    
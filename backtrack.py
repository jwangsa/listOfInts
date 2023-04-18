def combo(num, target, part = []):
    s = sum(part)
    
    if s == target:
        return part

    if s >= target:
        return None

    for i in range(0, len(num)):
        n = num[i]
        remaining = num[i+1:]
        result = combo(remaining, target, part + [n])
        
        if result is not None:
            return result

    return None

def isValid(s: str) -> bool:
    list = []
    pairs = {'{': '}', '(': ')', '[': ']'}
    for curr in s:
        if curr in pairs:
            list.append(curr)
        elif list and pairs.get(list[-1]) == curr:
            list.pop()
        else:
            return False
    return not list

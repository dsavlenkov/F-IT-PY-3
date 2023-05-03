def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    if brackets_row == "":
        return True
    elif brackets_row[0] == ")":
        return False

    stack = []

    for bracket in brackets_row:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")" and len(stack) != 0:
            stack.pop()
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False

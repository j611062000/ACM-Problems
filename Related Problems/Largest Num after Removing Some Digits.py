def removing_m_digits(m, d):
    stack = []

    for count, digit in enumerate(d):
        isEnoughDigits = len(stack) + m + 1 > count + 1
        isDigitGreatEnough = (digit > stack[-1]) if stack else True
        while stack and isEnoughDigits and isDigitGreatEnough:

            stack.pop()

        if len(stack) < len(d) - m:
            stack.append(digit)

    return stack


if __name__ == '__main__':
    m = 2
    d = [1,1,9,9,9]
    print(removing_m_digits(m, d))

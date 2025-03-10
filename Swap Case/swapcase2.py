def swap_case(s):
    result = []  # Use a list for efficiency
    for ch in s:
        if ch.isupper():
            result.append(ch.lower())  # Convert to lowercase
        elif ch.islower():
            result.append(ch.upper())  # Convert to uppercase
        else:
            result.append(ch)  # Keep non-alphabetic characters unchanged
    return "".join(result)  # Convert list back to string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

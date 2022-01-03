def swap_case(s):
    swaped = ""
    for letter in s:
        if letter.isupper():
            swaped += letter.lower()
        else:
            swaped += letter.upper()
    return swaped

if __name__ == '__main__':

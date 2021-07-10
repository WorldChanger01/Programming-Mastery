def romanTonum(s):
    '''
    This program converts roman numerals to numbers.
    It is easier to solve the problem looking at the roman numeral in the reversed form.
    The trick here is to simply use a reversed string and a dictionary.
    This program works for numbers 1 to 3999

    '''
    dict_rn = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    t = s[::-1]
    total = 0
    sto = 0
    for elem in t:
        if dict_rn[elem] >= sto:
            total += dict_rn[elem]
        else:
            total -= dict_rn[elem]
        sto = dict_rn[elem]
    return total


if __name__ == "__main__":
    print(romanTonum("MCXLVII"))

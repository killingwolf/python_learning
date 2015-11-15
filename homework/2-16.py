#!/usr/bin/python
# coding:utf-8


def main(number):
    """ 数字转化为英文单词
    """
    dict1 = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
        70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred",
        1000: "thousand"
    }
    if number <= 20:
        return dict1[number]
    elif number < 100:
        t = number / 10 * 10
        if number % 10 == 0:
            return "%s" % (dict1[t])
        else:
            return "%s-%s" % (dict1[t], dict1[number - t])
    elif number < 1000:
        h = number / 100
        tt = number % 100
        if number % 100 == 0:
            return "%s-%s" % (dict1[h], dict1[100])
        else:
            t = tt / 10 * 10
            if number % 10 == 0:
                return "%s-%s-%s" % (dict1[h], dict1[100], dict1[t])
            else:
                if tt <= 20:
                    return "%s-%s-%s" % (dict1[h], dict1[100], dict1[tt])
                else:
                    return "%s-%s-%s-%s" % (
                        dict1[h],
                        dict1[100],
                        dict1[t],
                        dict1[tt - t]
                    )
    elif number == 1000:
        return "%s-%s" % (dict1[1], dict1[1000])
    else:
        return "number too larger"


if __name__ == "__main__":
    print main(87)

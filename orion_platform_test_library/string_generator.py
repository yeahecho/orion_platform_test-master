# -*- coding: utf-8 -*-
# !/usr/bin/env python
import string
from itertools import chain
from random import choice, sample


# default: str_generator(Total_length=0, digits=0, upper=0, lower=0, char=0)
# Char mean "Special Character", only allow 2 options: 0 = No characters; 1 = Use default characters
# Please don't try any Negative Number ^_^ #

def str_generator(length=0, digits=0, upper=0, lower=0, char=0):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    email_char_accept = "!#$%&'*+-/=?^_`{|}~"
    try:
        if length < 0 or digits < 0 or upper < 0 or lower < 0 or char < 0:
            # Negative int data is not right
            return 'Error 01: You have a negative length, please double check!'
        elif char != 0:
            if char == 1:
                sp_char = email_char_accept
            else:
                sp_char = char
            if (length - digits - upper - lower) >= 0:
                ran_str = list(
                    # chain()函数的功能是将一组迭代器对象连接起来，chain()里有三个生成器表达式随机选择指定个数的字符
                    chain(
                        (choice(uppercase) for _ in range(upper)),
                        (choice(lowercase) for _ in range(lower)),
                        (choice(string.digits) for _ in range(digits)),
                        (choice(sp_char) for _ in range((length - digits - upper - lower)))
                    )
                )
                return ''.join(sample(ran_str, len(ran_str)))
            else:
                return 'Error 02: Wrong assigned length, please double check!'
        elif char == 0:
            if (length - digits - upper - lower) == 0:
                ran_str = list(
                    chain(
                        (choice(uppercase) for _ in range(upper)),
                        (choice(lowercase) for _ in range(lower)),
                        (choice(string.digits) for _ in range(digits))
                    )
                )
                return ''.join(sample(ran_str, len(ran_str)))
            else:
                return 'Error 02: Wrong assigned length, please double check!'
    except TypeError as te:
        return 'TypeError: ', te


def email_generator(option=0):
    # Email Address Limit: local part {64} @ domain part {255}
    # option = 0, standard email address => lower{5} + digits{5} @ lower{10} . lower{3} => Y
    # option = 1, before @ add '_' => lower{5} + digits{5}  + '_' @ lower{10} . lower{3} => Y
    # option = 2, before @ add '.' => lower{5} + digits{5}  + '.' @ lower{10} . lower{3} => Y
    # option = 3, before @ only 'A-Z' => upper{10} @ lower{10} . lower{3} => Y
    # option = 4, before @ only 'char' => char{10} @ lower{10} . lower{3} => N
    # option = 5, after @ before . add '-' => lower{5} + digits{5} @ lower{5} + '-' + lower{5} . lower{3} => Y
    # option = 6, after @ before . add '.' => lower{5} + digits{5} @ lower{5} + '.' + lower{5} . lower{3} => Y
    # option = 7, after @ before . only 'A-Z' => lower{5} + digits{5} @ upper{10} . lower{3} => Y
    # option = 8, after @ before . only 'char' => lower{5} + digits{5} @ char{10} . lower{3} => N
    # option = 9, after . add '_' => lower{5} + digits{5} @ lower{10} . lower{1} + '_' + lower{2} => N
    # option = 10, after . only 'A-Z' => lower{5} + digits{5} @ lower{10} . upper{3} => Y
    # option = 11, after . only 'char' => lower{5} + digits{5} @ lower{10} . char{3} => N
    # option = 12, before @ length {63} => lower + digits{63} @ lower{10} . lower{3} => Y
    # option = 13, before @ length {65} => lower + digits{65} @ lower{10} . lower{3} => N
    # option = 14, after @ length {254} => lower + digits{10} @ lower{252} . lower{1} => Y
    # option = 15, after @ length {256} => lower + digits{10} @ lower{252} . lower{3} => N
    # option = 16, No '@' => lower{5} + digits{5} + lower{10} . lower{3} => N
    # option = 17, No '.' => lower{5} + digits{5} + lower{10} lower{3} => Y
    # option = 18, multiple '@' => lower{5} @ digits{5} @ letter{10} . lower{3} => N
    # option = 19, two '.' together => lower{5} + '..' + digits{5} @ lower{10} . lower{3} => N
    dict_email = {
        0: {0: 'lower{5} + digits{5} @ lower{10} . lower{3}',
            1: str_generator(10, digits=5, lower=5) + '@' + str_generator(10, lower=10) + '.' + str_generator(3,
                                                                                                              lower=3),
            2: 'Should Pass'},
        1: {0: "before @ add '_'",
            1: str_generator(10, digits=5, lower=5) + '_' + '@' + str_generator(10, lower=10) + '.' + str_generator(3,
                                                                                                                    lower=3),
            2: 'Should Pass'},
        2: {0: "before @ add '.'",
            1: str_generator(10, digits=5, lower=5) + '.' + '@' + str_generator(10, lower=10) + '.' + str_generator(3,
                                                                                                                    lower=3),
            2: 'Should Pass'},
        3: {0: "before @ only 'A-Z'",
            1: str_generator(10, upper=10) + '@' + str_generator(10, lower=10) + '.' + str_generator(3, lower=3),
            2: 'Should Pass'},
        4: {0: "before @ only 'char'",
            1: str_generator(10, char=1) + '@' + str_generator(10, lower=10) + '.' + str_generator(3, lower=3),
            2: 'Should NOT Pass'},
        5: {0: "after @ before . add '-'",
            1: str_generator(10, digits=5, lower=5) + '@' + str_generator(5, lower=5) + '-' + str_generator(5,
                                                                                                            lower=5) + '.' + str_generator(
                3, lower=3), 2: 'Should Pass'},
        6: {0: "after @ before . add '.'",
            1: str_generator(10, digits=5, lower=5) + '@' + str_generator(5, lower=5) + '.' + str_generator(5,
                                                                                                            lower=5) + '.' + str_generator(
                3, lower=3), 2: 'Should Pass'},
        7: {0: "after @ before . only 'A-Z'",
            1: str_generator(10, digits=5, lower=5) + '@' + str_generator(10, upper=10) + '.' + str_generator(3,
                                                                                                              lower=3),
            2: 'Should Pass'},
        8: {0: "after @ before . only 'char'",
            1: str_generator(10, digits=5, lower=5) + '@' + str_generator(10, char=1) + '.' + str_generator(3, lower=3),
            2: 'Should NOT Pass'},
        9: {0: "after . add '_'",
            1: str_generator(10, digits=5, lower=5) + '@' + str_generator(10, lower=10) + '.' + str_generator(1,
                                                                                                              lower=1) + '_' + str_generator(
                2, lower=2), 2: 'Should NOT Pass'},
        10: {0: "after . only 'A-Z'",
             1: str_generator(10, digits=5, lower=5) + '@' + str_generator(10, lower=10) + '.' + str_generator(3,
                                                                                                               upper=3),
             2: 'Should Pass'},
        11: {0: "after @ before . only 'A-Z'",
             1: str_generator(10, digits=5, lower=5) + '@' + str_generator(10, upper=10) + '.' + str_generator(3,
                                                                                                               char=1),
             2: 'Should NOT Pass'},
        12: {0: "before @ length {63}",
             1: str_generator(63, digits=33, lower=30) + '@' + str_generator(10, lower=10) + '.' + str_generator(3,
                                                                                                                 lower=3),
             2: 'Should Pass'},
        13: {0: "before @ length {65}",
             1: str_generator(65, digits=33, lower=32) + '@' + str_generator(10, lower=10) + '.' + str_generator(3,
                                                                                                                 lower=3),
             2: 'Should NOT Pass'},
        14: {0: "after @ length {254}",
             1: str_generator(10, digits=5, lower=5) + '@' + str_generator(252, lower=252) + '.' + str_generator(1,
                                                                                                                 lower=1),
             2: 'Should Pass'},
        15: {0: "before @ length {256}",
             1: str_generator(10, digits=5, lower=5) + '@' + str_generator(252, lower=252) + '.' + str_generator(3,
                                                                                                                 lower=3),
             2: 'Should NOT Pass'},
        16: {0: "No '@' ",
             1: str_generator(10, digits=5, lower=5) + str_generator(10, lower=10) + '.' + str_generator(3, lower=3),
             2: 'Should NOT Pass'},
        17: {0: "No '.'",
             1: str_generator(10, digits=5, lower=5) + '@' + str_generator(10, lower=10) + str_generator(3, lower=3),
             2: 'Should Pass'},
        18: {0: "multiple '@'",
             1: str_generator(5, digits=5) + '@' + str_generator(5, lower=5) + '@' + str_generator(10,
                                                                                                   lower=10) + '.' + str_generator(
                 3, lower=3), 2: 'Should NOT Pass'},
        19: {0: "two '.' together",
             1: str_generator(5, digits=5) + '..' + str_generator(5, lower=5) + '@' + str_generator(10,
                                                                                                    lower=10) + '.' + str_generator(
                 3, lower=3), 2: 'Should NOT Pass'}
    }
    if option in dict_email:
        test_condition = dict_email[option][0]
        test_unit = dict_email[option][1]
        expect_result = dict_email[option][2]
        return test_condition, test_unit, expect_result
    else:
        return 'Cannot find your condition, please review the documents for more detail.'


def pass_generator(option=0):
    # Password, default length is 6, min 1 number and 1 letter
    # option 0, preset password => length=6, digits=3, lower=3 => Y
    # option 1, length {5} => length=5, digits=3, lower=2 => N
    # option 2, length {10} add upper => length=10, digits=3, upper=4, lower=3 => Y
    # option 3, length {10} add char => length=10, digits=3, lower=3, char=4 => Y
    # option 4, length {32} => length=32, digits=3, upper=2, lower=2, char=1 => Y
    dict_pass = {
        0: {0: 'preset password => length=6, digits=3, lower=3',
            1: str_generator(6, digits=3, lower=3),
            2: 'Should Pass'},
        1: {0: 'length=5, digits=3, lower=2',
            1: str_generator(5, digits=3, lower=2),
            2: 'Should NOT Pass'},
        2: {0: 'length=10, digits=3, upper=4, lower=3',
            1: str_generator(10, digits=3, upper=4, lower=3),
            2: 'Should Pass'},
        3: {0: 'length=10, digits=3, lower=3, char=1',
            1: str_generator(10, digits=3, lower=3, char=1),
            2: 'Should Pass'},
        4: {0: 'length=32, digits=3, upper=2, lower=2, char=1',
            1: str_generator(32, 3, 2, 2, 1),
            2: 'Should Pass'},
    }
    if option in dict_pass:
        test_condition = dict_pass[option][0]
        test_unit = dict_pass[option][1]
        expect_result = dict_pass[option][2]
        return test_condition, test_unit, expect_result
    else:
        return 'Cannot find your condition, please review the documents for more detail.'


# return [condition, test unit, expect result]
# print(email_generator(1))
# print(type(email_generator(1)))
# print(pass_generator(1))
# print(type(pass_generator(1)))
print("___", pass_generator(1)[1])

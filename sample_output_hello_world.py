#!/usr/bin/env python3
'''output "Hello world!" to standard output.
Input : None
return : None
'''


# -----------------------------------------------------------------------------
#  Functions
# -----------------------------------------------------------------------------

def print_def():
    print("Hello world!")


# -----------------------------------------------------------------------------
#  Main script
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    # print()関数
    print("Hello world!")

    # print(end='')
    print("Hello ", end='')
    print("world!")

    # print(end=' ')
    print("Hello", end=' ')
    print("world!")

    # print(.format notation)
    message = "Hello world!"
    print("{0}" .format(message))

    # print(.format notation 2 variables)
    message1 = "Hello"
    message2 = "world!"
    print("{0} {1}" .format(message1, message2))

    # print(% notation)
    message = "Hello world!"
    print("%s" % message)

    # print(% notation 2 variables
    message1 = "Hello"
    message2 = "world!"
    print("%s %s" % (message1, message2))

    # print(+ notation)
    message1 = "Hello"
    message2 = "world!"
    print(message1 + " " + message2)

    # print(f書式)関数
    print(f"Hello world!")

    # 変数(定数)を使用
    MESSAGE_CONST = "Hello world!"
    print(MESSAGE_CONST)

    # 変数を使用
    message_variable = "Hello world!"
    print(message_variable)

    # 変数とprint(f書式)を使用
    print(f"{message_variable}")

    # リストとprint()関数を使用
    list_ = ("Hello world!")
    print(list_)

    # リストとprint(f書式)を使用
    list_ = ("Hello world!")
    print(f"{list_}")

    # タプルとprint()関数を使用
    tuple_ = ["Hello world!"]
    print(tuple_[0])

    # タプルとprint(f書式)を使用
    tuple_ = ["Hello world!"]
    print(f"{tuple_[0]}")
    
    # 関数をコール
    print_def()

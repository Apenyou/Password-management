import hashlib
import random


def strtomd5(passwordstring):
    """
    接收参数，生成md5,取中间13位
    """
    md5hash = hashlib.md5(passwordstring.encode())
    md5pass = md5hash.hexdigest()
    return md5pass[9:-10]


def strspecial(passwordstring):
    """
    替换三个字符为特殊符号
    """
    passwordstring = list(passwordstring)
    special = ',.=-&^%$@#'
    special_c = random.sample(special, k=int(len(passwordstring) / 4))
    target = random.sample(range(0, len(passwordstring)), k=int(len(passwordstring) / 4))
    for index, target_v in enumerate(target):
        passwordstring[(target_v)] = special_c[index]
    return ''.join(passwordstring)


def strcapital(passwordstring):
    """
    转一般字母为大写
    """
    numb = int(len(passwordstring) / 2)
    passwordstring_1 = passwordstring[numb:]
    passwordstring_2 = passwordstring_1.swapcase()
    passwordstring = passwordstring_2 + passwordstring[:numb]
    return passwordstring


def pwdproduce(root, appname):
    md5 = strtomd5(root + appname)
    special = strspecial(md5)
    capital = strcapital(special)
    return capital


if __name__ == "__main__":
    root = '123123'
    appname = '微信'
    pwd = pwdproduce(root, appname)
    print(pwd)

import base64

def base64encode(pwd):

    bytesString = pwd.encode(encoding="utf-8")
    encodestr = base64.b64encode(bytesString)
    return(encodestr.decode())

def base64decode(pwd):

    decodestr = base64.b64decode(pwd)
    return(decodestr.decode())


if __name__ == '__main__':
    
    pwd = '345erfg345regre44554'
    base64pwd = base64encode(pwd)
    print(base64pwd)
    print(base64decode(base64pwd))
# import re
def textParser(plaintext:str) -> list:
    returnArray = []
    urls = plaintext.decode("utf-8").split('\n')
    for eachUrl in urls:
        if not "#" in eachUrl:
            returnArray.append(eachUrl.strip())
    
    return returnArray

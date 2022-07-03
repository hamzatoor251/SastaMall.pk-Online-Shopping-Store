def pswdcheck(pw):
    sAlpha=cAlpha=numeric=False
    for i in pw:
        if i.islower():
            sAlpha=True
        if i.isupper():
            cAlpha=True
        if i.isdigit():
            numeric=True
    if(sAlpha and cAlpha and numeric):
        return True
    return False

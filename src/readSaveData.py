

def readDataTxt(file) -> str:
    with open(file, "r") as f:
        txt = f.read()
    return txt

def saveDataTxt(file, txt) -> None:
    with open(file, "w") as f:
        f.write(txt)
    return

def readfile(path):
    binaryContent = open(path, "rb")
    content = binaryContent.read()
    return content

'''
Input -> path(str)
Output -> the content of the file as str
'''
def GetFileContents(path):
  f = open(path, 'r')
  return f.read()

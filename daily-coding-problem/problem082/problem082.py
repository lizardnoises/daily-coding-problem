__author__ = 'Sean Moore'

'''
Daily Coding Problem 82

Using a read7() method that returns 7 characters from a file, implement
readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns
“Hello w”, “orld” and then “”.


I will use camelCase here to be consistant with the prompt. My initial thought
is that we can use file rewinding via seek in conjunction with read7, but that
might be contrary to the point of the question because it's essentially
circumventing the restrictions of read7. A simpler problem interpretation does
not constrain the position of the file pointer after calling readN.
'''

def read7(f):
    '''
    Returns the next 7 characters that can be read from the file handled by the
    given file object.
    '''
    return f.read(7)

def readN(f, n):
    '''
    Returns the next n characters that can be read from the file handled by the
    given file object.
    '''
    buffer = ''
    i = 0
    while i < n:
        buffer += read7(f)
        i += 7
    return buffer[:n]

class FileReadContext:
    def __init__(self, fileName):
        self.fileName = fileName
        self.buffer = ''
    
    def __enter__(self):
        self.f = open(self.fileName, 'r')
        return self
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.f.close()
    
    def _readBuffer(self, n):
        temp = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return temp

    def read7(self):
        n = 7
        temp = self._readBuffer(n)
        n -= len(temp)
        temp += self.f.read(n)
    
    def readN(self, n):
        temp = ''
        i = 0
        while i < n:
            temp += self.read7()
            i += 7
        if len(temp) > n:
            self.buffer = temp[n:]
        return temp[:n]
        
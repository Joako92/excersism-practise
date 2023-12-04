class Cipher:
    def __init__(self, key="aaaaaaaaaa"):      
        self.key = key.lower()
        self.cipher = [ord(letter)-97 for letter in self.key]       

    def encode(self, text):
        key2 = []
        code = ""
        
        while len(key2) < len(text):
            key2.extend(self.cipher)
        
        for t,n in zip(text,key2):
            if ord(t)+n > 122:
                code += chr((ord(t)-26)+n)
            else:
                code += chr(ord(t)+n)

        return(code)

    def decode(self, text):
        key2 = []
        code = ""
        
        while len(key2) < len(text):
            key2.extend(self.cipher)
            
        for t,n in zip(text,key2):
            if ord(t)-n < 97:
                code += chr((ord(t)+26)-n)
            else:
                code += chr(ord(t)-n)

        return(code)

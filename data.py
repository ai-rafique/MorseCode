class Morse:
    character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    code = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110']

    def __init__(self):
        self.morse=dict(zip(self.character, self.code))

    def print_key(self):
        """
        prints the keys and values as a prettytable
        """
        from prettytable import PrettyTable
        keytab = PrettyTable(['key', 'value'])
        for key, val in self.morse.items():
            keytab.add_row([key, val])
        print(keytab) 

    def encode(self,plaintext):
        """
        Checks the character index against the code list
        """
        i=self.character.index(plaintext)
        return self.code[i] 

    def decode(self,encoded):
        """
        Checks the code index against the character list
        """
        i=self.code.index(encoded)
        return self.character[i]

    def convert(self,string):
        """
        breaks a string to list. E.g
        apple becomes ['a','p','p','l','e']
        """ 
        list1=[] 
        list1[:0]=string 
        return list1    

    def encode_process(self,text):
        """
        The encoding process where text is outputted as a more list
        """
        listy = self.convert(text)
        morse_code =[]
        for i in range(len(listy)):
            if listy[i] in self.character:
                morse_code.append(self.encode(listy[i]))
            else:
                morse_code.append(' ')  
        return morse_code        

    def decode_process(self,encoded):
        """
        The decoding process to convert a morse list to text list
        Please use double spacing to add space.
        E.g
        0000 00  0000 00
        would become
        ['H','I',' ','H','I']
        The double space is important so that we have a space between code and 
        when we join back, we have a perfect sentence.
        """
        plain_text =[]
        for i in range(len(encoded)):
            if encoded[i] in self.code:
                plain_text.append(self.decode(encoded[i]))
            else:
                plain_text.append(' ')            
        return plain_text        

    def ops(self):
        """
        List of available operations
        """
        print('a) Get Keys')
        print('b) Encode')    
        print('c) Decode')
        
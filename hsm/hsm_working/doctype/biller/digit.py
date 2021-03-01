class Digit():
    def __init__(self):
        self.val=""
        self.word=""
        self.length={6:100000,
                     4:1000,
                     3:100,
                     2:10}
    def dictionary(self,num):
        duct = {1:'One',
                2:'Two',
                3:'Three',
                4:'Four',
                5:'Five',
                6:'Six',
                7:'Seven',
                8:'Eight',
                9:'Nine'}

        decade2={
                10:'Ten',
                11:'Eleven',
                12:'Twelve',
                13:'Thirteen',
                14:'Fourteen',
                15:'Fifteen',
                16:'Sixteen',
                17:'Seventeen',
                18:'Eighteen',
                19:'Nineteen',
                20:'Twenty',
                30:'Thirty',
                40:'Fourty',
                50:'Fifty',
                60:'Sixty',
                70:'Seventy',
                80:'Eighty',
                90:'Ninety'}
        if num <10:
            return duct[num]

        if num > 9:
            return decade2[num]

    def units(self,num):
        dictn = {6:'Lakh',
                 4:'Thousand',
                 3:'Hundred'}
        if num in dictn:
            return dictn[num]
    def functn(self,num,length):
        divider = self.length[length]
        full_num= num // divider
        reminder= num % divider
        if full_num > 20:
            reminder1 = full_num % 10
            full_num = full_num - reminder1
            full_num = self.dictionary(full_num)
            if reminder1 != 0:
                reminder2 = self.dictionary(reminder1)
                unit = self.units(length)
                full_num1 = full_num + " "+reminder2
                self.word=self.word+" "+full_num1+" "+unit
                self.guess(reminder)
            else:
                unit = self.units(length)
                self.word=self.word+" "+full_num+" "+unit
                self.guess(reminder)
        else:
            self.val=self.dictionary(full_num)
            unit = self.units(length)
            if reminder == 0:
                self.word=self.word+" "+self.val+" "+unit+" Rs Only."
                return self.word
            else:
                self.word=self.word+" "+self.val+" "+unit
                self.guess(reminder)


    def guess(self,num):
        str_num = str(num)
        print(str_num)
        if len(str_num)>=6:
            self.functn(num,6)
        if len(str_num)>=4 and len(str_num)<6:
            val = self.functn(num,4)
        if len(str_num)==3:
            val = self.functn(num,3)

        if len(str_num)<=2:
            if int(str_num)>20:
                reminder3 = int(str_num) % 10
                full_num = int(str_num) - reminder3
                unit_val = self.dictionary(full_num)
                if reminder3 !=0:
                    reminder2 = self.dictionary(reminder3)
                    self.word=self.word+" "+unit_val+" "+reminder2+" Rs Only."
                else:
                    self.word=self.word+" "+unit_val+" Rs Only."
                return self.word
                # exit()
            else:
                reminder2 = self.dictionary(int(str_num))
                self.word=self.word+" and "+reminder2+" Rs Only."
                return self.word
        return self.word

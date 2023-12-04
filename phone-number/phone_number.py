class PhoneNumber:
    def __init__(self, number):
        num = []
        for c in number:
            if c.isdigit():
                num.append(c)
        number = "".join(num)
        
        if len(number) < 10 or len(number) > 11:
            raise ValueError("number should be 10 or 11 width")

        elif len(number) == 11 and number[0] != "1":
            raise ValueError("International country code should be 1")

        elif len(number) == 11 and number[0] == "1":
            if len(number) == 11 and number[1] == "0" or number[1] == "1" :
                raise ValueError("Area code should be 1")

            elif len(number) == 11 and number[4] == "0" or number[4] == "1" :
                raise ValueError("Exchange code should be 1")
            
            number = number[1:]

        elif len(number) == 10 and number[0] == "0" or number[0] == "1" :
            raise ValueError("Area code should be 1")

        elif len(number) == 10 and number[3] == "0" or number[3] == "1" :
            raise ValueError("Exchange code should be 1")
        
        self.number = number
        self.area_code = number[0:3]
        self.exchange_code = number[3:6]
        self.subscriber_number = number[6:]

    def pretty(self):       
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
        


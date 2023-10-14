

class Time:
    def __init__(self, h, m, s):
        #properties
        self.hour = h
        self.minute = m
        self.second = s
        self.fix()

    #methods
    def show(self):
        print (self.hour, ":", self.minute, ":", self.second)

    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new, m_new, s_new)
        # result.fix()
        return result
    
    def sub(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new, m_new, s_new)
        # result.fix()
        return result
    
    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.second < 0:
            self.second += 60
            self.minute -= 1

        if self.minute < 0:
            self.minute += 60
            self.hour -= 1
        
        if self.hour >= 24:         # to prevent 24:..:..
            self.hour -=24

    def second_to_time(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1
            while self.minute >= 60:
                self.minute -= 60
                self.hour += 1
        
        result = Time(self.hour, self.minute, self.second)
        return result
    
    def time_to_second(self):
        self.second = self.hour * 3600 + self.minute * 60 + self.second

        result = self.second
        return result
    
    def gmt_to_tehran(self):
        tehran_h = self.hour + 3
        tehran_m = self.minute + 30
        tehran_s = self.second

        result = Time(tehran_h, tehran_m, tehran_s)
        return result


t1 = Time(3, 75, 17)
t1.show()

t2 = Time(4, 50, 2)
t2.show()

t3 = t1.sum(t2)
t3.show()

t4 = Time(0, 0, 3667)
t5 = t4.second_to_time()
t5.show()

t6=t2.time_to_second()
print(t6)

gmt = Time(22, 33, 25)
tehran_time = gmt.gmt_to_tehran()
tehran_time.show()
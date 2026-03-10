class Solution:
    def parking_fee(self, hours):
        fee = 0
        if hours <= 2:
            fee = 0
        elif hours <= 5:
            fee = (hours-2)*20
        else :
            fee = 60 + (hours-5)*50

        if hours > 12:
            fee += 200        
        
        return fee
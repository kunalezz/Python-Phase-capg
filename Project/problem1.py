class Solution:
    def strong_passwords(self, passwords):
        strong = []
        
        for password in passwords:
            
            if len(password) < 8:
                continue
            
            has_upper = any(c.isupper() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(c in "@#$" for c in password)
            
            if has_upper and has_digit and has_special:
                strong.append(password)
        
        return strong
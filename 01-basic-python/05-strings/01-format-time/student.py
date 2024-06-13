# Write your code here

def format_time(hours, minutes, seconds):
    def format(n):
        return str(n).rjust(2, '0')
    
    return f'{format(hours)}:{format(minutes)}:{format(seconds)}'
import time 

def count_time(t):
    """This function takes a time in seconds as input and displays a countdown on the screen"""
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print('Timer Finished!')
    
# Get the input for countdown time in seconds 
t = int(input('Enter the countdown time in seconds: '))

# Start the countdown
count_time(t)
        
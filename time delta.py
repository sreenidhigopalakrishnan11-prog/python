import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    # Format: Day dd Mon yyyy hh:mm:ss +xxxx
    fmt = '%a %d %b %Y %H:%M:%S %z'
    
    # Parse the strings into datetime objects
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    
    # Calculate absolute difference in seconds
    diff_seconds = abs(int((dt1 - dt2).total_seconds()))
    
    return str(diff_seconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')

    fptr.close()

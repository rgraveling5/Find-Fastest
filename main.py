#TASK 1
names = ['J Ferguson','M Buchan', 'G Hunter', 'L MacDonald', 'Random Guy 1', 'Random Guy 2']
times = [32.125, 33.625, 64.125, 34.50, 59.355, 59.5]

min = 0
minPosition = 0
minValue = times[minPosition]

for x in range(6):
  if times[x] < minValue:
    minPosition = x
    minValue = times[x]
    
print('The competitor who completed the course in the least time is', names[minPosition], 'with a time of',times[minPosition], 'minutes')

"""
TASK 2
Converting to floating point representation
       Sign Bit    Mantissa        Exponent
64.125 --> 0  100 0000 0010 0000  0000 0111
33.625 --> 0  100 0011 0100 0000  0000 0110
32.125 --> 0  100 0000 0100 0000  0000 0110
34.500 --> 0  100 0101 0000 0000  0000 0110
"""
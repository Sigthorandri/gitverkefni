import math

n = 1
max_int = 0
while n > 0:
    num_int = int(input("Input a number: ")) 
    if num_int > max_int: # Athuga hvort inntak sé stærra en það núverandi max_int
        max_int =+ num_int # Breyta max_int í inntakið 
    if num_int < 0: # Athuga hvort inntak sé minna en 0
        n = -2 # Hætta í while loopu
print("The maximum is", max_int)
"""
A program to prove the prime number theory that
every prime number above 3 lies beside a multiple of 6self.


Author : Mike Rassi
Date 09/11/18

"""


prime_candidate = 2
max_number = 10000

prime_list = [2]


while prime_candidate < max_number:
    prime_switch = 1
    for number in prime_list:
        if prime_candidate % number == 0:
            prime_switch = 0
    if prime_switch == 1:
        prime_list.append(prime_candidate)
    max_number / prime_candidate
    prime_candidate += 1


print(prime_list)

for prime in prime_list:
    if (prime + 1 ) % 6 == 0 or (prime - 1 ) % 6 == 0:
        print (prime,": lies beside a multiple of 6.")
    elif prime == 2 or prime == 3:
        print (prime)
    else:
        print(prime,": NO PROOF")

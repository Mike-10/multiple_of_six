"""
A program to prove the prime number theory that
every prime number above 3 lies beside a multiple of 6self.


Author : Mike Rassi
Date 09/11/18
Amended 10/11/18

"""


prime_candidate = 2
max_number = 10000

prime_list = [2]

def check_list():
    global prime_candidate
    while prime_candidate < max_number:
        prime_switch = 1
        for number in prime_list:
            if prime_candidate % number == 0:
                prime_switch = 0
        if prime_switch == 1:
            prime_list.append(prime_candidate)
        max_number / prime_candidate
        prime_candidate += 1


def prime_check():
    for prime in prime_list:
        side_list = []
        def beside_function(beside_1, beside_2):
            side_list.append(beside_1 - 1)
            side_list.append(beside_2 + 1)
        if (prime + 1 ) % 6 == 0 or (prime - 1 ) % 6 == 0:
            beside_function(prime, prime)
            for side in side_list:
                if side % 6 != 0:
                    side_list.pop(side_list.index(side))
            multiple = side_list[0] / 6
            print ("-",prime,"lies beside",side_list[0],"  {", side_list[0],"/ 6 =", multiple," - an integer}")
        elif prime == 2 or prime == 3:
            print (prime)
        else:
            return prime,": NO PROOF"



def eternal_check():
    check_list()
    prime_check()
    global max_number
    max_number = max_number*2

for n in range(10):
    eternal_check()

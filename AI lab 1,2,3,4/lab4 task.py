def luhn(card_number):
    card_number = [int(digit) for digit in str(card_number)]
    checksum = 0
    odd_digits = card_number[-1::-2]
    even_digits = card_number[-2::-2]

    checksum += sum(odd_digits)
    
    for digit in even_digits:
        checksum += sum(divmod(digit * 2, 10))
    
    return checksum % 10 == 0


print(luhn(4532015112830366))  

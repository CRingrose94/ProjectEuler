def digit_powers(exponent):      

    pow_digits = [i ** exponent for i in range(10)]
    total_sum = 0
    upper_bound = (exponent + 1) * pow_digits[9]

    for j in range(10, upper_bound + 1):

        partial_sum = temp_num = j

        while temp_num:
            partial_sum -= pow_digits[temp_num % 10]
            temp_num //= 10

        if not partial_sum:
            total_sum += j

    return total_sum


if __name__ == '__main__':
    print(digit_powers(5))

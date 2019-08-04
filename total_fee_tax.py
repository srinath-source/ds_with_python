def fun_fee_cal(tax,*args):
    total_fee = 0;
    for i in args:
        i = i+tax
        total_fee = total_fee + i
    return total_fee
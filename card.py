card = input(" enter your credit card number: ")
if card[:1] == '4':
    print("visa");
elif card[:4] == '4123' or card[:4] == '4423' or card[:3] == '421' or card[:6] == '456700':
    print("visa electro")
elif card[:4] == '5121' or card[:4] == '5252' or card[:4] == '5353':
    print("master");
elif card [:2] == '50' or card[:2] == '51' or card[:2] == '52':
    print("maestro");
else:
    print("others");
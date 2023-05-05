def converter(amount_to_convert: int) -> float:
    # int(input("convert dollar to naira "))
    naira = amount_to_convert * 700
    print(f"The value is {naira:,.2f} in naira")
    return naira


if __name__ == '__main__':
    converter(34)

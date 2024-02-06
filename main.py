while True:
    var1 = input('item: ')
    var2 = float(input('how many: '))
    var3 = float(input('item cost each: '))

    multiplication = var2 * var3
    print(f'the total cost of item 1 is: {multiplication}')
    while True:
        answer = str(input('Run again? (yes/no): '))
        if answer in ('yes', 'no'):
            break
        print("invalid input.")
    if answer == 'yes':
        continue
    else:
        print("Goodbye")
        break
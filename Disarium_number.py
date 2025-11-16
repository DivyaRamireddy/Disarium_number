# disarium_number_checker.py
# Placement Important Program: DISARIUM NUMBER ✨

def is_disarium(num):
    """
    A Disarium Number is a number where the sum of its digits
    powered with their respective positions equals the number.
    Example: 135 → 1¹ + 3² + 5³ = 135
    """
    digits = str(num)
    total = 0

    for index, d in enumerate(digits, start=1):
        total += int(d) ** index

    return total == num


if __name__ == "__main__":
    print("✨ Disarium Number Checker ✨")
    print("-----------------------------")

    n = int(input("Enter a number: "))

    if is_disarium(n):
        print(f"{n} is a Disarium Number ✔️")
    else:
        print(f"{n} is NOT a Disarium Number ❌")

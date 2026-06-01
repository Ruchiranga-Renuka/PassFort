import re

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password):
    return bool(re.search(r'[a-z]', password))

def check_digit(password):
    return bool(re.search(r'\d', password))

def check_special(password):
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def check_password_strength(password):
    checks = {
        "At least 8 characters":     check_length(password),
        "Contains uppercase letter":  check_uppercase(password),
        "Contains lowercase letter":  check_lowercase(password),
        "Contains a number":          check_digit(password),
        "Contains a special character": check_special(password),
    }

    print("\n--- Password Strength Report ---")
    passed = 0
    for rule, result in checks.items():
        status = "✅" if result else "❌"
        print(f"  {status}  {rule}")
        if result:
            passed += 1

    score = passed / len(checks)

    print("\n--- Strength Rating ---")
    if score == 1.0:
        print("  💪 Very Strong")
    elif score >= 0.8:
        print("  🟢 Strong")
    elif score >= 0.6:
        print("  🟡 Moderate")
    elif score >= 0.4:
        print("  🟠 Weak")
    else:
        print("  🔴 Very Weak")

    print(f"\n  Score: {passed}/{len(checks)} rules passed")
    print("--------------------------------\n")

def main():
    print("=== Password Checker ===")
    while True:
        password = input("Enter a password to check (or 'quit' to exit): ")
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        check_password_strength(password)

if __name__ == "__main__":
    main()
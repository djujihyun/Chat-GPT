def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def main():
    print("1. 섭씨를 화씨로 변환")
    print("2. 화씨를 섭씨로 변환")
    print("3. 킬로그램을 파운드로 변환")
    print("4. 파운드를 킬로그램으로 변환")
    print("5. 미터를 피트로 변환")
    print("6. 피트를 미터로 변환")
    choice = input("어떤 단위를 변환하시겠습니까? (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        value = float(input("변환하고자 하는 값을 입력하세요: "))
        if choice == '1':
            result = celsius_to_fahrenheit(value)
            print(f"{value} 섭씨는 {result} 화씨입니다.")
        elif choice == '2':
            result = fahrenheit_to_celsius(value)
            print(f"{value} 화씨는 {result} 섭씨입니다.")
        elif choice == '3':
            result = kilograms_to_pounds(value)
            print(f"{value} 킬로그램은 {result} 파운드입니다.")
        elif choice == '4':
            result = pounds_to_kilograms(value)
            print(f"{value} 파운드는 {result} 킬로그램입니다.")
        elif choice == '5':
            result = meters_to_feet(value)
            print(f"{value} 미터는 {result} 피트입니다.")
        elif choice == '6':
            result = feet_to_meters(value)
            print(f"{value} 피트는 {result} 미터입니다.")
    else:
        print("유효하지 않은 선택입니다.")

if __name__ == "__main__":
    main()

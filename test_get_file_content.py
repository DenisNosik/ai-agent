from functions.get_file_content import get_file_content

if __name__ == "__main__":
    print("Result for lorem ipsum:\n", len(get_file_content("calculator", "lorem.txt")))

    print("Result for calculator, main.py:\n" + get_file_content("calculator", "main.py"))
    print("Result for pkg/calculator.py:\n" + get_file_content("calculator", "pkg/calculator.py"))
    print("Result for calculator '/bin/cat:\n" + get_file_content("calculator", "/bin/cat"))
    print("Result for calculator pkg/does_not_exist.py :\n" + get_file_content("calculator", "pkg/does_not_exist.py"))
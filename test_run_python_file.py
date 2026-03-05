from functions.run_python_file import run_python_file

if __name__ == "__main__":
    print("Should print the calculator's usage instructions\n", run_python_file("calculator", "main.py"))
    print("----")
    print("Should run the calculator\n", run_python_file("calculator", "main.py", ["3 + 5"]))
    print("----")
    print("Should run the calculator's tests successfully\n", run_python_file("calculator", "tests.py"))
    print("----")
    print("This should return an error\n", run_python_file("calculator", "../main.py"))
    print("----")
    print("This should return an error\n", run_python_file("calculator", "nonexistent.py"))
    print("----")
    print("This should return an error\n", run_python_file("calculator", "lorem.txt"))
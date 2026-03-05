from functions.write_file import write_file

if __name__ == "__main__":
    print("Test for lorem", write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print("Test for morelorem.txt", write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print("Test for /tmp/temp.txt", write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
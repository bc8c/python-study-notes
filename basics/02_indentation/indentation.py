if __name__ == "__main__":
    n = 10
    for i in range(n):
        print("This line is indented with 4 spaces.")
        if i % 2 == 0:
            print("This line is further indented inside an if block.")
        else:
            print("This line is also further indented inside the else block.")
    print("Back to the main indentation level.")

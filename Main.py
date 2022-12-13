from File_automate import app


if __name__ == "__main__":

    basepath = input("Enter your base directory path")
    file_name = app.Arrange_file(basepath=basepath)
    print(file_name)

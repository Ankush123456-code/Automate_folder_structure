from File_automate import app


if __name__ == "__main__":
    
    basepath = "C:/Users/Ankush babu/Desktop/webinar/"
    
    file_name = app.Arrange_file(basepath=basepath)
    if len(file_name) > 0:
        print(file_name)
    else:
        print("Failed")

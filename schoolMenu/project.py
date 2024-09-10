from datetime import datetime


def login(name, password):
    """
    this is the login section for the teacher
    :return:None
    """
    if name.lower() == "anna" and password == 12345:
        print(f"Module Record System- Login")
        print("-"*30)
        print(f"Name: {name}\nPassword: {password}\n")
        print(f"Welcome {name}!")
        print(f"Module Record System- Options")
        print("-"*30)
        choice = int(input("1. Record Attendance\n2. Generate Statistics\n3. Exit"))
        if choice == 1:
            print(">1\n\nRecording Attendance.")
            record_attendance()
        elif choice == 2:
            print(">2\n\nGenerating Statistics.")
            generate_stats()
        elif choice == 3:
            print(">3\n\nExiting Module Record System.")
            exit()
    else:
        print(f"Module Record System- Login")
        print("-" * 30)
        print(f"Name: {name}\nPassword: {password}\n")
        print("Login Failed.\nExiting Module Record System.")
        exit()


def record_attendance():
    """
    This function is where the teacher chooses which module and records attendance
    :return: students, student_record
    """
    students = []
    student_record = []
    today = []
    counter = 0
    print(f"Module Record System- Attendance - Choose a Module")
    print("-" * 30)
    module = int(input(f"1.SOFT_6017\n2.SOFT_6018"))
    if module == 1:
        print(f">{module}")
        print(f"Module Record System- Attendance - SOFT_6017")
        print("-" * 30)
        read_17 = open("SOFT_6017.txt", "r+")
        length17 = len(read_17.readlines())
        print(f"There are {length17} students enrolled")
        # Go back to top of file
        read_17.seek(0)
        for line in read_17:
            line = line.rstrip()
            line_data = line.split(",")
            students.append(line_data[0])
            student_record.append(line_data[1])
            for students in students:
                print(f"Student #{counter+1}: {students[counter]}")
                here = int(input("1.Present\n2.Absent"))
                if here == 1:
                    print(f">{here}")
                    today.append(", Present")
                    read_17.write(today[counter])
                elif here == 2:
                    print(f">{here}")
                    today.append(", Absent")
                    read_17.write(today[counter])
                counter += 1
        print("SOFT_6017.txt was updated with the latest attendance records.\nPress Enter to continue")
        read_17.close()

    elif module == 2:
        print(f">{module}")
        print(f"Module Record System- Attendance - SOFT_6018")
        print("-" * 30)
        read_18 = open("SOFT_6018.txt", "r")
        length18 = len(read_18.readlines())
        print(f"There are {length18} students enrolled")
        read_18.seek(0)
        for line in read_18:
            line = line.rstrip()
            line_data = line.split(",")
            students.append(line_data[0])
            student_record.append(line_data[1])
            for i in range(len(students)):
                print(f"Student #{counter+1}: {students[counter]}")
                here = int(input("1.Present\n2.Absent"))
                if here == 1:
                    print(f">{here}")
                    today.append(", Present")
                    read_18.write(today[counter])
                elif here == 2:
                    print(f">{here}")
                    today.append(", Absent")
                    read_18.write(today[counter])
                counter += 1
        print("SOFT_6018.txt was updated with the latest attendance records.\nPress Enter to continue")
        read_18.close()


def generate_stats():
    record_list1 = []
    record_list2 = []
    date = datetime.now().strftime('%Y_%m_%d')
    f = open(f"attendance_stats_{date}.txt", "x")
    print(f"Module Record System- Average Attendance Data")
    print("-" * 30)
    file1 = open("SOFT_6017.txt", "r")
    for line in file1:
        line = line.rstrip()
        line_data = line.split(",")
        record_list1.append(line_data[1])
    average_record1 = sum(record_list1)/len(record_list1)
    stars1 = "*" * round(average_record1/10)
    file1.close()
    print(f"Modular Programming\t\tSOFT_6017\t{average_record1}\t{stars1}")
    f.write(f"Modular Programming\t\tSOFT_6017\t{average_record1}\t{stars1}")
    file2 = open("SOFT_6018.txt", "r")
    for line in file2:
        line = line.rstrip()
        line_data = line.split(",")
        record_list2.append(line_data[1])
    average_record2 = sum(record_list2)/len(record_list2)
    stars2 = "*" * round(average_record2/10)
    file2.close()
    print(f"Programming Fundamentals\tSOFT_6018\t{average_record2}\t{stars2}")
    f.write(f"Programming Fundamentals\tSOFT_6018\t{average_record2}\t{stars2}")
    if average_record1 > average_record2:
        print(f"The best attended module is Modular Programming with a {average_record1}% attendance rate.")
        f.write(f"The best attended module is Modular Programming with a {average_record1}% attendance rate.")
        if average_record2 < 40:
            print(f"There is 1 module(s) with attendance under 40%:\n\tProgramming Fundamentals")
            f.write(f"There is 1 module(s) with attendance under 40%:\n\tProgramming Fundamentals")
    elif average_record1 < average_record2:
        print(f"The best attended module is Programming Fundamentals with a {average_record2}% attendance rate.")
        f.write(f"The best attended module is Programming Fundamentals with a {average_record2}% attendance rate.")
        if average_record1 < 40:
            print(f"There is 1 module(s) with attendance under 40%:\n\tModular Programming")
            f.write(f"There is 1 module(s) with attendance under 40%:\n\tModular Programming")
    print(f"The above data is also stored at Attendance_Stats_2023_02_01.txt.\nPress Enter to continue")
    f.close()


if __name__ == "__main__":
    name = input("What is your name?: ")
    password = int(input("What is your password?: "))
    login(name, password)

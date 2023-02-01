import students

main_dct = {}
student_list = []
subject_list = []

def start():
    while True:
        op = students.operation()
        if op == 1:
            student_name = students.add_student()
            if student_name not in student_list:
                student_list.append(student_name)
                main_dct[student_name] = {}
                for lesson in subject_list:
                    main_dct[student_name][lesson] = []


        if op == 2:
            subject_name = students.add_subject()
            if subject_name not in subject_list:
                subject_list.append(subject_name)
                for name in student_list:
                    main_dct[name][subject_name] = []


        if op == 3:
            name, subject, grades = students.add_grades()

            if 0 < grades < 6:
                main_dct[name][subject].append(grades)
            else:
                print('Ошибка! Нет такой оценки')

        if op == 4:
            print(main_dct)
        if op == 5:
            name = students.show_grades()
            print(main_dct[name])
        if op == 6:
            break

if __name__ == '__main__':
    report = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        report.append([name,score])


    report.sort(key = lambda row : row[1] )
    Lower = report[0][1]
    for secLower in report:
        if secLower[1] != Lower:
            Lower = secLower[1]
            break

    for name_grade in report:
        if name_grade[1] != Lower:
            report.remove(name_grade)

    report.sort(key = lambda name : name[0])

    for name_grade in report:
        if name_grade[1] == Lower:
            print (name_grade[0])

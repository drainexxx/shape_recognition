mas_s = []

def read_file(file_name):
    cer = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i in lines:
            for a in i:
                cer.append(a)

            cer.insert(0, '0')
            cer.append('0')
            cer.pop(11)
            mas_s.append(cer)
            cer =[]
        mas_s.append(['0','0', '0','0', '0','0', '0','0', '0','0', '0','0'])
        mas_s.insert(0, ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    return [line.strip() for line in lines]

def fun_fun(neme):
    read_file(neme)
#    print(mas_s)
    # def toch_1():
    con_mas = []
    con_con_mas = []
    schet = 0
    for i in mas_s:
        for a in i:
            con_mas.append(a)
    for i in range(len(con_mas)):  # i - индекс
        if con_mas[i] == '1':
            con_con_mas.append(i)
#    print(con_mas)
#    print(con_con_mas)
    for i in range(len(con_mas)):
        if con_mas[i] == '1':
            try:
                if ((con_mas[i - 1] == con_mas[i + 1]) and ((con_mas[i - 1] != '0') and con_mas[i + 1] != '0')) \
                        or (
                        (con_mas[i - 13] == con_mas[i + 13]) and ((con_mas[i - 13] != '0') and con_mas[i + 13] != '0')) \
                        or (
                        (con_mas[i - 12] == con_mas[i + 12]) and ((con_mas[i - 12] != '0') and con_mas[i + 12] != '0')) \
                        or (
                        (con_mas[i - 11] == con_mas[i + 11]) and ((con_mas[i - 11] != '0') and con_mas[i + 11] != '0')):
                    print(".", end=".")
                else:
                    schet += 1
#                    print(i)
            except:
                print('lol')

    print(schet)
    if schet == 3:
        print("треугольник")
    if schet == 4:
        print("четырехугольник")
    if schet > 4:
        print("окружность")

#fun_fun("box.txt")
fun_fun("circle.txt")
#fun_fun("rect.txt")
#fun_fun("trian_equi.txt")
#fun_fun("trian_iso.txt")
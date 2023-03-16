import re

def signalDecode(str):
    return re.findall('-?\d+\.?\d*', str)

if __name__ == '__main__':
    str1 = "i = 1227, sin(i) = 48.\n9216 A = 050 \ni = 1228, sin(i) = 17.7413 A = 050 \ni = 1229, sin(i) = -29.7503 A = 050 \ni = 1230,\n sin(i) = -49.8896 A = 050 \ni = 1231, sin(i) = -24.1606 A = 050 \ni = 1232, sin(i) = 23.7815 A = \n"
    str2 = "123\n 456\n -789 789\n asdasdasd 1asd54asfdasd1.2\n334"
    split = signalDecode(str1)
    for i in split:
        # if(i.isnumeric()):
        print(i)
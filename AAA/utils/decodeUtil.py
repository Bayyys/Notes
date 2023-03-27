import sys
sys.path.append('..')
import re
import serial
import time
from scipy.signal import butter
import utils.globalParams as glo

def signalDecode(str):
    # return [ float(i) for i in re.findall('-?\d+\.?\d*', str)]
    return re.findall('-?\d+\.?\d*', str)

def bytestoFloat(data):
    '''将字节转换为浮点数
    
    args: data: 读取到的数据
    
    return: data: 转换后的数据'''
    start_index = 0
    try:
        if data[3] > 128:
            tmp1 = (~data[start_index]) & 0xff
            tmp2 = ((~data[start_index + 1]) & 0xff) << 8
            tmp3 = ((~data[start_index + 2]) & 0xff) << 16
            data = -(tmp1 + tmp2 + tmp3 + 1)
            data = data / 24
        else:
            data = int((data[start_index]) + (data[start_index + 1] << 8) + (data[start_index + 2] << 16)
                        + (data[start_index + 3] << 24))
            data = data / 24
        return data
    except:
        return 0

def LowPassFilter(cutoffFreq, fs, N=8, ripple=1):  # 低通滤波
    # 低通滤波
    print("LowPassFilter Changed!")
    # return cheby1(N=N, rp=ripple,
    #                 Wn=cutoffFreq,
    #                 btype='lowpass', fs=fs,
    #                 analog=False, output='sos')
    return butter(N=N, Wn=cutoffFreq, btype='lowpass', output='sos', fs=fs)

def HighPassFilter(cutoffFreq, fs, N=8, ripple=1): # 高通滤波
    # 高通滤波
    print("HighPassFilter Changed!")
    # return cheby1(N=N, rp=ripple,
    #                 Wn=cutoffFreq,
    #                 btype='highpass', fs=fs,
    #                 analog=False, output='sos')
    return butter(N=N, Wn=cutoffFreq, btype='highpass', output='sos', fs=fs)

def NotchFilter(cutoffFreq, filterParam, fs, N=8, ripple=1):    # 陷波滤波
    # 陷波滤波
    print("NotchFilter Changed!")
    # return cheby1(N=N, rp=ripple,
    #                 Wn=[cutoffFreq - filterParam, cutoffFreq + filterParam],
    #                 btype='bandstop', fs=fs,
    #                 analog=False, output='sos')
    return butter(N=N, Wn=[cutoffFreq-filterParam, cutoffFreq+filterParam],
                  btype='bandstop', output='sos', fs=fs)

def BandPassFilter(passbandFreq, stopbandFreq, fs, N=8, ripple=1):  # 带通滤波
    # 带通滤波
    print("BandPassFilter Changed!")
    # return cheby1(N=N, rp=ripple,
    #                 Wn=[passbandFreq, stopbandFreq],
    #                 btype='bandpass', fs=fs,
    #                 analog=False, output='sos')
    return butter(N=N, Wn=[passbandFreq, stopbandFreq],
                  btype='bandpass', output='sos', fs=fs)


if __name__ == '__main__':

    i = 7

    if i == 1:
        sig1 = "i = 1227, sin(i) = 48.\n9216 A = 050 \ni = 1228, sin(i) = 17.7413 A = 050 \ni = 1229, sin(i) = -29.7503 A = 050 \ni = 1230,\n sin(i) = -49.8896 A = 050 \ni = 1231, sin(i) = -24.1606 A = 050 \ni = 1232, sin(i) = 23.7815 A = \n"
        str2 = "123\n 456\n -789 789\n asdasdasd 1asd54asfdasd1.2\n334"
        split = signalDecode(sig1)
        for i in split:
            # if(i.isnumeric()):
            print(i)
            print(type(i))
    
    elif i == 2:
        str = "a59b4400"
        str = "00449ba5"
        # print(decodeByteToFloat(str))
    
    elif i == 3:
        strHex = 0x352a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440037fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f1fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440023feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bafdffff6e124400ffffffffffffffff
        strT = 0x1234567878563412
        strBin = bin(strHex)
        # print(strBin)
        # print(struct.pack('B', strHex))
        test = strHex.to_bytes(length=144, byteorder='little', signed=True)
        print(test)
        print(len(test))
        print(test[0])
        print(test[1])
        print(test[143])
        print(0x352a.to_bytes(length=2, byteorder='little', signed=False))
        if test[0] & 0x80 == 0x80:
            print("yes")
        print(test[0] + test[1] + test[2] + test[3])
    
    elif    i == 4:
        str2 = 0x2d34362e353737373736202d34362e333933363530202d34362e323034383836202d34362e303131353030202d34352e383133353134202d34352e363130393436202d34352e343033383138202d34352e313932313439202d34342e393735393631202d34342e373535323735202d34342e353330313134202d34342e333030343939202d34342e303636343535202d34332e383238303034202d34332e353835313731202d34332e333337393739202d34332e303836343533202d34322e383330363138202d34322e353730353031202d34322e333036313236202d34322e303337353231202d34312e373634373133202d34312e343837373237202d34312e323036353933202d34302e393231333339202d34302e363331393932202d34302e333338353832202d34302e303431313339202d33392e373339363931202d33392e343334323639202d33392e313234393034202d33382e383131363237202d33382e343934343638202d33382e313733343630202d33372e383438363335202d33372e353230303234202d33372e313837363632202d33362e383531353831202d33362e353131383135202d33362e313638333938202d33352e383231333634202d33352e343730373438202d33352e313136353835202d33342e373538393130202d33342e333937373539202d33342e303333313639202d33332e363635313735202d33332e32393338313520

        str3 = 0x352a0200a55a0000a59b4400a59b4400a59b4400a59b4400a59b4400a59b440037fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400f1fdffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b440023feffffa59b4400a59b4400a59b4400a59b4400a59b4400a59b4400a59b4400bafdffff6e124400ffffffffffffffff

        # test = str3.to_bytes(length=144, byteorder='big', signed=True)
        # print(test.find(b'\xa5Z'))
        str4 = 0xa59b4400
        str5 = 0xa59b4400
        test = b't\x9dD\x00'
        print(test.hex())
        start_index = 0
        if test[3] > 128:
            tmp1 = (~test[start_index]) & 0xff
            tmp2 = ((~test[start_index + 1]) & 0xff) << 8
            tmp3 = ((~test[start_index + 2]) & 0xff) << 16
            data = -(tmp1 + tmp2 + tmp3 + 1)
            data = data / 24
        else:
            data = int(
                (test[start_index]) + (test[start_index + 1] << 8) + (test[start_index + 2] << 16) + (
                            test[start_index + 3] << 24))
            data = data / 24
        print(data)
        # str6 = str4.to_bytes(length=4, byteorder='little', signed=False)
        # str6 = str6 + str5.to_bytes(length=4, byteorder='little', signed=False)
        # print("str6: ", str6)


    elif i == 5:
        sig1 = b'\xb0H\x16\x00\xa5Z\x00\x00t\x9dD\x00F\x9eD\x00p\x9dD\x00i\x9dD\x00\x9f\x9dD\x00\x92\x9dD\x00\x84\x9eD\x00\xfc\x9dD\x00\xa2\x9dD\x00\xbe\x9dD\x00k\x9eD\x00E\x9eD\x00\x1d\x9eD\x00"\x9dD\x00\xf3\x9dD\x00u\x9dD\x00\x16\x9eD\x001\x9eD\x00\x8a\x9dD\x00\xb9\x9dD\x00\xc5\x9dD\x00\x8d\x9eD\x00\x84\x9dD\x00\x87\x9dD\x00\xbb\x9dD\x00Q\x9eD\x00?\x9dD\x00X\x9eD\x00\xd9\x9dD\x00\xab\x9dD\x00\xa5\x9dD\x00\xff\x9dD\x00\xff\xff\xff\xff\xff\xff\xff\xff\xdc\xb1H\x16\x00\xa5Z\x00\x00t\x9dD\x00F\x9eD\x00p\x9dD\x00i\x9dD\x00\x9f\x9dD\x00\x92\x9dD\x00\x84\x9eD\x00\xfc\x9dD\x00\xa2\x9dD\x00\xbe\x9dD\x00k\x9eD\x00E\x9eD\x00\x1d\x9eD\x00"\x9dD\x00\xf3\x9dD\x00u\x9dD\x00\x16\x9eD\x001\x9eD\x00\x8a\x9dD\x00\xb9\x9dD\x00\xc5\x9dD\x00\x8d\x9eD\x00\x84\x9dD\x00\x87\x9dD\x00\xbb\x9dD\x00Q\x9eD\x00?\x9dD\x00X\x9eD\x00\xd9\x9dD\x00\xab\x9dD\x00\xa5\x9dD\x00\xff\x9dD\x00\xff\xff\xff\xff\xff\xff\xff\xff\xdd\xb2H\x16\x00\xa5Z\x00\x00t\x9dD\x00F\x9eD\x00p\x9dD\x00i\x9dD\x00\x9f\x9dD\x00\x92\x9dD\x00\x84\x9eD\x00\xfc\x9dD\x00\xa2\x9dD\x00\xbe\x9dD\x00k\x9eD\x00E\x9eD\x00\x1d\x9eD\x00"\x9dD\x00\xf3\x9dD\x00u\x9dD\x00\x16\x9eD\x001\x9eD\x00\x8a\x9dD\x00\xb9\x9dD\x00\xc5\x9dD\x00\x8d\x9eD\x00\x84\x9dD\x00\x87\x9dD\x00\xbb\x9dD\x00Q\x9eD\x00?\x9dD\x00X\x9eD\x00\xd9\x9dD\x00\xab\x9dD\x00\xa5\x9dD\x00\xff\x9dD\x00\xff\xff\xff\xff\xff\xff\xff\xff\xde\xb3H\x16\x00\xa5Z\x00\x00t\x9dD\x00F\x9eD\x00p\x9dD\x00i\x9dD\x00\x9f\x9dD\x00\x92\x9dD\x00\x84\x9eD\x00\xfc\x9dD\x00\xa2\x9dD\x00\xbe\x9dD\x00k\x9eD\x00E\x9eD\x00\x1d\x9eD\x00"\x9dD\x00\xf3\x9dD\x00u\x9dD\x00\x16\x9eD\x001\x9eD\x00\x8a\x9dD\x00\xb9\x9dD\x00\xc5\x9dD\x00\x8d\x9eD\x00\x84\x9dD\x00\x87\x9dD\x00\xbb\x9dD\x00Q\x9eD\x00?\x9dD\x00X\x9eD\x00\xd9\x9dD\x00\xab\x9dD\x00\xa5\x9dD\x00\xff\x9dD\x00\xff\xff\xff\xff\xff\xff\xff\xff\xdf\xb4H\x16\x00\xa5Z\x00\x00t\x9dD\x00F\x9eD\x00p\x9dD\x00i\x9dD\x00\x9f\x9dD\x00\x92\x9dD\x00\x84\x9eD\x00\xfc\x9dD\x00\xa2\x9dD\x00\xbe\x9dD\x00k\x9eD\x00E\x9eD\x00\x1d\x9eD\x00"\x9dD\x00\xf3\x9dD\x00u\x9dD\x00\x16\x9eD\x001\x9eD\x00\x8a\x9dD\x00\xb9\x9dD\x00\xc5\x9dD\x00\x8d\x9eD\x00\x84\x9dD\x00\x87\x9dD\x00\xbb\x9dD\x00Q\x9eD\x00?\x9dD\x00X\x9eD\x00\xd9\x9dD\x00\xab\x9dD\x00\xa5\x9dD\x00\xff\x9dD\x00\xff\xff\xff\xff\xff\xff\xff\xff\xe0\xb5H\x16\x00\xa5Z\x00\x00t\x9dD\x00'

        rest = b''
        if len(rest) > 0:
            sig1 = rest + sig1
        while len(sig1) > 144:
            if sig1.find(b'\xa5Z') != -1:
                index_s = sig1.find(b'\xa5Z') - 4
                index_e = index_s + 144
                print(index_s)
                print(sig1[index_s: index_e])
                rest = sig1[index_e:]
                sig1 = sig1[index_e:]
            else:
                break
        print(rest)
        # print(sig1)
        # print(sig1.find(b'\xa5Z'))
    
    elif i == 6:
        str1 = b'\xc6\x84\x13\x00'
        str2 = b'\xc8\x84\x13\x00'
    
    elif i == 7:
        ser = serial.Serial(port='COM3', baudrate=4608000)
        i = 0
        time1 = time.time()
        while(i<500):
            if ser.inWaiting():
                data = ser.read(ser.in_waiting)
                print(data)
                i += 1
                print("count:\t", i)
        
        print(time.time() - time1)
        ser.close()
    
    elif i == 8:
        with open('111.txt', 'r') as f:
            data = f.read()
        test = re.split(' ', data)
        print(len(test))
        print(test[514878])
        print(len(data))






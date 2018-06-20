# Arduinoシリアルコンソールからcsvにデータを落とし込む

import serial
import serial.tools.list_ports
import csv

# 出力CSVファイル名
savefile = 'data1500.csv'

# MacでArduinoシリアルコンソールをCSVに落とし込むとき
def get_serial_for_mac() :
    ser = serial.Serial()
    ser.baudrate = 9600
    for file in os.listdir('/dev'):
        if "tty.usbmodem" in file:

            # ser.portにCOM?の情報が入る
            ser.port = '/dev/'+file

sf = open(savefile, 'w')
csvWriter = csv.writer(sf)

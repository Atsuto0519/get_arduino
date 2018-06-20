# Arduinoシリアルコンソールからcsvにデータを落とし込む

# 必要なライブラリインポート
import serial
import serial.tools.list_ports
import os
import csv
import datetime

# MacでArduinoシリアルコンソールのコムポート自動決定
def get_port_for_mac() :
    ser = serial.Serial()
    ser.baudrate = 9600
    for file in os.listdir('/dev'):
        if "tty.usbmodem" in file:

            # ser.portにCOM?の情報が入る
            ser.port = '/dev/'+file

            return ser

# Windowsなら
def get_port_for_win() :
    ser = serial.Serial()
    ser.baudrate = 9600
    for i in range(100):
        try:
            ser.port = i
            ser.open()

            return ser

        except:
            i = i


# 出力CSVファイル名
savefile = str(datetime.date.today())+'_1.csv'
sf = open(savefile, 'w')
csvWriter = csv.writer(sf)

# 個別指定
# Macなら、ターミナル→'ls /dev'
# →出てきたそれっぽいやつ（/dev/tty.usbmodem）をser.portへ
ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/tty.usbmodem1411'

# 自動ポート指定
# ser = get_port_for_mac()

# 接続
ser.open()

# CSVのヘッダー設定
csvWriter.writerow(['time','temperature'])

# シリアルストリート処理部分
while 1 :
    line = ser.readline()
    data = str(line)

    if "'" in data :
        data = data.split("'")[1]

    if "\\" in data :
        data = data.split("\\")[0]

    if ":" in data :
        data = data.split(":")[-1]

    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+","+data)
    csvWriter.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),data])

ser.close()

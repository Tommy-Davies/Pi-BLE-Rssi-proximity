from bt_proximity import BluetoothRSSI
import time
import sys
import math

BT_ADDR1 = 'B8:27:EB:83:62:CB'  # 200
BT_ADDR2 = 'B8:27:EB:D8:43:C5'  # 134
BT_ADDR3 = 'B8:27:EB:B5:D9:44'  # 100
NUM_LOOP = 30

def print_usage():
    print("Usage: python test_address.py <bluetooth-address> [number-of-request$")

def main():

    num = NUM_LOOP
    btrssi1 = BluetoothRSSI(BT_ADDR1)
    btrssi2 = BluetoothRSSI(BT_ADDR2)
    btrssi3 = BluetoothRSSI(BT_ADDR3)

    n=4    #Path loss exponent(n) = 1.5
    c = 10   #Environment constant(C) = 10
    A0 = 2   #Average RSSI value at d0
    actual_dist = 100   #Static distance between transmitter and Receiver in cm
    sum_error = 0
    count = 0

    for i in range(1, num):
        rssi_bt1 = float('.'.join(str(ele) for ele in btrssi1.request_rssi()))
        rssi_bt2 = float('.'.join(str(ele) for ele in btrssi2.request_rssi()))
        rssi_bt3 = float('.'.join(str(ele) for ele in btrssi3.request_rssi()))
        if(rssi_bt1!=0 and i>1):                   
            count=count+1
            x = float((rssi_bt1-A0)/(-10*n))         
            distance = (math.pow(10,x) * 100) + c
            print( "Approximate Distance 1:" + str(distance))
            print( "RSSI: " + str(rssi_bt1))
            print( "Count: " + str(count))
            print( " ")
        if(rssi_bt2!=0 and i>1):                
            count=count+1
            x = float((rssi_bt2-A0)/(-10*n))      
            distance = (math.pow(10,x) * 100) + c
            print( "Approximate Distance 2:" + str(distance))
            print( "RSSI: " + str(rssi_bt2))
            print( "Count: " + str(count))
            print( " ")
        if(rssi_bt3!=0 and i>1):                    #reduces initial false valu$
            count=count+1
            x = float((rssi_bt3-A0)/(-10*n))         #Log Normal Shadowing Model$
            distance = (math.pow(10,x) * 100) + c
            print( "Approximate Distance 3:" + str(distance))
            print( "RSSI: " + str(rssi_bt3))
            print( "Count: " + str(count))
            print( " ")
        time.sleep(1)


if __name__ == '__main__':
    main()

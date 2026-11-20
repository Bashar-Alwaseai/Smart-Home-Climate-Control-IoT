from gpio import *
from time import *

def main():
    pinMode(A0, OUT) #LCD
    pinMode(0, OUT) #Air cooling
    pinMode(1, OUT) #LED1
    pinMode(2, OUT) #Heating Element
    pinMode(3, OUT) #LED2
    pinMode(A1, IN) #Temperature Sensor
    print("Blinking")

    while True:
        temp = analogRead(A1);
        Temp = (((temp * 200) / 1023) - 100);
        print("The teperature is : ", temp)
        print("The teperature is : ", Temp)
        if Temp >= 20:
            digitalWrite(0, HIGH); #Air cooling
            digitalWrite(1, HIGH); #LED1
            digitalWrite(2, LOW);
            digitalWrite(3, LOW);  #Heating Element
            customWrite(A0, 'The cooling sys ON ');
        elif Temp <= 19:
            digitalWrite(2, HIGH); #Heating Element
            digitalWrite(3, HIGH); #LED2
            digitalWrite(0, LOW);
            digitalWrite(1, LOW);
            customWrite(A0 , 'The Heating sys ON ');
        else :
            digitalWrite(0, LOW); #Air cooling
            digitalWrite(1, LOW); #LED1
            digitalWrite(3, LOW); #LED2
            digitalWrite(2, LOW); #Heating Element
            customWrite(A0 , 'The temp is Normal');
            delay(200)
        delay(500)

if __name__ == "__main__":
    main()
    
    
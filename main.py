an  Alle
class roboter():

def __init__(self):
    neZha.set_motor_speed(MotorList.M1, 0)
    def fahre(self):
    neZha.set_motor_speed(MotorList.M1, 100)
    neZha.set_motor_speed(MotorList.M2, 100)
    def klaue_oeffnen(self):
    neZha.set_servo_angel(neZha.ServoTypeList._180, neZha.ServoList.S1, 180)
    def klaue_schließen(self):
    neZha.set_servo_angel(neZha.ServoTypeList._180, neZha.ServoList.S1, 50)
    def sensor_wert(self):
    pass

terminator = roboter()

terminator


Dominic Moser 17:31
    print("Starten")
    class roboter:
        def __init__():
        neZha.setMotorSpeed(neZha.MotorList.M1, 0)


    def fahre():
    neZha.setMotorSpeed(neZha.MotorList.M1, 100)
    neZha.setMotorSpeed(neZha.MotorList.M2, 100)

    def stopp():
        neZha.setMotorSpeed(neZha.MotorList.M1, 0)
        neZha.setMotorSpeed(neZha.MotorList.M2, 0)

public klaue_oeffnen():
    neZha.setServoAngel(neZha.ServoTypeList._180, neZha.ServoList.S1, 180)

public klaue_schliesen():
    neZha.setServoAngel(neZha.ServoTypeList._180, neZha.ServoList.S1, 50)

public sensor_wert():
pass


print("Roboter objekt erstellen")
    terminator = roboter()
print("Roboter klaue oeffnen)
    terminator.klaue_oeffnen()
print("Roboter klaue schließen)
    terminator.klaue_schliesen()
print("Roboter fahre")
    terminator.fahre()
while True:
    print("loop")

terminator stopp
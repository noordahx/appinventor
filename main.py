def OpenWindow():
    powerbrick.servo(powerbrick.Servos.S1, 105)
    powerbrick.servo(powerbrick.Servos.S2, 5)
def CloseWindow():
    global s1, s2
    s1 = 5
    s2 = 110
    powerbrick.servo(powerbrick.Servos.S1, s1)
    powerbrick.servo(powerbrick.Servos.S2, s2)

def on_button_pressed_a():
    OpenWindow()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_koi_mqtt_onread(data, topic):
    if topic == "NBPR3JH6":
        basic.show_string(data[len(data)-1:])
        receive = str(data[len(data)-1:])
        if receive == "C":
            CloseWindow()
        elif receive == "O":
            OpenWindow()
        
koi.koi_mqtt_onread(on_koi_mqtt_onread)

def on_button_pressed_b():
    CloseWindow()
input.on_button_pressed(Button.B, on_button_pressed_b)

s2 = 0
s1 = 0
koi.koi_init_pw(koi.SerialPorts.PORT2)
koi.koi_join_ap("123", "987654321")
basic.pause(5000)
MakerCloud_KOI.connect_maker_cloud_mqtt()
basic.pause(2000)
MakerCloud_KOI.subscribe_topic("NBPR3JH6")
koi.koi_mqtt_sub("NBPR3JH6")
CloseWindow()
basic.show_leds("""
    . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
""")
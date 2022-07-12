function OpenWindow () {
    powerbrick.Servo(powerbrick.Servos.S1, 105)
    powerbrick.Servo(powerbrick.Servos.S2, 5)
}
function CloseWindow () {
    s1 = 5
    s2 = 110
    powerbrick.Servo(powerbrick.Servos.S1, s1)
    powerbrick.Servo(powerbrick.Servos.S2, s2)
}
input.onButtonPressed(Button.A, function () {
    OpenWindow()
})
koi.koi_mqtt_onread(function (data, topic) {
    let receive: string;
if (topic == "NBPR3JH6") {
        basic.showString("" + (data.slice(data.length - 1)))
        receive = "" + data.slice(data.length - 1)
        if (receive == "C") {
            CloseWindow()
        } else if (receive == "O") {
            OpenWindow()
        }
    }
})
input.onButtonPressed(Button.B, function () {
    CloseWindow()
})
let s2 = 0
let s1 = 0
koi.koi_init_pw(koi.SerialPorts.PORT2)
koi.koi_join_ap("123", "987654321")
basic.pause(5000)
MakerCloud_KOI.connectMakerCloudMQTT()
basic.pause(2000)
MakerCloud_KOI.subscribeTopic("NBPR3JH6")
koi.koi_mqtt_sub("NBPR3JH6")
CloseWindow()
basic.showLeds(`
    . . . . .
    . . . . .
    . # # # .
    . . . . .
    . . . . .
    `)

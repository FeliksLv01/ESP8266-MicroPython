# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

import uos, machine

#uos.dupterm(None, 1) # disable REPL on UART(0)

import gc

#import webrepl

#webrepl.start()

gc.collect()


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('PandoraBox-2.4G', '104104104')  #wifi的SSID和密码
    while not sta_if.isconnected():
        pass
    print('network config:', sta_if.ifconfig())
    return sta_if

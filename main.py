def on_received_number(receivedNumber):
    if receivedNumber > dice:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global dice
    dice = randint(1, 6)
    basic.show_number(dice)
    radio.send_number(dice)
input.on_button_pressed(Button.A, on_button_pressed_a)

dice = 0
radio.set_group(1)
from BreakfastSerial import Arduino, Led
from time import sleep

morsePin = 13
dotDelay = 0.2

letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",    # A-I
           ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",  # J-R
           "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",         # S-Z
          ]
numbers = ["-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."] # digits

if __name__ == "__main__":
    board = Arduino()
    led = Led(board, morsePin)

    while(True):
        message = raw_input("Type your message ('EOF' to finish): ")
        if message == 'EOF':
            break

        for ch in message.upper():
            if ch.isalpha():
                morsech = letters[ord(ch) - ord('A')]
            elif ch.isdigit():
                morsech = numbers[ord(ch) - ord('0')]
            elif ch == " ":
                sleep(4 * dotDelay) # gab between words
                continue

            for dotOrDash in morsech:
                led.on()
                if dotOrDash == ".":
                    sleep(dotDelay) # dot duration
                else: # must be "-"
                    sleep(dotDelay * 3) # dash duration
                led.off()
                sleep(dotDelay) # gap between flashes
            sleep(dotDelay * 3) # gap between letters

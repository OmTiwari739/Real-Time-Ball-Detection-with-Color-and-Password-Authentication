import pygame
import cv2
import imutils
import numpy as np
import hashlib

string = ''
hashed_password = ''
current_string_p = []
display_p = []
symbol = '*'

def get_key():
    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key

def display_box(screen, message):
    fontobject = pygame.font.Font(None, 18)
    pygame.draw.rect(screen, (0, 0, 0), ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10, 200, 20), 0)
    pygame.draw.rect(screen, (255, 255, 255), ((screen.get_width() / 2) - 102, (screen.get_height() / 2) - 12, 204, 24), 1)

    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255, 255, 255)), ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()

def ask(screen, question):
    store = ['om']
    pygame.font.init()
    current_string_un = []
    display_box(screen, question + ": " + ''.join(current_string_un))
    while True:
        inkey = get_key()
        if inkey == pygame.K_BACKSPACE:
            current_string_un = current_string_un[0:-1]
        elif inkey == pygame.K_RETURN:
            break
        elif inkey == pygame.K_LSHIFT or inkey == pygame.K_RSHIFT:
            inkey = get_key()
            if inkey <= 127:
                upper_case = inkey - 32
                current_string_un.append(chr(upper_case))
        elif inkey <= 127:
            current_string_un.append(chr(inkey))
        display_box(screen, question + ": " + ''.join(current_string_un))
    return ''.join(current_string_un)

def strong_password(password):
    passloop = 1
    has_digit = 0
    uppercase = 0

    for character in password:
        if character.isdigit():
            has_digit += 1
        if character == character.upper() and not character.isdigit():
            uppercase += 1

    if has_digit > 0 and uppercase > 0:
        passloop = 2

def main():
    global display_p
    global display_p
    display_p = []
    pygame.init()
    screen = pygame.display.set_mode((320, 240))
    clock = pygame.time.Clock()

    userName = ask(screen, "Username")
    password = ask(screen, "Password")

    pygame.quit()  # Close the Pygame window

    if userName == 'om' and password == 'om':
        for character in password:
            display_p.append(symbol)
        pro = ''.join(display_p)

        # Check password security

        # Hash password
        salt = "5gz"
        hashing_password = password + salt
        h = hashlib.md5(hashing_password.encode())

        # Object detection
        lower = {'red': (166, 84, 141), 'green': (66, 122, 129), 'blue': (97, 100, 117), 'yellow': (23, 59, 119), 'orange': (0, 50, 80)}
        upper = {'red': (186, 255, 255), 'green': (86, 255, 255), 'blue': (117, 255, 255), 'yellow': (54, 255, 255), 'orange': (20, 255, 255)}
        colors = {'red': (0, 0, 255), 'green': (0, 255, 0), 'blue': (255, 0, 0), 'yellow': (0, 255, 217), 'orange': (0, 140, 255)}

        camera = cv2.VideoCapture(0)

        while True:
            grabbed, frame = camera.read()

            if not grabbed:
                break

            frame = imutils.resize(frame, width=600)
            blurred = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

            for key, value in upper.items():
                kernel = np.ones((9, 9), np.uint8)
                mask = cv2.inRange(hsv, lower[key], upper[key])
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

                cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
                center = None

                if len(cnts) > 0:
                    c = max(cnts, key=cv2.contourArea)
                    ((x, y), radius) = cv2.minEnclosingCircle(c)
                    M = cv2.moments(c)
                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                    if radius > 0.5:
                        cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)
                        cv2.putText(frame, key + " ball", (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[key], 2)

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        camera.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

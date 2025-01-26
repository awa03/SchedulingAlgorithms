import pygame
import os
from menu_items import OptionBox, Button, TextEntry

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((640, 480))

list1 = OptionBox(
    40, 40, 200, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30), 
    ["FIFO", "Round Robin", "Shortest Job First"])

runBTN = Button (
        145, 250, 94, 40, "Run", (150, 150, 150), 0, window)

addBTN = Button (
        40, 250, 94, 40, "Add", (150, 150, 150), 3, window)

nameTXT = TextEntry(40, 100, 200, 32)
timeTXT = TextEntry(40, 150, 200, 32)
arrivalTXT = TextEntry(40, 200, 200, 32)

entrys = [nameTXT, timeTXT, arrivalTXT]
buttons = [runBTN, addBTN]

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

        for button in buttons:
            button.handle_event(event)
        for entry in entrys:
            entry.handle_event(event)

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        runBTN.changeSelection(selected_option)

    window.fill((0, 0, 0))
    list1.draw(window)

    for button in buttons: 
        button.draw();

    for entry in entrys:
        entry.draw(window)

    pygame.display.flip()
    
pygame.quit()
exit()

###### BUTTONS: #####ä
Use the "return" function with a variable of the rect you want to be a button. When you do that the "collidepoint()"
function will only take the choosen rect for the button, everything else is just going to work normaly.


Example:

def settingSaveBarTopButton(surface):
    x = pygame.draw.rect(surface, darkgray, [(210, 100), (750, 40)]) # Draw "Save" Button
    pygame.draw.rect(surface, red, [(210, 100), (750, 40)], 2)  # Draw "Save" Button
    font = pygame.font.Font("fonts/Antreas.ttf", 30)
    text = font.render("Speicherstand", True, red)
    textwidth = text.get_rect().width
    textheight = text.get_rect().height

    surface.blit(text, (210 + (750 - textwidth) / 2, 100 + (40 - textheight) / 2))

    return x


















### Made by Prossinger ###
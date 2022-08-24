

def bound_1(bound_pattern, bound, bound_list, screen):

    if bound_pattern % 16 == 1:
        screen.blit(bound, (bound_list[7][1], 50))
    if bound_pattern % 16 == 2:
        screen.blit(bound, (bound_list[6][1], 50))
    if bound_pattern % 16 == 3:
        screen.blit(bound, (bound_list[5][1], 50))
    if bound_pattern % 16 == 4:
        screen.blit(bound, (bound_list[4][1], 50))
    if bound_pattern % 16 == 5:
        screen.blit(bound, (bound_list[3][1], 50))
    if bound_pattern % 16 == 6:
        screen.blit(bound, (bound_list[2][1], 50))
    if bound_pattern % 16 == 7:
        screen.blit(bound, (bound_list[1][1], 50))
    if bound_pattern % 16 == 8:
        screen.blit(bound, (bound_list[0][1], 50))
    if bound_pattern % 16 == 9:
        screen.blit(bound, (bound_list[0][1], 50))
        screen.blit(bound, (bound_list[1][1], 50))
        screen.blit(bound, (bound_list[2][1], 50))
        screen.blit(bound, (bound_list[3][1], 50))
    if bound_pattern % 16 == 10:
        screen.blit(bound, (bound_list[4][1], 50))
        screen.blit(bound, (bound_list[5][1], 50))
        screen.blit(bound, (bound_list[6][1], 50))
        screen.blit(bound, (bound_list[7][1], 50))
    if bound_pattern % 16 == 11:
        screen.blit(bound, (bound_list[0][1], 50))
        screen.blit(bound, (bound_list[1][1], 50))
        screen.blit(bound, (bound_list[2][1], 50))
        screen.blit(bound, (bound_list[3][1], 50))
    if bound_pattern % 16 == 12:
        screen.blit(bound, (bound_list[4][1], 50))
        screen.blit(bound, (bound_list[5][1], 50))
        screen.blit(bound, (bound_list[6][1], 50))
        screen.blit(bound, (bound_list[7][1], 50))

    if bound_pattern % 16 == 13:
        screen.blit(bound, (bound_list[0][1], 50))
        screen.blit(bound, (bound_list[1][1], 50))
        screen.blit(bound, (bound_list[2][1], 50))
        screen.blit(bound, (bound_list[3][1], 50))

    if bound_pattern % 16 == 14:
        screen.blit(bound, (bound_list[0][1], 50))
        screen.blit(bound, (bound_list[1][1], 50))
        screen.blit(bound, (bound_list[2][1], 50))
        screen.blit(bound, (bound_list[4][1], 50))
        screen.blit(bound, (bound_list[5][1], 50))
        screen.blit(bound, (bound_list[6][1], 50))
        screen.blit(bound, (bound_list[7][1], 50))
    if bound_pattern % 16 == 15:
        screen.blit(bound, (bound_list[0][1], 50))
        screen.blit(bound, (bound_list[1][1], 50))
        screen.blit(bound, (bound_list[3][1], 50))
        screen.blit(bound, (bound_list[4][1], 50))
        screen.blit(bound, (bound_list[5][1], 50))
        screen.blit(bound, (bound_list[6][1], 50))
        screen.blit(bound, (bound_list[7][1], 50))

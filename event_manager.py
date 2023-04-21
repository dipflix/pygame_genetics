# added constants
import pygame
from pygame import (K_a, K_d, QUIT, KEYDOWN, KEYUP, K_ESCAPE)

LEFT_KEY = K_a
RIGHT_KEY = K_d
LURU, LDRU, LURD, LDRD = range(4)  # velocity states
LD, RD, LU, RU = range(4)  # velocity key events
VEL_EVENTS = {LD, RD, LU, RU}  # every velocity key event value
NEW_VELOCITY_GOAL, NEW_STATE = range(2)  # indices of EVENT_DECISION_TABLE entries
MAX_VELOCITY = 200


EVENT_DECISION_TABLE = [
# event       LD                     RD                    LU                    RU             # cur state
    [[-MAX_VELOCITY, LDRU], [MAX_VELOCITY, LURD], [None,         None], [None,          None]], # LURU
    [[None,          None], [None,         LDRD], [0,            LURU], [None,          None]], # LDRU
    [[None,          LDRD], [None,         None], [None,         None], [0,             LURU]], # LURD
    [[None,          None], [None,         None], [MAX_VELOCITY, LURD], [-MAX_VELOCITY, LDRU]], # LDRD
]


class EventManagement(object):
    def __init__(self, player):
        self.player = player
        self.state = LURU

    def is_doneloop(self, flag):
        global is_doneloop
        is_doneloop = flag
        return is_doneloop

    def listen(self):

        for event in pygame.event.get():
            vel_event = None

            if event.type == QUIT:
                self.is_doneloop(True)
                break
            elif event.type == KEYDOWN:
                if event.key == LEFT_KEY:
                    vel_event = LD
                elif event.key == RIGHT_KEY:
                    vel_event = RD
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    self.is_doneloop(True)
                    break
                elif event.key == LEFT_KEY:
                    vel_event = LU
                elif event.key == RIGHT_KEY:
                    vel_event = RU

            if vel_event in VEL_EVENTS:
                entry = EVENT_DECISION_TABLE[self.state][vel_event]
                if entry[NEW_VELOCITY_GOAL] is not None:
                    self.player.velocity_goal.x = entry[NEW_VELOCITY_GOAL]
                if entry[NEW_STATE] is not None:
                    self.state = entry[NEW_STATE]

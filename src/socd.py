"""
SOCD stands for simultaneous opposite cardinal direction.

Basically, what'll happen if you press "left" and "right" 
at the same time or "left" while holding "right", and 
vise versa. Every game handles it differently. 
Some set such cases to "neutral", some have "last win", 
and some games just don't know what to do and do whatever.

Devices like smashbox usually have settings that you 
can toggle to have the behavior you want. This program 
basically allows you to do the same but with your keyboard. 

If opposite directions are pressed simultaneously, 
clean accordingly:
LAST_WIN: 
    The last button to be pressed is the one that will
    take place.
    ie.: Holding left and pressing right will make the
    character go right.
NEUTRAL:
    If opposite cardinal directions are pressed 
    simultaneously, then character will not move.
PRIORITY:
    If priority is set, then for each direction,
    vertical and horizontal, there must be a priority.
    ie.: Setting priority to DOWN and RIGHT.
         Pressing up and down simultaneously will make
         the character crouch.
         Same behaviour for right and left.
"""


class BaseCleaner:
    def __init__(self):
        self.name = "Base Abstract Cleaner"

    def clean(*directions):
        return directions



class NeutralCleaner(BaseCleaner):
    def clean(self, directions):
        if directions['up'] and directions['down']:
            directions['up'] = False
            directions['down'] = False
        if directions['left'] and directions['right']:
            directions['left'] = False
            directions['right'] = False
        return directions


class LastwinCleaner(BaseCleaner):
    """
    Can clean by the last press winning or the last
    press losing.
    """
    def __init__(self):
        self.last_h = ''
        self.last_v = ''

    def clean(self, directions):
        # Horizontal cleaning
        if directions['left'] and not directions['right']:
            last_h = 'left'
        elif directions['right'] and not directions['left']:
            last_h = 'right'
        elif not (directions['left'] or directions['right']):
            last_h = ''
        elif directions['left'] and directions['right']:
            if last_h != '':
                # No previous record of horizontal
                # Decide what to do. Neutral?
                pass
            elif directions['left'] == last_h:
                directions['left'] = False
                directions['right'] = True
            elif directions['right'] == last_h:
                directions['left'] = True
                directions['right'] = False
        # Vertical cleaning
        if directions['up'] and not directions['down']:
            last_v = 'up'
        elif directions['down'] and not directions['up']:
            last_v = 'down'
        elif not (directions['up'] or directions['down']):
            last_v = ''
        elif directions['up'] and directions['down']:
            if last_v != '':
                # No previous record of horizontal
                # Decide what to do. Neutral?
                pass
            elif directions['up'] == last_v:
                directions['up'] = False
                directions['down'] = True
            elif directions['down'] == last_v:
                directions['up'] = True
                directions['down'] = False
        return directions


class PriorityCleaner(BaseCleaner):
    def __init__(self, priority_h, priority_v):
        self.name = "Priority Cleaner"
        self.priority_h = priority_h
        self.priority_v = priority_v

    def clean(self, directions):
        if directions['up'] and directions['down']:
            if self.priority_v == 'up':
                directions['up'] = True
                directions['down'] = False
            elif self.priority_v == 'down':
                directions['up'] = False
                directions['down'] = True
        if directions['left'] and directions['right']:
            if self.priority_h == 'left':
                directions['left'] = True
                directions['right'] = False
            elif self.priority_h == 'right':
                directions['left'] = False
                directions['right'] = True
        return directions
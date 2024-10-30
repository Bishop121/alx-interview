#!/usr/bin/python3
"""a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """ a function that checks if all boxes of a list can br unlocked"""
    """ the unlocked boxes will be saved in a set for uniqueness"""
    unlocked = {0}

    """a stack to save keys and visit the boxes it can open"""
    stack = [0]

    while stack:
        """ as far as there are numbers in the stack continue"""
        current_box = stack.pop()
        """ this will pop the item in the stack,
            a new way to append new item will be done
        """
        for key in boxes[current_box]:
            """ the above check the keys that are iin the current box"""
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == len(boxes)

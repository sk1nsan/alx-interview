#!/usr/bin/python3

""" Lockboxes """
from collections import deque


def canUnlockAll(boxes):
    """ Lockboxes """
    unlocked_boxes = {0}
    queue = deque()
    queue.append(0)

    while len(queue) > 0:
        box = queue.popleft()
        for key in boxes[box]:
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                queue.append(key)

    return len(boxes) == len(unlocked_boxes)

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
        if box >= len(boxes):
            continue
        while len(boxes[box]) > 0:
            key = boxes[box].pop()
            unlocked_boxes.add(key)
            queue.append(key)

    return {x for x in range(len(boxes))} == unlocked_boxes

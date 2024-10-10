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
        while len(boxes[box]) > 0:
            key = boxes[box].pop()
            if key >= len(boxes):
                continue
            unlocked_boxes.add(key)
            queue.append(key)

    return len(boxes) == len(unlocked_boxes)

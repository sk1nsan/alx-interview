#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """ Lockboxes """
    unlocked_boxes = {0}
    queue = [0]

    while (queue):
        box = queue.pop(0)
        if box > len(boxes):
            continue
        while (boxes[box]):
            element = boxes[box].pop(0)
            unlocked_boxes.add(element)
            queue.append(element)

    if (len(boxes) == len(unlocked_boxes)):
        return True
    return False

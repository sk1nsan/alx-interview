#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """ Lockboxes """
    unlocked_boxes = {0}
    queue = [0]

    while (queue):
        box = queue.pop(0)
        while (boxes[box]):
            element = boxes[box].pop(0)
            unlocked_boxes.add(element)
            queue.append(element)

    for i in range(len(boxes)):
        if (i in unlocked_boxes):
            continue
        return False
    return True

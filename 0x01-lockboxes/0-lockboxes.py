#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """ Lockboxes """
    unlocked_boxes = {0}
    queue = [0]

    while (queue):
        box = queue.pop()
        if box > len(boxes):
            continue
        while (boxes[box]):
            element = boxes[box].pop()
            unlocked_boxes.add(element)
            queue.append(element)

    return len(boxes) == len(unlocked_boxes)

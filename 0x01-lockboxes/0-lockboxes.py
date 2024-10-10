#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """ Lockboxes """
    unlocked_boxes = {0}
    queue = [0]

    if not boxes:
        return False

    while (queue):
        box = queue.pop(0)
        if box > len(boxes) - 1:
            continue
        while (boxes[box]):
            element = boxes[box].pop(0)
            unlocked_boxes.add(element)
            queue.append(element)
    return {x for x in range(len(boxes))} == unlocked_boxes

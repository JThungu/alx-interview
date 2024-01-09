#!/usr/bin/python3
"""
Each box is numbered sequentially from 0 to n - 1 and may
contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: List of boxes with keys
    :return: True if all boxes can be opened, False otherwise
    """
    if not boxes or not isinstance(boxes, list):
        return False

    opened_boxes = [0]
    for box_index in opened_boxes:
        for key in boxes[box_index]:
            if key not in opened_boxes and 0 <= key < len(boxes):
                opened_boxes.append(key)

    return len(opened_boxes) == len(boxes)

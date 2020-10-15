"""
   Helper functions for OSD
"""

import time
import cv2
import numpy as np
import logging

class destiny2_bot_osd:

    def __init__(self, width, height):
        #self.frame = ""
        self.prev_frame_time = 0
        self.width = width
        self.height = height
        self.console_msgs = []

    def fps_update(self, frame):
        new_frame_time = time.time()
        fps = 1/(new_frame_time-self.prev_frame_time)
        self.prev_frame_time = new_frame_time
        cv2.putText(frame, "{}".format(str(int(fps))),
                    (self.width-70, 35), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (100, 255, 0), 3, cv2.LINE_AA)
        return()

    def write_console(self, frame):
        # length of console
        n = 4
        # First we crop the sub-rect from the image
        x, y, w, h = 0, self.height-200, self.width, self.height
        sub_img = frame[y:y+h, x:x+w]
        white_rect = np.zeros(sub_img.shape, dtype=np.uint8)

        res = cv2.addWeighted(sub_img, 0.5, white_rect, 0.5, 1.0)

        # Putting the image back to its position
        frame[y:y+h, x:x+w] = res

        for msg in self.console_msgs:
            cv2.putText(frame, "{}".format(msg),
                        (0, self.height-(200-(n*35))),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (100, 255, 0), 2, cv2.LINE_AA)
            n = n - 1
        return()

    def add_console(self, message):
        logging.info("add_console: {}".format(message))
        self.console_msgs.insert(0, message)
        if len(self.console_msgs) > 4:
            self.console_msgs.pop()
        for msg in self.console_msgs:
            logging.debug("add_console: msgs {}".format(msg))

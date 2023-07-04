"""cias_debugger - error and info message handler for cias

This module handles error and info messages.


Requirements
------------
time : Needed to timestamp events and track execution times.
sys : Allow the debugger to access exit() and others

Classes
-------
CiasDebugger : Logging class for cias.
"""

import time
import sys


class CiasDebugger(object):
    def __init__(self):
        self.stats = {}

        # self.messages contains every logged message sent to the debugger
        self.messages = []

        # If there are more than messages_size_limit elements in self.messages,
        # begin trimming self.messages at index [1].  Retain [0] because it
        # has the timestamp of when logging began
        self.messages_size_limit = 10000

        self.printEnabled = True

        # self.time_format for how to display timestamps on-screen
        # https://docs.python.org/3/library/time.html#time.strftime
        self.time_format = "%Y-%m-%d %H:%M:%S %z"

        self.message("DEBG", "Started debugger")

        # Some attributes to calculate and track loop run speed
        self.runtime_ticks = 0
        self.runtime_tick_time = time.time()
        self.runtime_mhz = 0

        # A bit to track whether a new log message has been seen.
        # For ex, set to False, then check if it's True.  if so,
        # a message has been seen by the debugger in the meantime.
        self.new_messages = False

    def perf_monitor(self):
        # Non-blocking method run once per main-loop execution cycle
        # Tracks and reports loop execution speed
        sample_size = 10000000
        self.runtime_ticks += 1
        if self.runtime_ticks > sample_size:
            self.runtime_mhz = ((sample_size / (time.time() -
                                                self.runtime_tick_time)) /
                                1000000)  # Divide by a million for MHz
            self.message("DEBG", "(Counter) Main loop execution MHz: {}".
                         format(self.runtime_mhz))
            self.runtime_ticks = 0
            self.runtime_tick_time = time.time()

    def log_stat(self, statistic, increment: int, value=0):
        if statistic not in self.stats:
            self.stats[statistic] = int(increment) or int(value)
        else:
            self.stats[statistic] += int(increment)

    def get_stat(self, statistic):
        if statistic not in self.stats:
            return 0
        else:
            return int(self.stats[statistic])

    def report_stat(self, statistic, mod=100):
        if self.printEnabled and statistic in self.stats:
            if (self.stats[statistic] == 1) or \
                    (self.stats[statistic] % mod == 0):
                self.message("DEBG", "(Counter) {}: {}".format(
                    statistic, self.stats[statistic]))

    def message(self, severity, message):
        timestamp = time.time()
        self.new_messages = True
        self.messages.append({"severity": severity,
                              "message": message,
                              "timestamp": timestamp})

        # Trim self.messages if it's grown over self.messages_size_limit
        # del at index [1] so that we always retain the very first message,
        # which contains the timestamp of the beginning of logging.
        # Otherwise the logged messages list would just grow indefinitely

        if len(self.messages) > self.messages_size_limit:
            del self.messages[1]

        if self.printEnabled:
            message_string = "{}- {}".format(severity, message)
            print(time.strftime(self.time_format, time.localtime(timestamp)),
                  message_string)

    def exit(self, message):
        self.message("EXIT", message)
        sys.exit(message)

    def summary(self):
        for stat in self.stats:
            self.message("DEBG",
                         "{}: {}".format(stat, self.stats[stat]))
        self.message("DEBG",
                     "Runtime: {} seconds".format((
                             self.messages[-1]["timestamp"] -
                             self.messages[0]["timestamp"])))
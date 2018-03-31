#!/usr/bin/env python
import re
import time
import argparse
import subprocess
import ConfigParser


def pinger(src, dst, count):
    params = ['ping', '-c', count, '-I', str(src), str(dst)]
    send_ping = subprocess.Popen(params, stdout=subprocess.PIPE)
    result, err = send_ping.communicate()
    success = re.search("rtt min", result)
    if success:
        my_line = success.string.rstrip()
        ping_time = my_line.split('\n')
        return ping_time[-1]
    else:
        return "No reply"


def get_next_index(current, max_index):
    if current == max_index-1:
        return 0
    else:
        return current+1

counter = 1
number_of_iterations = 100
max_log_files = 10
log_files = ["ping_results"+str(a)+".log" for a in range(max_log_files)]
current_file = 0  # to select file name from log_files[]
file_size_limit = 1000   # in bytes
log_file = open(log_files[current_file], 'w')
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--config_file', dest="config_file")
args = parser.parse_args()
ini_config = ConfigParser.RawConfigParser(allow_no_value=True)
ini_config.read(args.config_file)
while counter <= number_of_iterations:  # later to be replaced with while True
    for ip_src in ini_config.sections():
        for ip_dst in ini_config.options(ip_src):
            my_result = pinger(ip_src, ip_dst, '1')
            logline = str(time.time()) + " " + ip_src + " " + ip_dst + \
                " " + my_result + "\n"
            log_file.write(logline)
        log_file.flush()
        if log_file.tell() >= file_size_limit:
            log_file.close()
            current_file = get_next_index(current_file, max_log_files)
            log_file = open(log_files[current_file], 'w')
        time.sleep(10)
    counter = counter+1
log_file.close()

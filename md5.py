from __future__ import print_function
from __future__ import division

import hashlib
import logging
import os
import time

from multiprocessing.pool import ThreadPool

import tools


target_dir = 'static/data'
target_files = [os.path.join(target_dir, x) for x in os.listdir(target_dir)]


def get_md5(target):
    """Calculates md5 checksum for system file

    Args:
        target (str):  Path to file

    Returns:
        hash (str): md5 checksum string.
        target (str): original target file path input.
    """
    m = hashlib.md5()
    with open(target) as fid:
        m.update(fid.read())
    hash = m.hexdigest()
    return hash, target


@tools.timer
def serial_md5():
    """md5 calculation test for serial processing
    
    Returns:  
        md5s (list):  List of tuples containing md5 checksum string
            and target file path.
    """
    md5s = []
    for file_path in target_files:
        md5s.append(get_md5(file_path))
    return md5s


@tools.timer
def threaded_md5(threads=8):
    """md5 calculation test for serial processing

    Args:
        threads (int): Number of spawned threads. Defaults to `8`.

    Returns:  
        md5s (list):  List of tuples containing md5 checksum string
            and target file path.
    
    Notes:
        Uses multiprocessing thread dummy tool.
    """
    pool = ThreadPool(threads)
    md5s = pool.map(get_md5, target_files)
    return md5s


def test(output_path='test.md5'):
    """Speed test for serial and threaded md5 generation

    Args:
        output_path (str):  System path for threaded md5 checksum log

    Notes:
        Used log to confirm checksum veracity.
    """
    logging.basicConfig(level=logging.DEBUG)

    md5s_serial, time_serial = serial_md5()
    md5s_threaded, time_threaded = threaded_md5()

    # time.sleep(0.25)
    # print('md5s_threaded == md5s_serial:', md5s_threaded == md5s_serial)

    with open(output_path, 'w') as fid:
        for md5 in md5s_threaded:
            fid.write(' '.join(md5) + '\n')


if __name__ == '__main__':
    test()

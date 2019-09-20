import functools
import logging
import time


def timer(func):
    """Timing decorator with hooks to Python logging
    
    Logs execution time at log level `info`.
    
    Args:
        func (method):  Any method to be timed
        
    Returns:
        func method output.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)  # wrapped method call
        end = time.time()
        execution_time = end - start

        logging.info('`{function}` execution time: {exec_time}'.format(
            function=func.__name__, exec_time=execution_time))

        return output, execution_time
    return wrapper

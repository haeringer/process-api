import os
import psutil


def dict_to_list(dict_):
    """
    Takes an unnested dictionary and turns it into a list,
    containing the key-value pairs also in list format.
    """

    list_ = []
    try:
        for key, value in dict_.items():
            sublist = [key, value]
            list_.append(sublist)
        return list_
    except AttributeError:
        return None


def format_process_dict(pinfo):
    """
    Takes the dictionary from psutils' as_dict() function
    and formats it for better readability.
    """

    environ_list = dict_to_list(pinfo['environ'])

    pinfo_formatted = {
        'Name': pinfo['name'],
        'PID': pinfo['pid'],
        'PPID': pinfo['ppid'],
        'Environment': environ_list,
        'Command': pinfo['cmdline'],
    }
    return pinfo_formatted


def get_processes():
    """
    Return all processes running on the host system, except
    the ones belonging to the current group of processes.
    """

    processes = []
    pgid_current = os.getpgid(0)

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=[
                'name', 'pid', 'ppid', 'environ', 'cmdline',
            ])
            pgid = os.getpgid(pinfo['pid'])
        except psutil.NoSuchProcess:
            pass
        else:
            if pgid != pgid_current:
                process = format_process_dict(pinfo)
                processes.append(process)

    return processes

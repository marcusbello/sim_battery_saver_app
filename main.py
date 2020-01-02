import psutil


def get_apps():
    list_app = [p.info for p in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']) if p.info['cpu_percent'] > 0]
    return list_app


get_apps()


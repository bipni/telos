from stock.myip import MyIP

import socket
import multiprocessing
import os
import subprocess

class ScanIP:

    @staticmethod
    def pinger(job_q, results_q):
        DEVNULL = open(os.devnull, 'w')

        while True:
            ip = job_q.get()

            if ip is None:
                break

            try:
                subprocess.check_call(['ping', '-c1', ip], stdout=DEVNULL)
                results_q.put(ip)
            except:
                pass

    @staticmethod
    def scan_ip():
        print('Please wait a while...')

        ips = []

        my_ip = MyIP.get_ip().split('.')
        network = my_ip[0] + '.' + my_ip[1] + '.' + my_ip[2] + '.'

        jobs = multiprocessing.Queue()
        results = multiprocessing.Queue()

        pools = [multiprocessing.Process(target=ScanIP.pinger, args=(jobs, results)) for i in range(255)]

        for pool in pools:
            pool.start()
        
        for i in range(1, 255):
            jobs.put(network + '{0}'.format(i))
        
        for pool in pools:
            jobs.put(None)
        
        for pool in pools:
            pool.join()
        
        while not results.empty():
            ip = results.get()
            ips.append(ip)
        
        return ips

def run():
    return ScanIP.scan_ip()
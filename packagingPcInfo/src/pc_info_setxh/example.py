import os, socket, argparse, sys

class PC_DATA():
   
    def __init__(self) -> None:
        argv=sys.argv[1:]
        OS = os.environ['OS']
        HNAME=socket.gethostname()
        IP=socket.gethostbyname(HNAME)
        p = argparse.ArgumentParser(description="This is some program")
        # An option taking an argument
        p.add_argument("-n","--pcname",default=HNAME)
        # An option that sets a Boolean flag
        p.add_argument("-i","--ip", action="store", default=IP)
        p.add_argument("-os","--system", action="store",default=OS)
        args = p.parse_args(args=argv)
        self._pcname = args.pcname
        self._ip = args.ip
        self._system = args.system
    
    @property
    def pcname(self):
        '''GET PC NAME'''
        return self._pcname

    @property
    def ip(self):
        '''GET IP NAME'''
        return self._ip

    @property
    def system(self):
        '''GET OS NAME'''
        return self._system

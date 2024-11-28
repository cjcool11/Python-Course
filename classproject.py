class games:
    def __init__(self,gamename,gametype):
        self.gamename = gamename
        self.gametype = gametype

COD = games("Call Of Duty","FPS")
SolsRNG = games("SolsRNG","RNG")
print("{} is an {} game!".format(COD.gamename,COD.gametype))
print("{} is an {} game!".format(SolsRNG.gamename,SolsRNG.gametype))
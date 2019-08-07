from z3 import *
import string, sys

def main():
	s = Solver()
	nMF = Int('nMF')
	nFF = Int('nFF')
	nSS = Int('nSS')
	nHW = Int('nHW')
	nMS = Int('nMS')
	nSP = Int('nSP')

	total = RealVal(15.05)
	set_option(precision=2)
	cMF = RealVal(2.15)
	cFF = RealVal(2.75)
	cSS = RealVal(3.35)
	cHW = RealVal(3.55)
	cMS = RealVal(4.20)
	cSP = RealVal(5.80)
	s.add(nMF <= 6)
	s.add(nMF>=0)
	s.add(nFF>=0)
	s.add(nSS>=0)
	s.add(nHW>=0)
	s.add(nMS>=0)
	s.add(nSP>=0)
	s.add(((nMF*cMF) + (nFF*cFF) + (nSS*cSS) + (nHW*cHW) + (nMS*cMS) + (nSP*cSP)) == total)
	t=s.model
	print(s.check())
	while(s.check() == sat):
		print(s.model())
		s.add(Or(nMF!=s.model()[nMF], nFF!=s.model()[nFF], nSS!=s.model()[nSS], nHW!=s.model()[nHW], nMS!=s.model()[nMS], nSP!=s.model()[nSP]))

if __name__ == "__main__":
	main()
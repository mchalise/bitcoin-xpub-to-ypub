import base58
import sys
def main():
  bin_xpub=base58.b58decode_check('xpub6Brj1doPBv4VcDuSybR3njmYnEdfkLarPTU64q4iauqSSSqYQcU2GyiHeyhKQq4pn5TdY2vqm8ezLFQ8fVveQjGnBcKqP1nCB9kpNBpgsMn')
  prefix="049d7cb2".decode("hex")
  bin_ypub=bin_xpub
  bin_ypub=prefix + bin_ypub[4:]
  ypub=base58.b58encode_check(bin_ypub)
  print ypub

if __name__=="__main__":
  main()

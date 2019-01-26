require 'btcruby'

bin_xpub = BTC::Base58.data_from_base58check('xpub6Brj1doPBv4VcDuSybR3njmYnEdfkLarPTU64q4iauqSSSqYQcU2GyiHeyhKQq4pn5TdY2vqm8ezLFQ8fVveQjGnBcKqP1nCB9kpNBpgsMn')
prefix = ['049d7cb2'].pack('H*')
bin_ypub=bin_xpub
bin_ypub=prefix + bin_ypub[4..-1]
ypub=BTC::Base58.base58check_from_data(bin_ypub)
print ypub

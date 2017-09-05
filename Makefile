.PHONY: clean

all : openhash closedhash bst trie pot floyd dfs clean

openhash:
	@python openhash.py
closedhash:
	@python closedhash.py
bst:
	@python bst.py
trie:
	@python trie.py
pot:
	@python pot.py
floyd:
	@python floyd.py
dfs:
	@python dfs.py

clean:
	@\rm -f *.pyc
.PHONY: clean

all : openhash closedhash bst trie pot floyd dfs closed-delete.csv closed-insert.csv open-delete.csv open-insert.csv clean 

closed-delete.csv closed-insert.csv: closedhash.py
	python closedhash.py

open-delete.csv open-insert.csv: openhash.py
	python openhash.py

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
all: closed-delete.csv closed-insert.csv open-delete.csv open-insert.csv

closed-delete.csv closed-insert.csv: closedhash.py
	python closedhash.py

open-delete.csv open-insert.csv: openhash.py
	python openhash.py

clean:
	rm -f closed-delete.csv closed-insert.csv open-delete.csv open-insert.csv


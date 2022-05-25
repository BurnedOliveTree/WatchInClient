INTERPRETER = python3

install: requirements.txt
	$(INTERPRETER) -m pip install -r requirements.txt

run: install
	$(INTERPRETER) main.py
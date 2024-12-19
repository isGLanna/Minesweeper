VENV_DIR = ./VENV_DIR

.PHONY: all
all: run

.PHONY: run
run: 
	python3 Main.py

.PHONY: clean
clean: 
	rm -rf $(VENV_DIR)
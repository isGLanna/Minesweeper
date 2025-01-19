VENV_DIR = ./VENV_DIR
PYTHON = python3.11
MAIN_SCRIPT = Main.py

.PHONY: all
all: setup run

.PHONY: setup
setup: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt
	touch $(VENV_DIR)/bin/activate

.PHONY: run
run: $(VENV_DIR)/bin/activate
	$(VENV_DIR)/bin/python $(MAIN_SCRIPT)

.PHONY: clean
clean:
	rm -rf $(VENV_DIR)

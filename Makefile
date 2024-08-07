.PHONY: connect_wifi show_ip clean

VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

venv: requirements.txt
	@python3 -m venv $(VENV)
	@$(PIP) install -r requirements.txt

connect_wifi: venv
	@$(PYTHON) connect_wifi.py

show_ip: venv
	@$(PYTHON) show_ip.py

clean:
	rm -rf $(VENV)

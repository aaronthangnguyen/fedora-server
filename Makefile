.PHONY: connect_wifi show_ip clean

VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate


connect_wifi: $(VENV)/bin/activate
	$(PYTHON) connect_wifi.py

show_ip: $(VENV)/bin/activate
	$(PYTHON) show_ip.py

clean:
	rm -rf $(VENV)

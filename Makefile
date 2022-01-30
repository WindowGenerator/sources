
VENV = .venv
LOGS = .logs

create-venv:
	python3.9 -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install -r ./requirements.txt -r ./requirements.dev.txt


start-receiver:
	python3 -m receiver.main
	
start-transmitters:
	mkdir -p $(LOGS)

	nohup python3 -m transmitters.main \
		--data-path source_1.json \
		--port 8091 > .logs/slave_1.log &

	nohup python3 -m transmitters.main \
		--data-path source_2.json \
		--port 8092 > .logs/slave_2.log &

	nohup python3 -m transmitters.main \
		--data-path source_3.json \
		--port 8093 > .logs/slave_3.log &

stop-transmitters:
	# TODO: надо нормально получать PID и грохать процессы
	pkill -f transmitters.main
	

format:
	isort --apply --recursive ./
	black --skip-string-normalization ./
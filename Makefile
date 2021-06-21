init:
	#virtualenv --python=python3.8 venv
	#source $(pwd)/venv/bin/activate
	export PYTHONPATH=$PYTHONPATH:$PWD/src

test:
	pytest .

.PHONY: init test

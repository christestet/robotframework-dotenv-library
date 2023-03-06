install: venv hooks

hooks: venv
	$(VENV)/pre-commit install

docs: venv
	$(VENV)/libdoc RobotDotenv/DotenvLibrary.py docs/index.html

test: python-test robot-test

python-test: venv
	$(VENV)/pytest tests

robot-test: venv
	$(VENV)/robot  --log NONE --output NONE --report NONE tests

clean: clean-venv
	-rm -rf log.html output.xml report.html Makefile.venv *.egg-info .pytest_cache

include Makefile.venv
Makefile.venv:
	curl \
		-o Makefile.fetched \
		-L "https://github.com/sio/Makefile.venv/raw/v2020.08.14/Makefile.venv"
	echo "5afbcf51a82f629cd65ff23185acde90ebe4dec889ef80bbdc12562fbd0b2611 *Makefile.fetched" \
		| sha256sum --check - \
		&& mv Makefile.fetched Makefile.venv

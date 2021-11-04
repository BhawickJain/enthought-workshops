# Signifies our desired python version
# Makefile macros (or variables) are defined a little bit differently than traditional bash, keep in mind that in the Makefile there's top-level Makefile-only syntax, and everything else is bash script syntax.
PYTHON = python3

# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = help setup test run clean

# Defining an array variable
FILES = input output

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "make container"
	@echo "     Setup and Run docker compose container"
	@echo "make setup"
	@echo "     Install custom packages in editable mode"
	@echo "make test"
	@echo "     Run tests"
	@echo "make run"
	@echo "     run project (to be continued)"
	@echo "make container-clean"
	@echo "     Remove container image and volume data"
	@echo "make nbs"
	@echo "     compiles ipynbs into markdown and run clean script afterwards"
	@echo "make clean"
	@echo "     remove cached folders and files from testing and nbs"
	@echo "make typing"
	@echo "     Run type hinting checker"

container:
	docker compose up

container-clean:
	docker compose down -v --rmi all

# This generates the desired project file structure
# A very important thing to note is that macros (or makefile variables) are referenced in the target's code with a single dollar sign ${}, but all script variables are referenced with two dollar signs $${}
setup:
	@echo "installing packages..."
	pip install -e pyExamples
	@echo "done."
	
# The ${} notation is specific to the make syntax and is very similar to bash's $() 
# This function uses pytest to test our source files
# Run linter first to catch obvious errors
test: typing
	${PYTHON} -m pytest
	
run:
	@echo "${PYTHON} our_app.py - command not setup yet"

# In this context, the *.project pattern means "anything that has the .project extension"
# '-' in `-rm` to ignore errors thrown by command.
# https://stackoverflow.com/questions/2670130/make-how-to-continue-after-a-command-fails
clean:
	@echo "cleaning project..."
	@-rm -r .Trash-0
	@-rm -r .mypy_cache
	@-rm -r .pytest_cache
	@-rm -r __pycache__
	# - allows exit 0 regardless of outcome
	@-mv -f nbs/*.md .
	@-mv -f *.ipynb nbs/
	@echo "done."

# https://jupytext.readthedocs.io/en/latest/using-cli.html
notebooks:
	-jupytext --to md nbs/*.ipynb
	# TODO potentially bad practice
	make clean

typing:
	${PYTHON} -m mypy --ignore-missing-imports pyExamples
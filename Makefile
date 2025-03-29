.ONESHELL:

BASE=~/Desktop
VENV_NAME=ptmdb

all:
	$(MAKE) help
help:
	@echo "--------------"
	@echo "		HELP     "
	@echo "--------------"
	@echo "make help"
	@echo "		Display help"
	@echo "make install"
	@echo "		Install everything"
	@echo "make clear"
	@echo "		Delete all the files"
	@echo "--------------"

install:
	@python3 -m venv $(BASE)/$(VENV_NAME)
	@source	$(BASE)/$(VENV_NAME)/bin/activate
	@$(MAKE) setup
	@$(MAKE) requirements
	@echo "Install done"

setup:
	@cp ./plex.py $(BASE)/$(VENV_NAME)
	@cp ./tmdb.py $(BASE)/$(VENV_NAME)
	@cp ./script.py $(BASE)/$(VENV_NAME)
	@cp ./constants.py $(BASE)/$(VENV_NAME)
	@cp -r ./icons $(BASE)/$(VENV_NAME)

requirements:
	$(BASE)/$(VENV_NAME)/bin/pip install -r requirements.txt

clear:
	@rm -rf $(BASE)
	@echo "Files deleted"

.PHONY: help install clear

# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


# target: clean - Clean all ".pyc" files
clean:
	find . -name "*.pyc" -exec rm -rf {} \;


# target: migrate - Migrate all django applications considering app dependencies
migrate:
	python redinstagram/manage.py makemigrations redinstagram
	python redinstagram/manage.py migrate


# target: clean_migration - folders in all django apps
clean_migrations:
	ls redinstagram/ | grep -v -e 'manage.py' | xargs -I{} rm -rf redinstagram/{}/migrations/


# target: test - execute project related tests including coding convention and unittest
test:
	flake8 redinstagram/
	redinstagram/manage.py test redinstagram/ -v 2

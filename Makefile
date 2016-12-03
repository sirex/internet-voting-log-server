.PHONY: test
test:
	DJANGO_SETTINGS_MODULE=logserver.settings py.test -vvx --tb=native tests

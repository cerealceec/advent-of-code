_default:
  just --list

<<<<<<< HEAD
# run linting and typecheking over the solutions
@lint:
	ruff solutions
	pyright

=======
# error out if this isn't being run in a venv
_require-venv:
    #!/usr/bin/env python
    import sys
    sys.exit(sys.prefix == sys.base_prefix)

# install dev deps
@install: _require-venv
  # extra flags make this ~ as fast as I want
  pip install -r requirements.txt --quiet --disable-pip-version-check

# run linting and typecheking over the solutions
@lint: _require-venv install
  ruff check --quiet
  ruff format --check --quiet
  pyright

# run every solution for a given year
@validate year:
	for i in $(seq 1 25); do ./advent $i --slow --year {{year}}; echo; done;
>>>>>>> template/main

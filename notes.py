I got below while run pytest -
pytest
pytest: The
term
'pytest' is not recognized as the
name
of
a
cmdlet, function, script
file, or operable
program.Check
the
spelling
of
the
name, or if a path was included,
verify
that
the
path is correct and
try again.
At
line: 1
char: 1
+ pytest
+ ~~~~~~
+ CategoryInfo: ObjectNotFound: (pytest:String)[], CommandNotFoundException
+ FullyQualifiedErrorId: CommandNotFoundException


so i use this -
Verify pytest installation and location.
After installation, you can try running python -m pytest instead of just pytest.

python - m pytest

for generate report i unable to generate because he may be not recgnized

    i use python -m pytest --html=report.html
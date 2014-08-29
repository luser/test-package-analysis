Usage
=====

Write a manifest from a test package:
(mkdir tests; cd tests; unzip /path/to/tests.zip)
python writemanifest.py tests > tests-manifest.json

Analyze a set of manifests:
python analyzemanifests.py tests-manifest.json [another-manifest.json ...]

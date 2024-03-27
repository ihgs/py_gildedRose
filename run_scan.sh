#!/bin/bash
sonar-scanner \
  -Dsonar.projectKey=gilded-rose \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.token=sqp_333369453e9e18f3e7973fda335c2ae175c04a8f \
  -Dsonar.python.coverage.reportPaths=coverage.xml \
  -Dsonar.exclusions=**/test_*
#!/usr/bin/env bash
echo "running unit test"
pytest libs

echo "running Robotframework test"
robot atest
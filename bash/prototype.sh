#!/bin/bash

################################################################################
# LOGGER: DEFINE FUNCTIONS
################################################################################
logger_info() {
  local message="$1"
  local level="INFO"
  echo "${level}: ${message}"
  echo "${level}: ${message}" >> "${LOG_FILE}"
}

logger_fatal() {
  local message="$1"
  local level="FATAL"
  echo "${level}: ${message}"
  echo "${level}: ${message}" >> "${LOG_FILE}"
  exit 1
}

################################################################################
# PROTOTYPE: EXECUTE
################################################################################


execute() {
  echo "Hello prototype!"
}

execute;
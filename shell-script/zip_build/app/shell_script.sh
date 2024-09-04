#!/usr/bin/bash
#
# Shell script for a Tapis V3 application
# Check:
#  - two incoming arguments: arg1 arg2
#  - environment variables
#
# NOTE: To run manually please see instructions in README
#
PrgName=$(basename "$0")

USAGE="Usage: $PrgName arg1 arg2"

ARG1=$1
ARG2=$2

# Set directory for output
export OUT_DIR=/TapisOutput
# If standard Tapis output directory is not available then output to current directory
if [ ! -d "$OUT_DIR" ]; then
  OUT_DIR=.
fi

{
echo "Running script: $PrgName with arguments: $*"
echo "id=$(id)"
echo "PWD=$(pwd)"
echo "HOME=$HOME"
echo "========================================="

#
# Check number of arguments
#
if [ $# -ne 2 ]; then
  echo "Expected two arguments: arg1 arg2"
  echo "$USAGE"
  echo "FAILED"
  exit 1
fi

echo "Found expected number of app args."

#
# Check argument values
#
if [ "$ARG1" != "arg1" ]; then
  echo "First argument was not arg1"
  echo "$USAGE"
  echo "FAILED"
  exit 1
fi
echo "Found expected arg1 value."

if [ "$ARG2" != "arg2" ]; then
  echo "Second argument was not arg2"
  echo "$USAGE"
  echo "FAILED"
  exit 1
fi
echo "Found expected arg2 value."

#
# Check that all environment variables expected are set
# NOTE: Bash can distinguish between not set (a.k.a. null) and set but no value (a.k.a. empty string)
#       The expression ${env_variable-set_because_null} expands to "set_because_null" only if
#       env_variable was not set.
# NOTE: The use of {!ev_name} allows us to reference the loop variable as an environment variable name.
#
# NOTE: When this is run via docker using --env-file it appears that variables without a value are unset, so
#       we can only check for variables with a value. Possibly because they are not exported.
# NOTE: This means we are unable to support env variables that are set but empty when running a Tapis job.
# Variables that should be set but empty.
# EV_CHECK_SET="APP_ALL_DEFAULTS APP_BY_DEFAULT_DEFAULT APP_ONLY_FIXED_DEFAULT"
# EV_CHECK_SET="$EV_CHECK_SET SYS_ALL_DEFAULTS SYS_BY_DEFAULT_DEFAULT SYS_ONLY_FIXED_DEFAULT"

EV_CHECK_SET="MY_ENV1"
for ev in $EV_CHECK_SET
do
  ev_name=$ev
  ev_resolved=${!ev_name-x_set_because_null}
  if [ "${ev_resolved}" == "x_set_because_null" ]; then
    echo "Environment variable not set. Environment variable: $ev_name"
    echo "FAILED"
    exit 1
  fi
  echo "Found environment variable: $ev with value: $ev_resolved"
done

#
# Check specific values for environment variables
#
# ---------------------------------------------
if [ "$MY_ENV1" != "env_1_value" ]; then
  echo "Environment variable had incorrect value. Expected: env_1_value Found: $ENV_1"
  echo "FAILED"
  exit 1
fi
echo "Found expected MY_ENV1 value: $ENV_1"

echo "================================"
echo "Success"
} | tee $OUT_DIR/shell_script.out
exit 0

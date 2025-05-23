#!/bin/bash
export $(grep -v '^#' .env | xargs)

uvicorn app.core.app_instance:app \
  --host $HOST \
  --port $PORT \
  $( [ "$RELOAD" = "true" ] && echo "--reload" )

#uvicorn app.core.app_instance:app --host 0.0.0.0 --port 8800
#!/bin/bash

FIB_URL="http://flask-app-alb-v2-30219326.us-east-1.elb.amazonaws.com:5000/fib"
CONVERT_URL="http://flask-app-alb-v2-30219326.us-east-1.elb.amazonaws.com:5000/convert"

# Function to send a single request using ab
send_single_request() {
  ab -n 1 -c 1 "$1"
}

# Function to send 100 requests in batches of 10 concurrent connections
send_batch_requests() {
  ab -n 100 -c 10 "$1"
}

echo "Starting First Phase: 3 cycles with 1 request each and 5 min gaps..."

for i in {1..3}
do
  echo "[Cycle $i] Sending 1 request to /fib..."
  send_single_request "$FIB_URL"

  echo "Sleeping 5 minutes..."
  sleep 300  # 5 minutes

  echo "[Cycle $i] Sending 1 request to /convert..."
  send_single_request "$CONVERT_URL"

  echo "Sleeping 5 minutes..."
  sleep 300  # 5 minutes
done

echo "Starting Second Phase: 3 rounds of 100 requests (10 at a time) with gaps..."

for i in {1..3}
do
  echo "[Round $i] Sending 100 requests to /fib with concurrency 10..."
  send_batch_requests "$FIB_URL"

  echo "Sleeping 5 minutes before /convert..."
  sleep 300  # 5 minutes

  echo "[Round $i] Sending 100 requests to /convert with concurrency 10..."
  send_batch_requests "$CONVERT_URL"

  echo "Sleeping 5 minutes before next round..."
  sleep 300  # 5 minutes
done

echo "All request cycles completed."

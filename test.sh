#!/bin/bash

OPENAI_API_KEY=secret_
LAMBDA_API_KEY=secret_
OPENAI_API_BASE="https://api.lambdalabs.com/v1"

# Loop through num_concurrent_requests in powers of 2 (1, 2, 4, 8, 16, 32)
for num_concurrent_requests in 1 2 4 8 16 32 64
do
    # Calculate max_num_completed_requests as 2x num_concurrent_requests
    max_num_completed_requests=$((2 * num_concurrent_requests))

    # Run the Python script with the calculated parameters
    python token_benchmark_ray.py \
    --model "405bnmfp8" \
    --mean-input-tokens 16000 \
    --stddev-input-tokens 1600 \
    --mean-output-tokens 4000 \
    --stddev-output-tokens 400 \
    --max-num-completed-requests ${max_num_completed_requests} \
    --timeout 3600 \
    --num-concurrent-requests ${num_concurrent_requests} \
    --results-dir "result_outputs_q${max_num_completed_requests}_c${num_concurrent_requests}" \
    --llm-api openai \
    --additional-sampling-params '{}'
done

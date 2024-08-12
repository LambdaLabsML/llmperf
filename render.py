import json
import os
import matplotlib.pyplot as plt

# List of indices to loop through
indices = [1, 2, 4, 8, 16, 32, 64]

# Initialize lists to store data for plotting
latencies = []
throughputs = []
labels = []

# Loop through each index
for index in indices:
    # Construct the folder and file path
    folder_name = f"result_outputs_q{2 * index}_c{index}"
    file_path = os.path.join(folder_name, "405bnmfp8_550_150_summary.json")
    
    try:
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Extract the required values
        latency = data.get("results_end_to_end_latency_s_mean")
        throughput = data.get("results_request_output_throughput_token_per_s_mean")
        
        # Store the data for plotting
        latencies.append(latency)
        throughputs.append(throughput)
        labels.append(f"concur={index}")
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except KeyError as e:
        print(f"Key {e} not found in file: {file_path}")

# Plotting the data
plt.figure(figsize=(10, 6))
plt.scatter(latencies, throughputs)

# Annotating each data point with its label
for i, label in enumerate(labels):
    plt.annotate(label, (latencies[i], throughputs[i]), textcoords="offset points", xytext=(5,5), ha='right')

# Labeling the axes
plt.xlabel("results_end_to_end_latency_s_mean")
plt.ylabel("results_request_output_throughput_token_per_s_mean")
plt.title("Latency vs Throughput for Different Concurrent Requests")

# Set the x-axis to start from 0
plt.xlim(0, None)

# Save the plot as a PNG file
output_file = "latency_vs_throughput.png"
plt.grid(True)
plt.savefig(output_file)
print(f"Plot saved as {output_file}")

import os
import pandas as pd
import matplotlib.pyplot as plt

files = os.listdir("exp")
files = [f for f in files if f.startswith("num_k")]

# Initialize empty list to store dataframes
dfs = []

# Read each CSV file and append to list
for file in files:
    try:
        df = pd.read_csv(f"exp/{file}", header=None)
    except:
        from IPython import embed
        embed()
    # Extract rank and num_k from filename
    parts = file[5:].split('_')
    rank = None
    num_k = None
    
    for i, part in enumerate(parts):
        if part == 'rank':
            rank = int(parts[i+1])
        elif part == 'k':
            num_k = int(parts[i+1].split('.')[0])  # Remove .csv extension
            
    df['rank'] = rank
    df['num_k'] = num_k
    dfs.append(df)

# Concatenate all dataframes
combined_df = pd.concat(dfs, ignore_index=True)



# Create line plot
plt.figure(figsize=(10, 6))

# Get unique ranks
ranks = combined_df['rank'].unique()
# Sort data by num_k for proper line connections
combined_df = combined_df.sort_values('num_k')

# Sort ranks for ordered legend
ranks = sorted(ranks)

# Plot line for each rank
for rank in ranks:
    rank_data = combined_df[combined_df['rank'] == rank]
    plt.plot(rank_data['num_k'], rank_data[1], marker='o', label=f'rank={rank}')

plt.xlabel('Number of Random Basis')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Number of Random Basis for Different Ranks')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('exp/num_k_accuracy_plot.png')
plt.close()

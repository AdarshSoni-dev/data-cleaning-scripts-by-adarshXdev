import pandas as pd
import matplotlib.pyplot as plt
import os

# === Step 1: Load data ===
# Use absolute path only for the raw input file (you can make this dynamic too)
raw_data_path = 'D:/freelance-gigs/Data-cleaning-scripts/sample_data/netflix_watch_history.csv'
df = pd.read_csv(raw_data_path)

# === Step 2: Clean data ===
df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime
daily_count = df.groupby('Date').size()  # Count titles per day
cleaned_df = df.drop_duplicates()        # Remove duplicates

# === Step 3: Prepare smart paths for saving cleaned data and plot ===
# This makes your script dynamic — doesn't depend on where you run from
base_dir = os.path.dirname(os.path.dirname(__file__))  # Go one folder up from /scripts
clean_data_path = os.path.join(base_dir, 'cleaned_data', 'netflix_cleaned.csv')
plot_save_path = os.path.join(base_dir, 'plots', 'watch_time_trend.png')

# === Step 4: Save cleaned data ===
os.makedirs(os.path.dirname(clean_data_path), exist_ok=True)  # Auto create if needed
cleaned_df.to_csv(clean_data_path, index=False)

# === Step 5: Create & save plot ===
plt.figure(figsize=(10, 5))
daily_count.plot(kind='bar', color='skyblue')
plt.title('Netflix Viewing Count Per Day')
plt.xlabel('Date')
plt.ylabel('Number of Titles Watched')
plt.tight_layout()

os.makedirs(os.path.dirname(plot_save_path), exist_ok=True)
plt.savefig(plot_save_path)
plt.show()

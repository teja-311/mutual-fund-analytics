import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")

processed_path.mkdir(exist_ok=True)

for file in raw_path.glob("*.csv"):
    df = pd.read_csv(file)

    print(f"Processing {file.name}")
    print(f"Shape before: {df.shape}")

    df = df.drop_duplicates()

    print(f"Shape after : {df.shape}")

    output_file = processed_path / file.name
    df.to_csv(output_file, index=False)

print("All files processed successfully!")
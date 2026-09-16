import kagglehub

path = kagglehub.dataset_download(
    "jonbown/us-2020-traffic-accidents",
    output_dir="./data"
)

print("Dataset downloaded to:", path)
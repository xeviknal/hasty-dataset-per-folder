from collections import defaultdict
import glob
import os
from hasty import Client

API_KEY = "MEEEEC_API_KEY"
client = Client(api_key=API_KEY)
project = client.get_project('projectIDGoESHERE')
print(project)

# List all the files to import
files = []
for ext in ["jpg", "png", "jpeg"]:
    files.append(glob.glob(f"**/*.{ext}"))


# No dataset has been created
datasets = defaultdict()
for upload_file in files:
    folder_name = os.path.dirname(upload_file)
    dataset_id = datasets.get(folder_name)
    if not dataset_id:
        dataset_id = project.create_dataset(folder_name)
        datasets[folder_name] = dataset_id
    print("Uploading:", upload_file)
    try:
        project.upload_from_file(dataset_id, upload_file)
    except Exception as e:
        print(f"Error uploading {upload_file} to {folder_name}/{dataset_id}")
        print(e)


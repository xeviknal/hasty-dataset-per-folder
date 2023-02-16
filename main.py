from hasty import Client
import glob
import os

API_KEY = "MEEEEC_API_KEY"
client = Client(api_key=API_KEY)
project = client.get_project('projectIDGoESHERE')
print(project)


# List all the files to import
files = []
for ext in ["jpg", "png", "jpeg"]:
    files.append(glob.glob(f"**/*.{ext}"))


# No dataset has been created
datasets = []
for upload_file in files:
    print("Uploading:", upload_file)
    project.upload_from_file(dataset_id, upload_file)


for dirs in os.listdir(source_dir):
    upload_dir = os.path.join(source_dir, dirs)
    if os.path.isfile(upload_dir):
        continue
    else:
        dataset_name = dirs
        dataset_id = project.create_dataset(dataset_name)
        print(dataset_name, "dataset created")
        for root, dirs, files in os.walk(source_dir):
            for filename in files:
                upload_file = os.path.join(root, filename)
                if upload_file.endswith(".jpg") or upload_file.endswith(".png"):
                    project.upload_from_file(dataset_id,
                                   upload_file)
                    print("Uploading:", upload_file)

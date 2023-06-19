
import csv
import os
import shutil



# Example usage

print("input drive letter of sd card")
drive=input(":").capitalize()

formats = {
    "n64": (f"{drive}:\\VN64\\roms", f"{drive}:\\VN64\\GUI", f"{drive}:\\VN64\\GUI\\VN64.csv"),
    "z64": (f"{drive}:\\VN64\\roms", f"{drive}:\\VN64\\GUI", f"{drive}:\\VN64\\GUI\\VN64.csv"),
    "nes": (f"{drive}:\\VNES\\roms", f"{drive}:\\VNES\\GUI", f"{drive}:\\VNES\\GUI\\VNES.csv"),
    "gb": (f"{drive}:\\VGBC\\roms", f"{drive}:\\VGBC\\GUI", f"{drive}:\\VGBC\\GUI\\VGBC.csv"),
    "gbc": (f"{drive}:\\VGBC\\roms", f"{drive}:\\VGBC\\GUI", f"{drive}:\\VGBC\\GUI\\VGBC.csv"),
    "gba": (f"{drive}:\\VGBA\\roms", f"{drive}:\\VGBA\\GUI", f"{drive}:\\VGBA\\GUI\\VGBA.csv"),
    "iso": (f"{drive}:\\VPSP\\roms", f"{drive}:\\VPSP\\GUI", f"{drive}:\\VPSP\\GUI\\VPSP.csv")
}

# Define the desired image size
target_size = (410, 358)

# Iterate through all files in the source folder
items=len(os.listdir("roms"))
for i, file_name in enumerate(os.listdir("roms")):
    if len(file_name.split('.'))>1:
        file_ext = file_name.split(".")[-1]
        cfile_name=file_name.split(".")
        cfile_name.pop()
        cfile_name='.'.join(cfile_name)
    else:
        file_ext = file_name.split(".")[-1]
    print(file_ext)
    # Check if the file extension exists in the formats dictionary
    if file_ext in formats:
        roms_folder, image_folder, csv_file = formats[file_ext]

        # Move the file to the destination folder
        source_path = os.path.join("roms", file_name)
        dest_path = os.path.join(roms_folder, file_name)
        shutil.move(source_path, dest_path)

        # Download the image from Google Images

        # Append the new row to the CSV file
        new_csv_row = [cfile_name, cfile_name, "", ""]
        temp_csv_file = csv_file + ".tmp"
        shutil.copyfile(csv_file, temp_csv_file)
        with open(temp_csv_file, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(new_csv_row)
        shutil.move(temp_csv_file, csv_file)
        print(f"done with {file_name.split('.')[0]} {i} out of {items}")

print("Files and images downloaded, sorted, and CSV file updated successfully!")

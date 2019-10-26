import os

file_path = os.path.dirname(os.path.abspath(__file__))
root_path = "/".join(file_path.split("/")[0:-1])
data_path = os.path.join(root_path, "data_csv")
data_preview_path = os.path.join(root_path, "data_preview")


def data_preview():
    for label in os.listdir(data_path):
        create_html(label)


def create_html(label):
    file_out_path = os.path.join(data_preview_path, f"{label}.html")
    if not os.path.exists(data_preview_path):
        os.mkdir(data_preview_path)
    if os.path.exists(file_out_path):
        os.remove(file_out_path)
    with open(os.path.join(data_path, label, f"{label}.csv"), "r") as file_in:
        csv_rows = file_in.readlines()
        for row in csv_rows:
            print(f"<div><img src='{row}'></div>")
            with open(file_out_path, "a") as file_out:
                image_tag = (
                    f"<div style='display:inline-block; margin:10px'><img src='{row}' width=299></div>"
                )
                file_out.write(image_tag)


if __name__ == "__main__":
    data_preview()

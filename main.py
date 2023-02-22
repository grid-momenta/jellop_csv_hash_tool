import flet_core.icons
from flet import *
import os
import pandas as pd
import hashlib


def main(page: Page):
    page.padding = 20
    page.title = "Jellop CSV Hash Tool"

    csv_location = Text("")
    result = Text("")

    def picker1_dialogue(e: FilePickerResultEvent):
        if e.files and len(e.files):
            csv_location.value = e.files[0].path
            csv_location.update()

    my_picker1 = FilePicker(on_result=picker1_dialogue)
    page.overlay.append(my_picker1)
    page.update()

    def process_hashing(e):
        result.value = ""
        result.update()

        if csv_location.value == "":
            result.value = "Please upload csv file."
            result.update()
            return

        df = pd.read_csv(csv_location.value, encoding="ISO-8859-1")
        first_header = list(df.columns)[0]

        # hashing the 'Password' column
        df[first_header] = df[first_header].apply(lambda x: hashlib.sha256(str(x).encode('utf-8')).hexdigest())

        dir_name = os.path.dirname(csv_location.value)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        _, tail = os.path.split(csv_location.value)
        file_name, file_extension = os.path.splitext(tail)

        save_file = f"{dir_name}/{file_name}_hashed{file_extension}"

        # writing the new CSV output
        df.to_csv(save_file, index=False)

        result.value = f"Hash completed. File saved to {save_file}"
        result.update()

        return

    page.add(
        Column([
            Column([
                ElevatedButton(
                    "Pick CSV",
                    icon=flet_core.icons.UPLOAD_FILE,
                    on_click=lambda _: my_picker1.pick_files(allow_multiple=False)
                ),
                csv_location,
                ElevatedButton(
                    "Hash",
                    on_click=process_hashing
                ),
                result,
                Container(
                    content=Column([Text("CG Engineering, Inc 2023")]),
                    margin=Margin(top=300, bottom=0, left=500, right=0)
                ),
            ], expand=True),
        ])
    )


flet.app(target=main)

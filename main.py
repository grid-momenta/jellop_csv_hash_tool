import flet_core.icons
from flet import *
from csv_hasher import hash_csv


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

        save_file = hash_csv(csv_location.value, hash_choice.value)

        result.value = f"Hash completed. File saved to {save_file}"
        result.update()

        return

    hash_choice = RadioGroup(
        content=Column([
            Radio(value="md5", label="MD5"),
            Radio(value="sha1", label="SHA1"),
            Radio(value="sha256", label="SHA256")]
        )
    )

    hash_choice.value = "sha256"

    page.add(
        Column([
            Column([
                ElevatedButton(
                    "Pick CSV",
                    icon=flet_core.icons.UPLOAD_FILE,
                    on_click=lambda _: my_picker1.pick_files(allow_multiple=False)
                ),
                csv_location,
                Text("Select hash method:"),
                hash_choice,
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

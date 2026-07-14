import os


class StorageService:

    def save_document(self, document):

        os.makedirs(
            "output",
            exist_ok=True
        )

        with open(
            "output/result.txt",
            "w",
            encoding="utf-8"
        ) as file:

            for region in document.regions:

                file.write(

                    "=" * 50 + "\n"

                )

                file.write(

                    region.recognized_text

                )

                file.write("\n\n")

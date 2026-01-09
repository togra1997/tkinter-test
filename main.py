import customtkinter as ctk

from wigets.filepick import FilePicker
from wigets.filepick_radio import FilePickAndRadio
from wigets.folderpick import FolderPicker
from wigets.scroll import ScrollableFrame


class App(ctk.CTk):
    def __init__(self) -> None:
        """
        アプリケーションのメインウィンドウを作成する。
        """
        super().__init__()
        self.file_path_dict: dict[str, str] = {}
        self.setup()

    def setup(self) -> None:
        """
        ウィンドウのレイアウトを設定する。
        """
        self.geometry("400x300")
        self.title("File Picker Example")

        scrollable_frame = ScrollableFrame(self)
        scrollable_frame.pack(fill="both", expand=True)

        FilePicker(
            master=scrollable_frame,
            key="file_path",
            label="Select File:",
        ).pack(pady=2, padx=2)

        FilePicker(
            master=scrollable_frame,
            key="file_path1",
            label="Select Another File:",
        ).pack(pady=2, padx=2)

        FilePickAndRadio(
            master=scrollable_frame,
            key="file_path2",
            label="Select CSV File:",
        ).pack(pady=2, padx=2)

        FolderPicker(
            master=scrollable_frame,
            key="folder_path",
            label="Select Folder:",
        ).pack(pady=2, padx=2)

        ctk.CTkButton(
            master=self,
            text="Print File Paths",
            command=lambda: print(self.file_path_dict),
        ).pack(pady=10)

    def set(self, key: str, file_path: str) -> None:
        """
        ファイルパスを辞書に設定する。

        Args:
            key (str): 辞書のキー。
            file_path (str): ファイルパス。
        """
        self.file_path_dict.update({key: file_path})


def main() -> None:
    """
    アプリケーションを起動する。
    """
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

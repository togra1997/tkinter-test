from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk


class FolderPicker(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, key: str, label: str, **kwargs) -> None:
        """
        フォルダ選択用のウィジェット。

        Args:
            master (ctk.CTk): 親ウィジェット。
            key (str): ファイルパスを保存するキー。
            label (str): ラベルのテキスト。
            **kwargs: キーワード引数。
        """
        super().__init__(master, **kwargs)
        self.key: str = key
        self.label_name: str = label
        self.setup()

    def setup(self) -> None:
        """
        ウィジェットのレイアウトを設定する。
        """
        self.label = ctk.CTkLabel(self, text=self.label_name)
        self.label.grid(row=0, column=0, pady=0, padx=5, sticky="w")

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Select a file...",
            width=200,
        )
        self.entry.grid(row=1, column=0, pady=0, padx=5)

        ctk.CTkButton(self, text="Browse", command=self.browse_file).grid(
            row=1, column=1, pady=0, padx=5
        )

    def browse_file(self) -> None:
        """
        フォルダ選択ダイアログを開き、選択したフォルダパスをエントリに表示する。
        """
        folder = filedialog.askdirectory()
        if folder:
            folder_path = Path(folder).name
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, folder_path)
            self.master.set(self.key, folder)

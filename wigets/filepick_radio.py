import tkinter as tk

import customtkinter as ctk
import pandas as pd

from wigets.filepick import FilePicker


class FilePickAndRadio(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, key: str, label: str, **kwargs) -> None:
        """
        ファイル選択とラジオボタンを組み合わせたウィジェット。

        Args:
            master (ctk.CTk): 親ウィジェット。
            key (str): ファイルパスを保存するキー。
            label (str): ラベルのテキスト。
            **kwargs: キーワード引数。
        """
        super().__init__(master, **kwargs)
        self.key: str = key
        self.label_name: str = label
        self.radio_var: tk.StringVar | None = None
        self.setup()

    def setup(self) -> None:
        """
        ウィジェットのレイアウトを設定する。
        """
        FilePicker(
            master=self,
            key=self.key,
            label=self.label_name,
        ).pack(pady=2, padx=2)

    def set(self, key: str, file_path: str) -> None:
        """
        ファイルパスを設定し、ラジオボタンを作成する。

        Args:
            key (str): 設定するキー。
            file_path (str): 設定するファイルパス。
        """
        try:
            # 既存のラジオボタンを削除
            self.clear_radio_buttons()
            self.master.set(key, file_path)
            radio_list = self.make_radio_list(file_path, "b")
            self.radio_var = tk.StringVar(value=radio_list[0])  # デフォルト値を設定
            self.radio_selected()
            for option in radio_list:
                ctk.CTkRadioButton(
                    self,
                    text=option,
                    variable=self.radio_var,
                    value=option,
                    command=self.radio_selected,
                ).pack(anchor="w", padx=10)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to create radio buttons: {e}")

    def make_radio_list(self, filepath: str, col: str) -> list[str]:
        """
        CSVファイルから指定列のユニークな値を取得する。

        Args:
            filepath (str): CSVファイルのパス。
            col (str): 列名。

        Returns:
            list[str]: ユニークな値のリスト。
        """
        df = pd.read_csv(filepath)
        return df[col].unique().tolist()

    def radio_selected(self) -> None:
        """
        ラジオボタンの選択状態を取得し、親ウィジェットに設定する。
        """
        self.master.set("radio", self.radio_var.get())

    def clear_radio_buttons(self) -> None:
        """
        現在のラジオボタンをすべて削除する。
        """
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkRadioButton):
                widget.destroy()

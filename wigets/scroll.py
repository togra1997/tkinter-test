import customtkinter as ctk


class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent: ctk.CTk, *args, **kwargs) -> None:
        """
        スクロール可能なフレームを作成するクラス。

        Args:
            parent (ctk.CTk): 親ウィジェット。
            *args: 可変長引数。
            **kwargs: キーワード引数。
        """
        super().__init__(parent, *args, **kwargs)
        self.parent: ctk.CTk = parent  # Appクラスのインスタンスを保持

    def set(self, key: str, file_path: str) -> None:
        """
        親ウィジェットにキーとファイルパスを設定する。

        Args:
            key (str): 設定するキー。
            file_path (str): 設定するファイルパス。
        """
        self.parent.set(key, file_path)

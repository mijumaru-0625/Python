import tkinter.filedialog as filedialog

# ファイル名の取得
ret = filedialog.askopenfilename(title="COM ファイルを選択",
                                 filetypes= [("COMファイル", "*.d"),
                                             ("任意のファイル", "*.*")])
print(ret, type(ret))

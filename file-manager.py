import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import firebase_admin
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate('APIkey.json')
firebase_admin.initialize_app(cred, {
    "storageBucket": "storage bucket url"
})
db = firestore.client()
bucket = storage.bucket("storage bucket url")

current_path = ''

root = tk.Tk()
root.title("Firebase Storage Explorer")
root.geometry("800x600")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

frame_main = tk.Frame(root)
frame_main.pack(pady=10, fill=tk.BOTH, expand=True)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

listbox_files = tk.Listbox(frame_main, width=50, height=20)
listbox_files.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

def create_folder():
    folder_path = simpledialog.askstring("Create Folder", "Enter the folder path to create:")
    if folder_path:
        if not folder_path.endswith('/'):
            folder_path += '/'
        placeholder_blob = bucket.blob(folder_path + ".placeholder")
        placeholder_blob.upload_from_string('')
        messagebox.showinfo("Success", f"Folder {folder_path} created.")
        refresh_view()

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        destination_blob_name = simpledialog.askstring("Destination", "Enter the destination path in Firebase Storage:")
        if destination_blob_name:
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_filename(file_path)
            messagebox.showinfo("Success", f"File {file_path} uploaded to {destination_blob_name}")
            refresh_view()


def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        destination_blob_name = simpledialog.askstring("Destination", "Enter the destination path in Firebase Storage:")
        
        destination_blob_name = destination_blob_name.replace('\\', '/')
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(file_path)
        
        messagebox.showinfo("Success", f"File {file_path} uploaded to {destination_blob_name}")
        refresh_view()


def download_file():
    selected_file = listbox_files.get(tk.ACTIVE)
    if selected_file:
        destination_file_name = filedialog.asksaveasfilename()
        if destination_file_name:
            blob = bucket.blob(selected_file)
            blob.download_to_filename(destination_file_name)
            messagebox.showinfo("Success", f"File {selected_file} downloaded to {destination_file_name}")


def delete_file():
    selected_file = listbox_files.get(tk.ACTIVE)
    if selected_file:
        blob = bucket.blob(selected_file)
        blob.delete()
        messagebox.showinfo("Success", f"File {selected_file} deleted from Firebase Storage")
        refresh_view()




def refresh_view():
    listbox_files.delete(0, tk.END)
    list_files(current_path)


def list_files(folder_path):
    blobs = bucket.list_blobs(prefix=folder_path)
    folders = set()
    files = []
    
    for blob in blobs:
        name = blob.name[len(folder_path):]
        if '/' in name:
            folder_name = name.split('/')[0] + '/'
            folders.add(folder_name)
        else:
            if not blob.name.endswith('.placeholder'):
                files.append(name)

    for folder in folders:
        listbox_files.insert(tk.END, folder)

    for file in files:
        listbox_files.insert(tk.END, file)            


def open_folder():
    global current_path
    selected_folder = listbox_files.get(tk.ACTIVE)
    if selected_folder.endswith('/'):
        current_path += selected_folder
        refresh_view()


def back():
    global current_path
    if current_path != '':
        path_list = current_path.split('/').pop()
        current_path = '/'.join(path_list)
        refresh_view()


btn_create_folder = tk.Button(frame_top, text="Create Folder", command=create_folder)
btn_create_folder.pack(side=tk.LEFT, padx=10)

btn_upload = tk.Button(frame_top, text="Upload File", command=upload_file)
btn_upload.pack(side=tk.LEFT, padx=10)

btn_download = tk.Button(frame_top, text="Download File", command=download_file)
btn_download.pack(side=tk.LEFT, padx=10)

btn_delete = tk.Button(frame_top, text="Delete File", command=delete_file)
btn_delete.pack(side=tk.LEFT, padx=10)

btn_openfolder = tk.Button(frame_top, text="Open Folder", command=open_folder)
btn_openfolder.pack(side=tk.LEFT, padx=10)

btn_back = tk.Button(frame_top, text="Back", command=back)
btn_back.pack(side=tk.LEFT, padx=10)

btn_refresh = tk.Button(frame_top, text="Refresh", command=refresh_view)
btn_refresh.pack(side=tk.LEFT, padx=10)

refresh_view()
root.mainloop()

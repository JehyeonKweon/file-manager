## Overview

**Project Title**: Cloud File Manager

**Project Description**: Store files in the firebase cloud storage and beable to create folder, upload and download files, and explore the storage

**Project Goals**: Learning cloud database

## Instructions for Build and Use

Steps to build and/or run the software:

1. Form a user interface
2. Get the list of file and folder in the firebase storage and display
3. Create Folder Button - Get users the path to make new folder make placeholder at the path
4. Upload File Button - Get file path to upload and get path in firebase and upload
5. Download File Button - get path of file to download and path to where to put it
6. Delete File Button - get path of file to delete and delete the file
7. Open Folder Button - add the folder's name at current path and refresh the list at the current path
8. Back Button - delete the last folder at current path
9. Refresh Button - Get list from current path and display

Instructions for using the software:

1. Run file-manager.py file
2. Create Folder Button - Click the button then gives the path to create a folder
3. Upload File Button - Click the button and get the path of file to upload and Get the path to store the file in firebase as sting and save it there
4. Download File Button - Select the file to download and click the button then choose file path to download
5. Delete File Button - Select file to delete and click the button
6. Open Folder Button - Select folder and click the button
7. Back Button - Go back to the folder that include the current folder
8. Refresh Button - Click to refresh the list

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python
    * tkinter
    * firebase-admin
* Google firebase

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Youtube](https://www.youtube.com/watch?v=I1eskLk0exg)
* [Stackoverflow](https://stackoverflow.com/questions/73576319/get-list-of-all-folders-in-firebase-storage-using-python)
* [Chat GPT](https://chatgpt.com/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Better UI
* [ ] Path finder UI for firebase storage to get path
* [ ] User Authentication

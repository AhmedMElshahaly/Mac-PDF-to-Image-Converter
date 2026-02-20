# Smart PDF Slicer & Organizer 📄➡️🖼️

A dual-purpose tool designed to automate the process of converting PDF pages into high-quality images and organizing them into dedicated folders. 

This project provides **two versions** depending on your needs: a native macOS application and a cloud-based Google Colab script.

---

## 💻 Option 1: Native Mac App (Offline)
A simple, fast, and standalone macOS application that converts any PDF file into high-quality PNGs. No installation or terminal required!

### How to use the Mac App:
1. Go to the **[Releases](../../releases/latest)** section on the right side of this page.
2. Download the `PDF_Converter.zip` file.
3. Double-click the `.zip` file on your Mac to extract the application.
4. **Important for first-time use on Mac:** - Right-click the extracted App and select **Open**.
   - A warning will appear (since it's not from the App Store), click **Open** again.

---

## ☁️ Option 2: Google Colab Script (Cloud-based)
Don't have a Mac? Want to save the images directly to your Google Drive? Use the cloud version! This script asks for page ranges and neatly organizes your sessions into folders inside your Google Drive.

### How to use the Colab Script:
1. Open the tool using this link: 👉 **[Open in Google Colab](https://colab.research.google.com/drive/1Zmb8oIb_dnjhB6oMsoG_VjHVftT6XI7C)])**
2. Click on **File > Save a copy in Drive** to create your own private workspace.
3. Run the **cell** and follow the interactive prompts to upload your PDF, set the grade name, and slice your sessions.
4. The extracted images will be saved automatically to your Google Drive!

---

## 🛠 Features
- **High-Quality Extraction:** Uses Zoom 2.0 to ensure text and images remain crisp.
- **Smart Organization:** Automatically creates main folders and sub-folders for your sessions.
- **Cross-Platform:** Use the Mac App for local processing or the Colab script from any device (Windows, Linux, tablets).
- **Built with:** Python, PyMuPDF (fitz), PyInstaller, and Google Colab API.

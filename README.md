# Python Folder File Renamer for AI Datasets

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A Python-based tool to automate file renaming for organizing datasets. This bot renames files based on their parent folder's name and appends sequential numbers (e.g., `folder_name_1`, `folder_name_2`), making it perfect for creating structured datasets for AI/ML projects.

---

## Features
- **Automated File Renaming**: Renames files based on their folder names.
- **Sequential Numbering**: Appends numbers (1, 2, 3, ...) for easy sorting and organization.
- **AI Dataset Preparation**: Simplifies dataset creation for machine learning and AI projects.
- **Customizable**: Easily adaptable to different folder structures and naming conventions.

---

## Use Cases
- Preparing image datasets for computer vision tasks.
- Organizing text or audio files for natural language processing (NLP) projects.
- Structuring datasets for training machine learning models.

---

## Example
### Input:
```
images/
  cats/
    cat_image.jpg
    cat_image2.jpg
  dogs/
    dog_image.jpg
```

### Output:
```
images/
  cats/
    cats_1.jpg
    cats_2.jpg
  dogs/
    dogs_1.jpg
```

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-folder-file-renamer-ai-dataset.git
   ```
2. Navigate to the project directory:
   ```bash
   cd python-folder-file-renamer-ai-dataset
   ```
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Place your files in the desired folder structure.
2. Run the script:
   ```bash
   python rename_files.py --directory /path/to/your/folder
   ```
3. Watch as files are automatically renamed and organized!

---

## Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support
If you find this project helpful, consider giving it a ⭐️ on GitHub!

---


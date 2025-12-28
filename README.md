# Personal Notebook Manager 📝

A simple and intuitive command-line application for managing personal notes with tagging and search capabilities.

## 📋 Features

- ✅ **Add notes** with title, content, and tags
- 📚 **List all notes** with formatted display
- 🔍 **Search notes** by keyword (searches in title and content)
- 🏷️ **Filter by tags** to organize your notes
- ✏️ **Edit existing notes** - modify title, content, or tags
- 🗑️ **Delete notes** with confirmation
- 💾 **Automatic saving** - notes are saved to a JSON file
- 📅 **Timestamps** - each note includes creation date and time

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

### Installation

1. Clone or download this repository:
```bash
git clone https://github.com/raneenmandalawe/python-notebook-manager-Raneen.git
cd python-notebook-manager-Raneen
```

2. Make sure you have Python 3 installed:
```bash
python3 --version
```

### Running the Application

Simply run the main Python file:
```bash
python3 notebook_manager.py
```

Or on Windows:
```bash
python notebook_manager.py
```

## 📖 How to Use

When you run the application, you'll see a menu with the following options:
```
==================================================
       Personal Notebook Manager
==================================================
(1) Add note
(2) List notes
(3) Search notes
(4) Filter by tag
(5) Edit note
(6) Delete note
(0) Exit
==================================================
```

### 1. Adding a Note

- Select option `1`
- Enter a title for your note
- Enter the content (press Enter twice when finished)
- Add tags separated by commas (e.g., `work, important, todo`)
- The note will be saved automatically with the current date and time

### 2. Listing All Notes

- Select option `2`
- View all your notes with their titles, dates, tags, and content preview

### 3. Searching Notes

- Select option `3`
- Enter a keyword to search
- The app will find all notes containing that keyword in the title or content

### 4. Filtering by Tag

- Select option `4`
- See all available tags
- Enter a tag to filter
- View all notes with that specific tag

### 5. Editing a Note

- Select option `5`
- Choose the note number you want to edit
- Update the title, content, or tags
- Press Enter to keep the current value for any field

### 6. Deleting a Note

- Select option `6`
- Choose the note number you want to delete
- Confirm the deletion
- The note will be permanently removed

### 7. Exiting

- Select option `0`
- All notes will be saved automatically before exiting

## 📁 File Structure
```
python-notebook-manager/
│
├── notebook_manager.py    # Main application file
├── README.md             # This file
└── notes.json           # Auto-generated file storing your notes
```

## 💾 Data Storage

Notes are stored in a file called `notes.json` in the same directory as the application. The file is automatically created when you add your first note.

### Example notes.json format:
```json
[
  {
    "title": "Shopping List",
    "content": "Milk, Bread, Eggs, Cheese",
    "tags": ["home", "shopping"],
    "date": "2025-11-27 14:30:00"
  },
  {
    "title": "Project Ideas",
    "content": "Build a personal website\nLearn machine learning\nCreate a mobile app",
    "tags": ["work", "ideas"],
    "date": "2025-11-28 09:15:00"
  }
]
```

## 🎯 Project Requirements Met

This project fulfills all the required features:

- ✅ Functions for each action
- ✅ Lists and dictionaries for data storage
- ✅ Input/output using `input()` and `print()`
- ✅ File handling with JSON
- ✅ Main loop with menu
- ✅ Clear formatting
- ✅ JSON file storage
- ✅ Clean, readable code with comments
- ✅ Graceful error handling
- ✅ Automatic timestamp using `datetime`

## 🎨 Code Quality

The code includes:

- **Clear function names** that describe their purpose
- **Type hints** for better code documentation
- **Comments** explaining key sections
- **Error handling** for file operations and user input
- **Input validation** to prevent crashes
- **No code repetition** - each function has a specific purpose

## 🔧 Troubleshooting

### Problem: "Permission denied" error
**Solution:** Make sure you have write permissions in the directory where you're running the application.

### Problem: Notes not saving
**Solution:** Check if there's enough disk space and that you have write permissions.

### Problem: "Module not found" error
**Solution:** This application only uses Python's standard library, so make sure you're using Python 3.6 or higher.

## 🚀 Future Improvements (Optional)

Ideas for extending this project:

- Sort notes by date, title, or tags
- Export notes to PDF or text file
- Add password protection
- Colorized output for better readability
- Cloud backup integration
- Search with regular expressions
- Note categories or folders

## 👩‍💻 Author

Raneen Mandalawe

## 📝 License

This project is created for educational purposes.

## 🙏 Acknowledgments

- Thanks to Reichan for the assignment and guidance
- YouTube Python tutorial: https://www.youtube.com/watch?v=K5KVEU3aaeQ

---

**Enjoy organizing your notes! 📝✨**

If you have any questions or suggestions, feel free to reach out!

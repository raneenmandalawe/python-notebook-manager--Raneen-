#!/usr/bin/env python3
"""
Personal Notebook Manager
A command-line application for managing personal notes with tags and search functionality.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


# File path for storing notes
NOTES_FILE = "notes.json"


def load_notes() -> List[Dict]:
    """
    Load notes from the JSON file.
    Returns an empty list if the file doesn't exist or is invalid.
    """
    if not os.path.exists(NOTES_FILE):
        return []
    
    try:
        with open(NOTES_FILE, 'r', encoding='utf-8') as file:
            notes = json.load(file)
            return notes if isinstance(notes, list) else []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not load notes file: {e}")
        return []


def save_notes(notes: List[Dict]) -> bool:
    """
    Save notes to the JSON file.
    Returns True if successful, False otherwise.
    """
    try:
        with open(NOTES_FILE, 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"Error: Could not save notes: {e}")
        return False


def add_note(notes: List[Dict]) -> None:
    """
    Add a new note to the collection.
    Prompts the user for title, content, and tags.
    """
    print("\n=== Add New Note ===")
    
    # Get title
    while True:
        title = input("Enter note title: ").strip()
        if title:
            break
        print("Title cannot be empty. Please try again.")
    
    # Get content
    print("Enter note content (press Enter twice when done):")
    content_lines = []
    empty_count = 0
    while empty_count < 1:
        line = input()
        if line:
            content_lines.append(line)
            empty_count = 0
        else:
            empty_count += 1
    content = "\n".join(content_lines).strip()
    
    # Get tags
    tags_input = input("Enter tags (comma-separated, e.g. 'work,important'): ").strip()
    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
    
    # Create note with current date
    note = {
        "title": title,
        "content": content,
        "tags": tags,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    notes.append(note)
    
    if save_notes(notes):
        print(f"✓ Note '{title}' added successfully!")
    else:
        print("✗ Failed to save note.")


def list_notes(notes: List[Dict]) -> None:
    """
    Display all notes in a formatted manner.
    """
    if not notes:
        print("\nNo notes found. Add your first note!")
        return
    
    print(f"\n=== All Notes ({len(notes)} total) ===")
    for i, note in enumerate(notes, 1):
        print(f"\n[{i}] {note['title']}")
        print(f"    Date: {note.get('date', 'N/A')}")
        print(f"    Tags: {', '.join(note['tags']) if note['tags'] else 'No tags'}")
        
        # Show first 100 characters of content
        content = note['content']
        if len(content) > 100:
            print(f"    Content: {content[:100]}...")
        else:
            print(f"    Content: {content}")


def search_notes(notes: List[Dict]) -> None:
    """
    Search notes by keyword in title or content.
    """
    keyword = input("\nEnter search keyword: ").strip().lower()
    
    if not keyword:
        print("Search keyword cannot be empty.")
        return
    
    results = [
        note for note in notes
        if keyword in note['title'].lower() or keyword in note['content'].lower()
    ]
    
    if not results:
        print(f"\nNo notes found containing '{keyword}'")
        return
    
    print(f"\n=== Search Results ({len(results)} found) ===")
    for i, note in enumerate(results, 1):
        print(f"\n[{i}] {note['title']}")
        print(f"    Date: {note.get('date', 'N/A')}")
        print(f"    Tags: {', '.join(note['tags']) if note['tags'] else 'No tags'}")
        print(f"    Content: {note['content'][:100]}{'...' if len(note['content']) > 100 else ''}")


def filter_by_tag(notes: List[Dict]) -> None:
    """
    Filter and display notes by a specific tag.
    """
    # Show all available tags
    all_tags = set()
    for note in notes:
        all_tags.update(note['tags'])
    
    if not all_tags:
        print("\nNo tags found in any notes.")
        return
    
    print(f"\nAvailable tags: {', '.join(sorted(all_tags))}")
    tag = input("Enter tag to filter by: ").strip().lower()
    
    if not tag:
        print("Tag cannot be empty.")
        return
    
    results = [note for note in notes if tag in [t.lower() for t in note['tags']]]
    
    if not results:
        print(f"\nNo notes found with tag '{tag}'")
        return
    
    print(f"\n=== Notes with tag '{tag}' ({len(results)} found) ===")
    for i, note in enumerate(results, 1):
        print(f"\n[{i}] {note['title']}")
        print(f"    Date: {note.get('date', 'N/A')}")
        print(f"    Tags: {', '.join(note['tags'])}")
        print(f"    Content: {note['content'][:100]}{'...' if len(note['content']) > 100 else ''}")


def edit_note(notes: List[Dict]) -> None:
    """
    Edit an existing note.
    """
    if not notes:
        print("\nNo notes available to edit.")
        return
    
    list_notes(notes)
    
    try:
        choice = int(input("\nEnter note number to edit (0 to cancel): "))
        if choice == 0:
            return
        if choice < 1 or choice > len(notes):
            print("Invalid note number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    note = notes[choice - 1]
    
    print(f"\nEditing: {note['title']}")
    print("(Press Enter to keep current value)")
    
    # Edit title
    new_title = input(f"Title [{note['title']}]: ").strip()
    if new_title:
        note['title'] = new_title
    
    # Edit content
    print(f"Current content: {note['content']}")
    edit_content = input("Edit content? (y/n): ").strip().lower()
    if edit_content == 'y':
        print("Enter new content (press Enter twice when done):")
        content_lines = []
        empty_count = 0
        while empty_count < 1:
            line = input()
            if line:
                content_lines.append(line)
                empty_count = 0
            else:
                empty_count += 1
        new_content = "\n".join(content_lines).strip()
        if new_content:
            note['content'] = new_content
    
    # Edit tags
    current_tags = ', '.join(note['tags'])
    new_tags = input(f"Tags [{current_tags}]: ").strip()
    if new_tags:
        note['tags'] = [tag.strip() for tag in new_tags.split(',') if tag.strip()]
    
    if save_notes(notes):
        print("✓ Note updated successfully!")
    else:
        print("✗ Failed to save changes.")


def delete_note(notes: List[Dict]) -> None:
    """
    Delete a note from the collection.
    """
    if not notes:
        print("\nNo notes available to delete.")
        return
    
    list_notes(notes)
    
    try:
        choice = int(input("\nEnter note number to delete (0 to cancel): "))
        if choice == 0:
            return
        if choice < 1 or choice > len(notes):
            print("Invalid note number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    note_title = notes[choice - 1]['title']
    confirm = input(f"Are you sure you want to delete '{note_title}'? (y/n): ").strip().lower()
    
    if confirm == 'y':
        notes.pop(choice - 1)
        if save_notes(notes):
            print(f"✓ Note '{note_title}' deleted successfully!")
        else:
            print("✗ Failed to save changes.")
    else:
        print("Deletion cancelled.")


def display_menu() -> None:
    """
    Display the main menu.
    """
    print("\n" + "="*50)
    print("       Personal Notebook Manager")
    print("="*50)
    print("(1) Add note")
    print("(2) List notes")
    print("(3) Search notes")
    print("(4) Filter by tag")
    print("(5) Edit note")
    print("(6) Delete note")
    print("(0) Exit")
    print("="*50)


def main():
    """
    Main application loop.
    """
    print("Welcome to Personal Notebook Manager!")
    print("Loading notes...")
    
    notes = load_notes()
    print(f"Loaded {len(notes)} note(s).")
    
    while True:
        display_menu()
        
        choice = input("\nSelect an option: ").strip()
        
        if choice == '1':
            add_note(notes)
        elif choice == '2':
            list_notes(notes)
        elif choice == '3':
            search_notes(notes)
        elif choice == '4':
            filter_by_tag(notes)
        elif choice == '5':
            edit_note(notes)
        elif choice == '6':
            delete_note(notes)
        elif choice == '0':
            print("\nSaving and exiting...")
            save_notes(notes)
            print("Goodbye! 👋")
            break
        else:
            print("\n✗ Invalid option. Please try again.")


if __name__ == "__main__":
    main()

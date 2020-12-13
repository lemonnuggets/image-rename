# image-rename
  Recursively renames files in folders and subfolders in the format {yyyy-mm-dd hrs-min-sec}.extension.
  
  Files without date-time info are left untouched.
  
# Prerequisites
  ## Pillow
  
  [Installation Guide](https://pillow.readthedocs.io/en/latest/installation.html)
  
  ## Maya

  [Installation Guide](https://github.com/timofurrer/maya#-installing-maya)

# Usage
  `./img_rename.py path/to/folder1 ./relative/path/to/folder2`

# TODO
  - [ ] Allow a -r flag to make recursive nature optional
  
  - [ ] An option to make a copy of the file instead of renaming it
  
  - [ ] Get metadata from windows instead of image file (or give user the choice)

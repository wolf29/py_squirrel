py_squirrel
===========

Simple python script to break out data from sql dumps

SQL dumps from working databases can be so big that you cannot pull specific raw data by just opening a text editor.  This is how I want to do it, and so these big sql files have to be breakable into smaller sql files maybe into table level.
This script will basically turn a sql dump into a filesystem, with schema-level being the sub-directories and each table being a sql text file.

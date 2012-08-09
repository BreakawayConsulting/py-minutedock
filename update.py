"""
An example script that is used to update entries. This adds
a project code 'new_project' to any entries for a given 'customer'
that doesn't have a project set.
"""
from md import MinuteDock
import datetime

def update(md):
    entries = md.entries_search(date_range = (datetime.date(2012, 7, 1), datetime.date(2012, 8, 30)),
                                user_logins = ['user1', 'user2', 'user3'],
                                contacts = ['customer'],
                                projects = [],
                                )

    for e in entries:
        e.change_project('new_project')
        e.update()

def main():
    md = MinuteDock()
    update(md)

if __name__ == "__main__":
    main()

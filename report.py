"""
An example script that uses the MinuteDock API to create
a custom report.
"""
import argparse
import datetime
from md import MinuteDock

def mysort(sortable, *attrs):
    def mykey(x):
        return tuple([getattr(x, attr) for attr in attrs])

    sortable.sort(key=mykey)

def mygroup(iterable, attr):
    groups = {}
    for i in iterable:
        grouping = getattr(i, attr)
        groups[grouping] = groups.get(grouping, []) + [i]
    return groups.values()

def report(md):
    entries = md.entries_search(date_range = (datetime.date(2012, 7, 1), datetime.date(2012, 7, 31)),
                                contacts = [],
                                projects = ['SOMEPROJECT'],
                                )

    for e in  [e for e in entries if e.timer_active]:
        print(e.raw)

    entries = [e for e in entries if not e.timer_active]
    mysort(entries, 'user_id', 'date')
    groups = mygroup(entries, 'user_id')

    total_time = 0
    for g in groups:
        user = md.users_by_id[g[0].user_id]
        print("%s %s" % (user.first_name, user.last_name))
        time = 0
        for e in g:
            print("%-20s %s %-5.2f %s" % (e.date.strftime("%d/%m/%Y"), e.project_id, e.duration / 3600.0, e.description))
            time += e.duration
        print("   SUB TIME", time/3600.0)
        total_time += time
    print("%-20s %-5.2f" % ("Total time", total_time / 3600.0))

def main():
    md = MinuteDock()
    report(md)

if __name__ == "__main__":
    main()

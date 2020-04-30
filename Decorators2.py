import operator
from operator import itemgetter

def person_lister(f):
    def inner(people):
        
        getcount = itemgetter(2)
        m=sorted(people,key=getcount)
        return map(f,m)
        # complete the function
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
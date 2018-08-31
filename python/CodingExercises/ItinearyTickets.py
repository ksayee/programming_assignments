# Given a list of tickets, find itinerary in order using the given list.
# Example:
# Input:
# "Chennai" -> "Banglore"
# "Bombay" -> "Delhi"
# "Goa"    -> "Chennai"
# "Delhi"  -> "Goa"
# Output:
# Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore,

def ItinearyTickets(ary):

    dict={}

    for l in ary:

        key=l[0]
        val=l[1]

        if key not in dict.keys():
            dict[key]=val

    rev_dict={}

    for key,val in dict.items():

        if val not in rev_dict.keys():
            rev_dict[val]=key

    start=''

    for key,val in dict.items():

        if key not in rev_dict.keys():
            start=key
            break

    fnl_lst=[]
    to=dict[start]
    tup=(start,to)
    fnl_lst.append(tup)

    start=to
    while True:

        if to in dict.keys():
            tup=[to,dict[to]]
            fnl_lst.append(tup)
            to=dict[to]
        else:
            break

    return fnl_lst

def main():

    ary=[("Chennai","Banglore"),("Bombay","Delhi"),("Goa","Chennai"),("Delhi","Goa")]
    print(ItinearyTickets(ary))

if __name__=='__main__':
    main()
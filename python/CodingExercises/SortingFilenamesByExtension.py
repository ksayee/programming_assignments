# Sorting a list of files names first by extension and then by name of the file

def SortingFilenamesByExtension(lst):

    fnl_lst=sorted(lst,key=lambda x:(x.split('.')[1],x.split('.')[0]))
    return fnl_lst

def main():
    
    lst=['file10.csv','file2.com','file6.yml','file7.cfg','file5.abc','file9.zzz','file1.yxy','file4.txy','file8.trw','file3.mvw','file0.abc']
    print(SortingFilenamesByExtension(lst))

if __name__=='__main__':
    main()
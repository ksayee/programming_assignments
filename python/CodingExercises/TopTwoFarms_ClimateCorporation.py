# Given a list of farms with attributes “name”, “crop”, and “size”, return a list of the
#  top two farms by size for each crop.

# Example input:
# "adams", "corn", 100
# "adair", "soybeans", 50
# "benton", "soybeans", 90
# "boone", "corn", 75
# "carroll", "wheat", 200
# "creation", "corn", 90
# "dansplot" , "soybeans", 55
# "edgars", "soybeans", 95
# "everlast", "corn", 70
# "greenacres", "wheat", 205

def TopTwoFarms(crop_lst):

    dict = {}

    for element in crop_lst:
        farm = element[0]
        crop = element[1]
        crop_size = element[2]

        if crop in dict.keys():
            dict[crop].append((farm,crop_size))
        else:
            dict[crop]=[]
            dict[crop].append((farm,crop_size))

    for crop,val in dict.items():
        top_two = sorted(val,key=lambda x:x[1],reverse=True)[:2]
        print("Top 2 for {Crop} is: {val}".format(Crop=crop,val=str(top_two)))

def main():

    crop_lst = [["adams", "corn", 100],["adair", "soybeans", 50],
[ "benton", "soybeans", 90],
[ "boone", "corn", 75],
[ "carroll", "wheat", 200],
[ "creation", "corn", 90],
[ "dansplot" , "soybeans", 55],
[ "edgars", "soybeans", 95],
[ "everlast", "corn", 70],
[ "greenacres", "wheat", 205]]
    TopTwoFarms(crop_lst)

if __name__=='__main__':
    main()
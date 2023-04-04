import pickle

mylist = [1,2,3,4,5,'hack','the','world']

mylist_file = open('picklerick', 'wb')
pickle.dump(mylist, mylist_file)

mylist_file.close()

open_file = open("picklerick",'rb')

pickledrick = pickle.load(open_file)

print(pickledrick)
from AR.DATABASE import *

a = SqLite("data.db")



try:
    a.Add('''CREATE TABLE Accounts (
        name text,
        address text,
        phone text,
        email text,
        type text,
        bal integer,
        pf text
    )''')
except:
    print("alredy Table Accounts is Exist")


try:
    a.Add('''CREATE TABLE BuyVouchar (
        bid integer PRIMARY KEY,
        challan_sc text,
        date text,
        field text,
        carno text,
        challan text,
        note text
    )''')
except:
    print("alredy Table BuyVouchar is Exist")

try:
    a.Add('''CREATE TABLE  BuyProduct(
        bpid integer PRIMARY KEY,
        quality text,
        pcs integer,
        rate integer,
        bid text
    )''')
except:
    print("alredy Table BuyProduct is Exist")


from final import *
import conn

def choice():
    
    print "1.Create"
    print "2.Delete"
    print "3.Select"
    print "4.Insert"
    print "5.Update"
    user = raw_input("What you want?")
    if user == "1":
        create_table()
        choice()
    elif user == "2":
        delete()
        choice()
    elif user == "3":
        select()
        choice()
    elif user == "4":
        insert()
        choice()
    elif user == "5":
        update()
        choice()    

choice()
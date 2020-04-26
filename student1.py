
nested_dictionary={"alex":{"math":"50","physics":"98","chemistry":"69","biology":"78","social":"89"},
"martin":{"math":"45","physics":"99","chemistry":"100","biology":"89","social":"88"},
"trisha":{"math":"66","physics":"68","chemistry":"70","biology":"71","social":"68"}}
name=input("enter name:")
sub=input("enter subject:")
def get_all_values(nested_dictionary):
    for nam, subject in nested_dictionary.items():
        if "alex" in nested_dictionary :
        	for marks in subject:
        		print(marks +':',subject[marks])

            


get_all_values(nested_dictionary)










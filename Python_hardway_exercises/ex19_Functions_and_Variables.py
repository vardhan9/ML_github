def cheese_and_crackers(cheese_count,no_of_cracker_boxes):
	print"you had %d cheeses"%cheese_count
	print"you had %d boxes of crackers"%no_of_cracker_boxes
	print"man thats enough for a party"
	print "get a blanket.\n"


print "we can just give function number directly"
cheese_and_crackers(20,30)

print "we can use variables from our script"
amount_of_cheese= 50
amount_of_boxes=60
cheese_and_crackers(amount_of_cheese,amount_of_boxes)

print"we can do math inside"
cheese_and_crackers(50+50,100+100)


print"we can combine both : variables and math"
cheese_and_crackers(amount_of_cheese+500,amount_of_boxes+200)
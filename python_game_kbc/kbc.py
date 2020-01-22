question = ["(1)snehalaya kahape hai?","(2)snehalaya ke project manager kon hai?","(3)snehalaya mai kitne student hai?","(4)snehalaya ke sachiv kon hai?","(5)snehalaya mai 12th class mai kitne student hai?","(6)snehalaya ke student ka brithday konse month mai aata hai?","(7)snehalaya ke kitne project hai?","(8)snehalaya konse year mai sthyapan huaa hai?","(9)snehalaya mai school hai kay?","(10)Navgurukul kaha pe hai?","(11)Navgurukul mai kitni grils hai?","(12)Navgurukul mai kay shikhate hai?","(13)Navgurukul ke co-founder kon hai?","(14)Navgurukul ke buliding ka colour konsa hai?","(15)Navgurukul ke kitne campes hai?"]

first_options = ["(1)Ahmednagar","(1)sanjay gujale","(1)450","(1)vishnu ambekar","(1)10","(1)may","(1)13","(1)2000","(1)hai","(1)mumbai","(1)50","(1)kuch bhi nahi","(1)Abhishekh Gupta","(1)read","(1)1"]
second_options = ["(2)pune","(2)vaijnath lohar","(2)240","(2)sachin dormule","(2)20","(2)Auguest","(2)12","(2)2004","(2)nahi","(2)bangoar","(2)60","(2)clivil enggniarig","(2)Amar shinha","(2)orange","(2)3"]
third_options = ["(3)mumbai","(3)sunil more","(3)350","(3)nick","(3)30","(3)jun","(3)14","(3)2008","(3)tha","(3)pune","(3)56","(3)college enggniarig","(3)rishabh varma","(3)black","(3)2"]
forth_options = ["(4)delhi","(4)joes","(4)300","(4)rajiv gujar","(4)40","(4)jully","(4)23","(4)1989","(4)shayd","(4)Ahmednagar","(4)70","(4)software enggniarig","(4)koi bhi nahi","(4)yellow","(4)nahi hai"]

all_option = ["first_option","second_option","third_option","forth_options"]
ans_key = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3]
prize = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000]

question.append("(16)snehalaya kay hai?")# Add karne ke liye use kiya hai.
print question

first_options.append("(1)school")# Add karne ke liye use kiya hai.
print first_options

second_options.append("(2)Rudha ashram")# Add karne ke liye use kiya hai.
print second_options

third_options.append("(3)orfan NGO")# Add karne ke liye use kiya hai.
print third_options

forth_options.append("(4)NGO")# Add karne ke liye use kiya hai.
print forth_options

ans_key.append(4)# Add karne ke liye use kiya hai.
print ans_key3

answer_list = []#ek empty list li hai user jo input dalega vo input iss list mai store hoga.

i = len(question)# list ke eleament ko count karne ke liye use kiya hai.
print i

options2 = [] #ek khali variable mai ek value store karne ke liye use kiya hai.
options2.append("vaijnath lohar")
print options2

if "vaijnath lohar" in third_options:#ek options mai vo value hai ya nahi hai dekhane ke liye use kiya hai.
	print "hai"
else:
	print "nahi hai"

b = 0
i = 0
a = 0
n = len(question)
while (i<len(question)):
	print question[i]
	print len(question[i])#har ek question ki lenath nikal ne ke liye use kiya hai.
	print first_options[i]
	print second_options[i]
	print third_options[i]
	print forth_options[i]
	user_input =int(raw_input("enter your answer"))
	if ans_key [i] == user_input:
		print "your answer right hai"
		print prize[i]
	else:
		print "try again"
		break
	
	answer_list.append(user_input)#jo bhi input datega user vo input jo empty list hai useme store hone ke liye ye use kiya hai.
	print answer_list
	
	while a < len(prize):
		if a == 4:
			print "congrats! Aapka frist padaav pura hogaya hai." 	
		if a == 9:
			print "congrats! Aapka Doosra padaav pura hogaya hai."
		if a == 15:
			print "Congrats! Aap ek crore rupye jeet gaye aap ja sakte ho."		
		if a == i:
			print "prize",(prize[a])
			b = (prize[a]+b)	
			a = a +1
			break
	i = i + 1
print "total prize=",b 	
#question.pop()#list mai jo element hai usemese last ka element ko hatanekeliye use kiya hai.
#print question	
#dot format on strings
name = 'dom'
f'hello, {name}!'

#movie rental
little_mermaid = 3
brother_bear = 5
hercules = 1
rental_list = [little_mermaid, brother_bear, hercules]
price = sum(rental_list) *3

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a 
# different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much 
# will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 
# 4 hours for Amazon.
pay = {6:400, 10:350, 4:380}
total = 0
for i in pay:
     total = i*pay[i]
print total
















username = 'codeup'
password = 'notastrongpassword'


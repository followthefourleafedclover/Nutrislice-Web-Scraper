# Nutrislice
A simple script that sends the Glastongury High School Lunch Menu today and tomorrow. Made from scratch.

* Args
 - Program does not take any arguments. 

* Out 
- Program displays status code of GET request to Nutrislice API, and sends an email to the intended recepient of the content of today's lunch menu at Glastonbury High School as well as tomorrow's lunch menu as well. 

* Resources
- Only used past projects to understand smtplib. 

# API
https://glastonburyus.nutrislice.com/menu/api/weeks/school/glastonbury-high/menu-type/lunch/2022/08/29/ 

This is a read-only API, which means only GET, HEAD, and OPTIONS requests are accepted.

# Future Updates & Additional Comments
In the future, I will update the program such that it also displays nutritional data. I would also like to turn this script into a fully fleshed-out application that allows students and parents alike to have a more convenient way of accessing their schools lunch menu. 

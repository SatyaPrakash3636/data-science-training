#! /usr/bin/env python3

# Form a new string by taking 1st/3rd/6th/7th fields from the following line with ‘|’ as separator.
# Icrisat: x: 1001:51: global crop research institute: /home/icrisat: /bin/bash

input_date = "Icrisat: x: 1001:51: global crop research institute: /home/icrisat: /bin/bash"

# Converting input data to list
sliced_list = input_date.split(":")[::2]

# Removing extra spaces
final_list = [ i.strip() for i in sliced_list ]

# Joining the fields with '|' symbol
final_string = "|".join(final_list)

# Printing output list
print(final_string)
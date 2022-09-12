# Using logical operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")   
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
     print(county)
for county in counties:
    print (county)
# Using range to obtain county names    
for i in range(len(counties)):
    print(counties[i])
# Working with dictionaries    
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# Keys:
for county in counties_dict.keys():
    print (county)
# Values    
for voters in counties_dict.values():
    print (voters)
# To obtain the value of a specific key    
print (counties_dict['Arapahoe'])
# For key-value pairs
### for county, voters in counties_dict:
###    print(county, voters)
for county, voters in counties_dict.items():
    print (county, " has " ,voters, "registered voters") 
# Working with dictionary lists:
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
# Printing the list of dictionary keys and values
for county_dict in voting_data:
    print(county_dict)
# Using range to print county names
for i in range(len(voting_data)):
      print(voting_data[i]['county'])
# Printing the matching keys and values in the dictionary list
for county_dict in voting_data:  
     print(county_dict.values())
# Printing values alone     
for county_dict in voting_data:
     print(county_dict['registered_voters'])
# Printing statements with f strings
for county, voters in counties_dict.items():
    print(f"{county} county has {voters :,} registered voters.")
# Print multiple strings or lines to the screen  
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
# Format Floating-Point Decimals
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
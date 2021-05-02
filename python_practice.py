#print("Hello World")
#counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[1] == "Denver":
#    print(counties[1])


#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
#    print("Turn on the AC.")
#else:
#    print("Open the windows.")

#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not in the list of counties.")

#x = 0
#while x <= 5:
#    print(x)
#    x += 1

#counties = ["Arapahoe", "Denver", "Jefferson"]
#for county in counties:
#    print(county)

county_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
#    print(county)
#for county in counties_dict.keys():
#    print(county)
#for voters in counties_dict.values():
#    print(voters)
#for county, voters in counties_dict.items():
#    print(county, voters)

#for county, voters in counties_dict.items():
#    print(county)
#    print(" county has")
#    print(voters)
#    print(" registered voters.")

for county, voters in county_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in county_dict.items():
    print(f"{county} county has {voters} registered voters.")


#counties_dict = [{"county": "Arapahoe", "voters": 422829}, {"county": "Denver", "voters": 463353}, {"county": "Jefferson", "voters": 432438}]
#for county, voters in counties_dict.items():
#    print(county, voters)

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#    print(county_dict)

#for i in range(len(voting_data)):
#    print(voting_data[i])

#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)

#for county_dict in voting_data:
#    print(county_dict['registered_voters'])

#Multi line
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

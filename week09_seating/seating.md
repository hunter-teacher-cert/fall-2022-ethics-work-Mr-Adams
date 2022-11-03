# Airplane Seating Algorithm
## Considerations
* Families with minors together
* Handicap Accessibility / Disability accomodation
* Overbooking tickets
* People cheating the system to get cheaper seats but with good seats or seats with a group
* Privacy
* Note: This is tough because it is for cheaper tickets that are randomnly assigned.  It is likely that people may be dishonest to get better seats with their party or that it is not necessarily fair to give families priority when they buy the budget tickets.  I struggle with that question, but will account for it if there is a party of two-- An adult and one minor under 5, but if they are larger party then they must buy tickets that will let you pick your seat. My algorithm will prioritize families with minor 5-10 by seating them as close as possible in the plane, but with no garauntee to proximity.

##  Algorithm Plan
* Once a person has selected the budget choice, they understand they do not get a seat selection, the user will answer if they are traveling with any minors under the age of 5 or between the age of 6 and 10.
* Based on their selection the program will present them with the explanation for the ticket they are purchasing
  * Minor Under 5-Will need to verify their child's DOB and possibly submit some other type of age verification (I would like to have the age verified as they will be placed in an aisle and middle seat right after this step)
    *  The verification may be a bit intrusive but will make sure that this person is not just taking advantage of something to get a better seat.  I think there is tech now that can be used to verify each document automically.
  * 6-10 must acknowledge they undertand they will be sat as close to the minor as possible and there is not garauntee of closeness but they will have some priority in the random process
* After they have entered their information the program will ask them if they have a physical disability that requires special accomodation.
  * They will let the program know their special accomodation
  * before they can proceed the program will check if there are any available seats that fit their required accomodation
  * If yes, the computer will place that person there, but they will have to verify their disability with either a doctor's note or their handicap pass
    * The verification may be a bit intrusive but will make sure that this person is not just taking advantage of something to get a better seat.  I think there is tech now that can be used to verify each document automically.
  * If no, the program will prompt them with other flight options that have their required accomodation. 
* 24hr before the flight people will be assigned randomly to their seats.  Any left over seats may be sold at the budget price or seat selection price and will fill the remaining seats until non remain.
* The program will seat any adults and associated minors 6-10 first with priority placed on younger kids to be close and then rest of tickets will be sat

## Other Concerns
* The verification may be a bit intrusive but will make sure that this person is not just taking advantage of something to get a better seat.  I think there is tech now that can be used to verify each document automically.
* If they can verify then there is still the issue of equity that some people will get awarded, but it is only going to one adult and a small minor or a person that is less abled and should not be discriminated against.
* No one will get a seat selection, but some poeple will be assigned to the first available seat from the back forward that accomodates them.

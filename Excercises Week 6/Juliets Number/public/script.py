#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ['0779266313', '0789266313', '0792566313', '0792646313', '0792663113', '0792663130','0792663213', '0792663313', '0792696313', '0796266313']
#'', '', '', '', '', '0792663130', 
#'', '', '', ''
# Confirmed Numbers: 079266313


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    # This function accepts a string n for juliets number where one digit is missing.
    # and should return a list of all whatsapp numbers that might belong to juliet 
    possible_nrs_for_juliet = []
    n_without_07 = str(n[2:])
    all_possible_nrs = []
    print(n_without_07)
    print(n_without_07[:6+1] + "0" + n_without_07[6+1:])

    #Add numbers 0-9 up until last digit and add to possible_nrs_for_juliet
    for idx, number in enumerate(n_without_07):
        #Add number up until last digit
        for i in range(0,10):
            possible_nr = n_without_07[:idx] + str(i) + n_without_07[idx:]
            all_possible_nrs.append(possible_nr)
    #Add number in last digit
    for i in range(0,10):
        possible_nr = n_without_07[:] + str(i)
        all_possible_nrs.append(possible_nr)
    
    all_possible_nrs = list(set(all_possible_nrs))
    
    #Check if list of possible numbers is in whatsapp numbers
    for nrs in all_possible_nrs:
        for registered_nrs in wa_nrs:
            #print(registered_nrs)
            if nrs == registered_nrs[2:]:
                #print(nrs)
                possible_nrs_for_juliet.append("07" + nrs)

    return possible_nrs_for_juliet

    # Don't forget to return your result

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("079266313"))

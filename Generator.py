
'''
Utilities classes/functions
''' 

class Time_Conversion():
    def hr_min_sec2sec(input):  # String in format HH:MM:SS
        pre_parsing = input.split(":")
        tot_len_hrs = int((pre_parsing[0]))   # assign variables
        tot_len_min = int((pre_parsing[1]))
        tot_len_sec = int((pre_parsing[2]))

        tot_len_hrs_norm = tot_len_hrs * (60 ** 2)
        tot_len_min_norm = tot_len_min * 60
        tot_len_sec_norm = tot_len_sec  # For my own sake

        Total_lenght_Seconds = tot_len_hrs_norm + tot_len_min_norm + tot_len_sec_norm
        return Total_lenght_Seconds

    def sec2hr_min_sec(input):
        hrs = int(input / (60**2))
        if hrs == 0:
            min = int(input / (60))
        else:
            min = int((input - hrs*(60**2)) / (60))
        sec = input - (hrs*(60**2) + (min*60))
        out_string = f"{hrs}:{min}:{sec}"
        return out_string

def true_false_input_handler(input):
    answer = int(input)
    if answer == 1:
        answer = True
    elif answer == 0:
        answer = False
    else:
        print("Error, entered value is neither 0 or 1")
    return answer


'''
Primary processing (Level 1) Global attributes
''' 

# Main methods
def Set_Total_Lenght():
    Total_lenght = input("Set Total Lenght(in HH:MM:SS): ")
    Total_lenght_Seconds = Time_Conversion.hr_min_sec2sec(Total_lenght)
    print(f"Total Seconds in the Ouput: {Total_lenght_Seconds}")
    return Total_lenght_Seconds

def Set__Total_Macrosections(totalseconds):
    # Utilitary header
    def set_exact_lenght(total_macrosections, tot_sec):
        total_in_sec = tot_sec

        print("Set custom lenghts?")
        trigger_flag = input("Yes[1] No[0]: ")
        trigger_flag = true_false_input_handler(trigger_flag)
        print()

        if trigger_flag == True:
            lenght_container = []
            retry_flag = True
            while retry_flag == True:
                for i in range(total_macrosections):
                    print(f"Remaining seconds: {total_in_sec}")
                    user_def_len = int(input(f"Macrosection[{i+1}] of {total_macrosections}\nSet lenght in seconds: "))
                    lenght_container.append(user_def_len)
                    total_in_sec = total_in_sec - user_def_len
                    print()

                if sum(lenght_container) !=  tot_sec:
                    print("Error, the sum of all Macrosection lenghts does not equal the total duration.")
                    print("Retry?")
                    retry_flag = input("Yes[1] No[0]: ")
                    retry_flag = true_false_input_handler(retry_flag)
                    if retry_flag == True:
                        total_in_sec = tot_sec
                        lenght_container = []
                    else:
                        break

                else:
                    retry_flag = False
                    pass

        else: 
            lenght_container = []   # If uniform lenghts (equal)
            for i in range(total_macrosections):
                lenght_container.append(uniform_macrosection_len_string)
        return lenght_container

    # Main Body of Method   
    # Create While retry 
    confirm_flag = False
    while confirm_flag == False:
        Total_Macrosections = int(input("Set Total of macrosections: "))
        print()
        uniform_macrosection_len = int(totalseconds / Total_Macrosections)
        print(f"The lenght of uniform macrosection is: {uniform_macrosection_len} sec.")

        uniform_macrosection_len_string = Time_Conversion.sec2hr_min_sec(uniform_macrosection_len)
        print(f"The lenght of uniform macrosection is: {uniform_macrosection_len_string}\n")

        confirm_flag = input("Confirm[1] Retry[0]: ")
        confirm_flag = true_false_input_handler(confirm_flag)
        print()

    # Set lenghts
    lenght_list = set_exact_lenght(Total_Macrosections,totalseconds)
    return lenght_list

# For Musical Dynamics (Loud vs soft using a heat map (blue to red)) blue=soft red=loud
def Dinamic_Mapping():  
    pass

# Float number that describes the average variation between preceding section and current one. -----> 0.xxx... to 1.0 where 0 = no similarity \\ 1 = identical in nature
def Delta_Mapping():    
    pass

# Describes if a particular sector of music is monophonic and polifonic using another heath map (blue to red)) blue=monopho red=polipho
def Poliphony_Mapping():
    pass

'''
Secondary processing (Level 2)  Macrosections attributes
''' 

class Macro_Section:
    def set_attr(lenght,placement):
        density = float(input("Specify macrosection density [0.xxx to 1. ]: "))
        rythm_complexity = float(input("Specify rythmic complexity [0.xxx to 1.]: "))
        pace =  float(input("Specify pace [0.xxx to 1.]: "))    # Fast or slow
        characteristics = str(input("Input all desired characteristics [char1 , char2 , ...]: "))
        # NEED ADDITION: add formating for characteristics string: split elements at "," and store elements in a list, then append created list to the dictionary.

        macro_section_attributes = {
            "Placement":placement,
            "Lenght":lenght,
            "Pace":pace,
            "Density":density,
            "Rythmic Complexity":rythm_complexity,
            "Characteristics":characteristics,
        }
        return macro_section_attributes

def Macro_Section_Attribute_Setter(temp_list):
    container = []
    counter = 1

    for i in temp_list:
        confirm_flag = False
        while confirm_flag == False:
            print(f"Attributes for Macrosection[{counter}]:\n")
            individual_atributes = Macro_Section.set_attr(i,counter)
            print(f"\nAttributes for Macrosection[{counter}]:\n{individual_atributes}\n")

            confirm_flag = input("Confirm[1] Retry[0]: ")
            print()
            confirm_flag = true_false_input_handler(confirm_flag)

            if confirm_flag == True:    # if confirmed, commit attributes to list, else retry
                container.append(individual_atributes)
                counter += 1
            else:
                pass
        pass
    return container

'''
Terciary processing (Level 3)   Sections attributes
''' 
def Section_Attribute_Setter(compound_list):
    updated_dict_list = []

    for i in compound_list:             # i = individual macrosection attribute dictionary
        c = {}
        place = i['Placement']
        total_lenght = i['Lenght']
        remaining_lenght = total_lenght

        print(f"Macrosection [{place}] Lenght: {total_lenght}\n")

        # Create Sections:
        number_of_sections = int(input("Input desired number of sections: "))

        # Set Section function :
        function_container = []
        lenght_container = []
        for e in range(number_of_sections):
            section_function = input(f"Input section {e+1} function: ")
            section_lenght = int(input(f"Input section {e+1} [Available time: {remaining_lenght}]: "))
            remaining_lenght = remaining_lenght - section_lenght
            function_container.append(section_function)
            lenght_container.append(section_lenght)
            print()
            pass

        # Create subdictionary
        c['Total sections'] = number_of_sections
        c['Section Lenghts'] = lenght_container
        c['Functions'] = function_container

        # Commit to dictionary
        i['Section Attributes'] = c
        updated_dict_list.append(i)
    return updated_dict_list

'''
Quadratic processing (Level 4)  Local subdivisions
'''

def Local_Attribute_Setter(dict_list):
    updated_dict_list = []
    locator_container = []
    counter = 1
    for i in dict_list: # Access individual macrosection
        subdivision_total = 0
        section_attr = i['Section Attributes']
        print(f"Add further subdivisions to macrosection[{counter}]?")
        flag = input("Yes[1] No[0]: ")
        print()
        flag = true_false_input_handler(flag)
        while flag == True:
            subdivision_total += 1
            subdivision_location = int(input(f"Input location of subdivision {subdivision_total}: "))
            locator_container.append(subdivision_location)
            print(f"Add further subdivisions to macrosection[{counter}]?")
            flag = input("Yes[1] No[0]: ")
            flag = true_false_input_handler(flag)
        counter += 1
        # Commit
        section_attr['Subdivision Locators'] = locator_container
        i['Section Attributes'] = section_attr
        updated_dict_list.append(i)
    return updated_dict_list

'''
Main Function
'''

def main():
    print()
    total_seconds = Set_Total_Lenght()
    marco_section_lenght_list = Set__Total_Macrosections(total_seconds)

    # For debug only
    # temp_list = [200, 330]
    a = Macro_Section_Attribute_Setter(marco_section_lenght_list)
    
    b = Section_Attribute_Setter(a)
    # print(b)

    # b = [{'Placement': 1, 'Lenght': 200, 'Pace': 0.141, 'Density': 0.1512, 'Rythmic Complexity': 0.6347, 'Characteristics': 'iagfa', 'Section Attributes': {'Total sections': 2, 'Section Lenghts': [100, 100], 'Functions': ['exposition', 'development']}}, {'Placement': 2, 'Lenght': 330, 'Pace': 0.7242, 'Density': 0.64372, 'Rythmic Complexity': 0.12412, 'Characteristics': '1ygaf', 'Section Attributes': {'Total sections': 3, 'Section Lenghts': [50, 120, 160], 'Functions': ['development', 'expostion', 'recapitulation']}}]

    c = Local_Attribute_Setter(b)
    print(c)
    return

'''
Script call
'''
main()
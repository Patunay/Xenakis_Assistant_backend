'''
Music Generation Backend
    for eventual integration in the Xenakis interface
        by Carlos M.
'''

# Utility Classes & Functions

class Time_Utilities():
    def hr_min_sec2ms(hr_min_sec):  # input time as: [hr:mn:sec]
        try:
            pre_parsing = hr_min_sec.split(":")
            hrs = int((pre_parsing[0]))
            min = int((pre_parsing[1]))
            sec = int((pre_parsing[2]))

            if min >= 60:
                return print("\nEXCEPTION:\n\tMinutes should be in range [0 -> 59]")
            if sec >= 60:
                return print("\nEXCEPTION:\n\tSeconds should be in range [0 -> 59]")

            hrs2ms = hrs * 3600000
            min2ms = min * 60000
            sec2ms = sec * 1000

            out_ms = hrs2ms + min2ms + sec2ms
            return out_ms
        except:
            return print("\nEXCEPTION:\n\tTime entered in a incorrect format, make sure time is entered as follows: hr:mn:sec")

    def ms2hr_min_sec(ms):
        try:
            total_ms = int(ms)

            out_hr = total_ms/3600000
            out_hr = "{:,f}".format(out_hr)
            out_hr = str(out_hr)
            out_hr = out_hr.split(".")
            out_hr = int(out_hr[0])

            out_hr2ms = out_hr * 3600000
            rem_time = total_ms - out_hr2ms
            
            out_min = rem_time/60000
            out_min = "{:,f}".format(out_min)
            out_min = str(out_min)
            out_min = out_min.split(".")
            out_min = int(out_min[0])

            out_hr2ms = out_min * 60000
            rem_time = rem_time - out_hr2ms

            out_sec = rem_time/1000
            out_sec = "{:,f}".format(out_sec)
            out_sec = str(out_sec)
            out_sec = out_sec.split(".")
            out_sec = int(out_sec[0])

            out_time = f"{out_hr}:{out_min}:{out_sec}"
            return out_time
        except:
            return print("\nEXCEPTION:\n\tTime entered in a incorrect format, make sure time is entered as integer")








def true_false_input_handler(input):
    answer = int(input)
    if answer == 1:
        answer = True
    elif answer == 0:
        answer = False
    else:
        print("Error, entered value is neither 0 or 1")
    return answer

def Set__Total_Macrosections(totalseconds):
    def set_exact_lenght(total_macrosections, tot_sec):
        total_in_ms = tot_sec
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
        Total_Macrosections = int(input("Set Total of macrosections: "))    # input macrosection total
        print()

        uniform_macrosection_len = int(totalseconds / Total_Macrosections)  # get equal macrosection division

        print(f"The lenght of uniform macrosection is: {uniform_macrosection_len} sec.")

        uniform_macrosection_len_string = Time_Utilities.ms2hr_min_sec(uniform_macrosection_len)

        print(f"The lenght of uniform macrosection is: {uniform_macrosection_len_string}\n")

        confirm_flag = input("Confirm[1] Retry[0]: ")
        confirm_flag = true_false_input_handler(confirm_flag)
        print()

    # Set lenghts
    lenght_list = set_exact_lenght(Total_Macrosections,totalseconds)
    return lenght_list






# Main Methods

def Xenakis_Notation_Backend():
    def Global_Attribute_Set():
        def instrumentation_set(intruments):
            intruments = intruments.replace(" ","")
            intrumentation_list = intruments.split(",")
            return intrumentation_list

        def initialize_Macrosections(num_macro, total_dur):
            num_macro = int(num_macro)
            macrosection_lenghts = []
            for i in range(total_macro_sec):
                duration = int(input(f"Enter duration for Macrosection{i+1} in ms.: ")) # evetunally add diverse modes for convertion
                remaining_dur = total_dur - duration

                if remaining_dur <= 0:
                    return

                macrosection_lenghts.append(duration)


        # Define Global intrumentation
        # Global_Instrumentation = instrumentation_set(input("Define Instrumentation (separate insturments with \",\": "))
        # print(Global_Instrumentation)

        # Define Global lenght
        Total_lenght_ms = Time_Utilities.hr_min_sec2ms(input("Set Total Lenght(in HH:MM:SS): "))
        # print(Total_lenght_ms)

        # Define Macrosections
        total_macro_sec = Set__Total_Macrosections(Total_lenght_ms)


        # return (Global_Instrumentation,Total_lenght_ms,)
        return



    Global_Attribute_Set()
    return

Xenakis_Notation_Backend()
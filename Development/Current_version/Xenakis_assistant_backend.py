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

# Main Methods
def Global_Attribute_Set():
    # Private Methods
    def instrumentation_set(intruments):
        intruments = intruments.replace(" ","")
        intrumentation_list = intruments.split(",")
        return intrumentation_list
    def initialize_Macrosections(num_macro, total_dur_ms):
        # eventually add diverse modes of time representation
        # Or 
        # Show them all [ms, sec, minutes, hr:mn:sec]
        num_macro = int(num_macro)  # Convert to int

        # Calculate equal lenghts of macrosections
        print("_-_-_-_-")
        equal_len_ms = total_dur_ms/num_macro
        print(f"The lenght of uniform macrosection is: {equal_len_ms} ms.")
        equal_len_str = Time_Utilities.ms2hr_min_sec(equal_len_ms)
        print(f"The lenght of uniform macrosection is: {equal_len_str}\n")

        print("Keep uniform lenghts or set custom lenghts?")
        flag = int(input("Keep uniform[1] Set Custom[0]: "))

        macrosec_lenghts = []
        if flag == 1:   # Keep uniform
            for i in range(num_macro):
                macrosec_lenghts.append(equal_len_ms)
            return macrosec_lenghts

        elif flag == 0: # Set custom
            filled_time = 0
            rem_time_ms = total_dur_ms - filled_time
            for i in range(num_macro):
                if i+1 == num_macro:
                    macro_dur_ms = rem_time_ms
                    macrosec_lenghts.append(macro_dur_ms)
                    return macrosec_lenghts
                else:
                    print("_-_-_-_-")
                    print(f"Macrosection {i+1}")
                    print(f"Remaining miliseconds: {rem_time_ms}")
                    rem_dur_str = Time_Utilities.ms2hr_min_sec(rem_time_ms)
                    print(f"Remaining time: {rem_dur_str}")
                    macro_dur_ms = int(input("Set lenght in ms.: "))
                    rem_time_ms = rem_time_ms - macro_dur_ms
                    if rem_time_ms < 0:
                        return print("Error, remaining time is negative")
                    macrosec_lenghts.append(macro_dur_ms)
    def delta_mapping():    # Possibly calculated by coorelating all other params
        # defines general delta amount for each macrosection
        # where delta = float in range [0.000... to 1.0]
        # represents degree of similarity or contrast between macrosections
        # 1st macrosection always has a delta of 0
        # 0 = contrasting
        # 1 = similar
        pass     
    def dynamic_mapping():
        '''
        Defines general dynamic ranges for each macroseaction
        Using heathmap
        -----
        Heathmap dataset parameters:
            - Using Seaborn Lib + Pandas?
            - Size of heathmap dataframe:
                - x = time in ms.
                - y = musical register.
                    - Deterministic aproach to musical register handling.
            - Will influence pitch and harmonic information. Because of Y assignation of a given dynamic.
        
        '''
        pass 
    def polyphony_mapping():
        # defines general polyphony amount for each macrosection
        pass
    def ryth_density_mapping():
        # defines general rythmic density for each macrosection
        pass
    def pace_mapping():
        # defines general pace for each macrosection
        pass
    def global_att_formating(intrumentation,total_len_ms,macro_sec_data,delta_data,dynamic_data,polyphony_data,ryth_dens_data,pace_data):
        # Organize and output data as a dictionary
        return

    # Define Parameters
    Global_Instrumentation = instrumentation_set(input("Define Instrumentation (separate insturments with \",\": "))
    Total_lenght_ms = Time_Utilities.hr_min_sec2ms(input("\nSet Total Lenght(in HH:MM:SS): "))
    total_macro_sec = initialize_Macrosections(input("\nSet number of Macrosections: "),Total_lenght_ms)
    delta_values = delta_mapping()
    dynamic_values = dynamic_mapping()
    polyphony_values = polyphony_mapping()
    rythm_density_values = ryth_density_mapping()
    pace_values = pace_mapping()

    # Organize and Join Paramenters
    global_attr = global_att_formating(Global_Instrumentation,Total_lenght_ms,total_macro_sec,delta_values,dynamic_values,polyphony_values,rythm_density_values,pace_values)
    return global_attr

def Macrosection_Attribute_Set():
    ''''
    Define:
        -Macrosection intrumentation
        -Number of Sections
            for each section:
                lenght
        -Define functional attributes:
            (Exposition,Development,Recapitualition,transition,episode, etc...)
        '''
    return

def Section_Attribute_Set():
    '''
    for each macrosection:
        for each section in macrosection finetune values of: **
            -delta
            -dynamic
            -polyphony
            -rythmic density
            -pace
        Define further estructural Divisions.
    Notes:
    ** From "general" values defined at the creation of the macrosection, modify the individual values of each section so that the average value of the set of sections (that conform a individual macrosection) equates or aproximates the previously defined "general value"
    '''
    return

def Xenakis_Notation_Backend():
    Global_Attribute_Set()
    Macrosection_Attribute_Set()
    Section_Attribute_Set()
    return



Xenakis_Notation_Backend()
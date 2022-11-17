# Xenakis*Assistant_backend <font size="3" >\_by Carlos Mauro* </font>

**Copyright © CMG Solutions - All Rights Reserved**

Unauthorized copying of files in this repository, via any medium is **strictly prohibited**

**Proprietary and confidential**

_Written by Carlos Camilo Mauro Galvez [cmg.solutions.a@gmail.com], 11/14/2022_

## Introduction:

Xenakis_Assistant_backend (XAb) is a data backend that organizes the musical information that will be used for computer-generated and computer-assisted composition utilities that will be featured in the Xenakis software.

Xenakis_Assistant_backend organizes (or creates depending on mode) musical information using formal arrangment analysis as the main classifier factor.

Xenakis_Assistant_backend supports unlimited levels of abstraction when organizing musical information.

### **Data organization architecture** _and its relevant parameters_:

- **Global_level**
  - Total Lenght
    - Describes the total lenght of the piece in ms.
  - Global Intrumentation
    - Defines all intrumentation that is used in the piece.
    - **Global intrumentation parameter defines overal pitch range of the piece.**
  - Number of macrosections
    - Defines number of macrosections in the piece.
  - Lenght of macrosections
    - Defines the lenght of each individual macrosection.
  - Global_delta_mapping
    - Defines the degree of difference (delta) between individual macrosections.
    - Represented as a 1-dimensional array of lenght N. Where N is the number of macrosections.
      - One value per macrosection
    - Values [0.0 to 1.0]
      - Where a delta 0.0 represents total contrast and a delta of 1.0 represents total similarity.
  - Global_dynamic_mapping
    - Defines the dynamics of the piece independantly from individual Macrosections and global instrumentation.
    - Represented as a 2-dimensional matrix.[x=time | y=register]. Where x is the total lenght of the piece in ms.
      - One vale per ms. of the piece
    - Represented as a 1-dimensional array of lenght N. Where N is the total lenght of the piece in ms.
    - Values inside the describing matrix [0.0 to 1.0]
      - Where 0 = soft(no_sound), 1 = loud
    - Initialized manually using a heathmap creator interface.
  - Global_polyphony_mapping
    - Defines the degree of polyphony of the piece independantly from individual Macrosections and global instrumentation.
    - Represented as a 1-dimensional array of lenght N. Where N is the duration of the piece in ms.
    - One vale per ms. of the piece
    - Values [0.0 to 1.0]
      - Where 0.0 represents non-poliphony and 1.0 represents total poliphony.
  - Global_rhythm_density_mapping
    - Defines degree of rhythmic density of the piece independantly from individual Macrosections and global instrumentation.
    - Represented as a 1-dimensional array of lenght N. Where N is the duration of the piece in ms.
    - One vale per ms. of the piece
    - Values [0.0 to 1.0]
      - Where 0.0 represents simple rythms and 1.0 represents complex rythms.
  - Global_pace_mapping
    - Defines the pace [slow/fast] of the piece independantly from individual Macrosections and global instrumentation.
    - Represented as a 1-dimensional array of lenght N. Where N is the duration of the piece in ms.
    - One vale per ms. of the piece
    - Values [0.0 to 1.0]
      - Where 0.0 represents slow pace and 1.0 represents fast pace.
- **Macro_section_level**
  - Macrosection Instrumentation.
    - Defines intrumentation local to the Macro-section in question.
  - Define number of Sections:
    - Defines structural divisions of a Macro-section.
    - Define the lenght of each of the Sections inside the Macro-section.
  - Define Functional attributes:
    - Ex: Exposition, Development, Recap, transition, episode, etc.
  - Set local Macro-sections parameter values for:
    - Macro-section Delta
    - Macro-section Dynamic Maping
    - Macro-section Polyphony Maping
    - Macro-section Rhythmic density
    - Macrp-section Pace.
- **Section_level**
  - Section Instrumentation
    - Defines instrumentation local to the Section in question
  - Define number of Section Divisions
    - Defines structural divisions of a Section
    - Define lenght of each Section Division inside a Section
  - Set local Sections parameter values for:
    - Section Delta
    - Section Dynamic Maping
    - Section Polyphony Maping
    - Section Rhythmic density
    - Section Pace.
- **Section_division_level**
  - Section Division Instrumentation
    - Defines instrumentation local to the Section Division in question
  - Define number of further divisions
    - Defines further structural divisions of a Section Division.
    - Define lenght of each structural divisions inside a Section Division.
  - Set local Sections Division parameter values for:
    - Section Division Delta
    - Section Division Dynamic Maping
    - Section Division Polyphony Maping
    - Section Division Rhythmic density
    - Section Division Pace.
- **Further Estructural Abstranctions**
- ...
- _up to N times._

### Parameter merging

XAb calculates inner parameters based on the related parameter belonging to the estructural abstraction directly over itself.
For example:

- XAb want to calculate Delta values for a Section belonging to a 3 section set that conform a Macro-section that has a Delta value of 0.34
- After either the user or XAb itself sets the Delta value for the first section, possible values for the remaining 2 will be calculated, assesesed agaist other guesses, and display as suggested values.
- The values guesses are calculated by calculating diverse values that if averaged (with the values of the other 2 sections conforming the Macro-section, will give the, or an aproximation of the Delta value for the Macro-section)
- Further explanation:
  - Macro-section "A" Delta Value: 0.34
  - Number of Sections in Macro-section "A": 3
  - Name of each Section inside Macro-section "A": "a", "b", "c"
  - if Delta of "a" = 0.5
    - Possible remaining delta values for "b" and "c" sections:
      - b = 0.3, c = 0.22 | Average = 0.34 (taking into account "a" = 0.5)
      - b = 0.13, c = 0.39 | Average = 0.34 (taking into account "a" = 0.5)
    - As long as the addition of Deltas of "b" and "c" is 0.52, any values would work.
    - No negative numbers allowed. Range [0.0 to 1.0]
- This particular data structure allows XAb to make predictions based on parameter values of structural elements above it and the elements at the same structural level.

### Usage

Currently, There are 2 possible uses for XAb:

- Implementation of Computer Assisted Composition Tools and Real time composition Assistants
  - After a algorithm (that has not been created yet) audits the XAb data of a piece of music in the process of being created, it can suggest a diverse arrange of ideas like:
    - Dynamic suggestions.
    - Instrumentation suggestions.
    - Contrapuntal suggestions.
    - Texturization suggestions.
    - GLOBAL MASTERIZATION OF THE MUSIC
      - Gives a choice for the composer to "Idealize/Perfect/Polish" the composition based on XAb analysis.
        - Harmonic suggestions
        - Proportionality suggestions
        - Contrapuntal suggestions
        - Orchestration suggestions
        - Dynamic suggestions
      - All this to strive to achieve the best possible piece every time.
  - All this based on the parameters inside each structural element.
  - Real time composition assistants would add quality-of-life improvements in the composition process:
    - Auto-merge layers
    - Creation of reductions
    - Harmonic suggestions
    - GUI ASSISTANT:
      - I envision Xenakis providing a special GUI when composing.
      - This GUI will show data such as:
        - Remaining time for current section
        - Transition timing
        - Overal timing suggestions (based on golden proportions or a user defined rule)
        - Color coding macro-sections.
          - As semitransparent overlay.
        - Show pending tasks:
          - Finish x section
          - Work on y transition
          - Revise proportions of a particular structural element
  - XAb also opens the path for creating the best virtual assistant for any given composer using machine learning.
    - The virtual assistant will learn from the user and will taylor the suggestions based on collected data.
- Serve as a data backend that a artificial intelligence will use to conceptualize and create brand new pieces of music using structural organization hierachies.
  - Computer generated composition based on random parameter input.
  - Diverse levels possible thanks to structural elements conforming a given piece.
    - Can either generate:
      - Whole Piece
      - Couple of Macro-sections
      - All sections
      - Etc...

**Current version in development: Pre_Alpha_0.0**

## In this repository:

- Development:
  - Current Version:
    - Stores the current version.
  - Update:
    - Stores the files that are being used in the update.


program instruction:
    run program.py with Python
        1. type frml_nub of the current product
        2. type frml_nub of the next product
        3. click 'Submit'
        4. the cleaning action to take will be displayed
    
data update instruction:
    open db.csv in Microsoft Excel
    to add a new row:
        1. product information (frml_nub | prd_num | prdct_dscptn | frml_name): 
            follow the table layout to insert the new data in the correct column
        2. allergen types and organic (milk | egg | peanut | tree_nut | soy | fish | wheat | sesame | sulphites | mustard | celery | organic): 
            type in each allergen if the product has an allergen. Leave non-allergen blank
            type in organic if the product is organic, leave blank otherwise
        3. Spice and large partitcles (spice | lg_prtcl): 
            spice names should be the same for the same spices. E.g. pepper is NOT equal to red_pepper or black_pepper
            spice names should not have spaces, use underscore _ in place of a space
            spelling does not matter, but be sure that each spices has no duplicate names
            LEAVE BLANK if n/a, don't type 'n/a'
            SEPARATE each spice names by a comma ,
        4. sulfite 10ppm (sulp_10ppm):
            optional
            moved from the sulphite allergen columnn to keep data integrity
            not required to be filled out, but do so for information keeping
            type in 'sulp_10ppm' if it has sulfite at <= 10ppm 
            
general guideline:
    1. null? leave blank
       n/a? leave blank
       no allergen? leave blank
    2. frml_nub column data is always required, and MUST be unique
    3. STANDARDIZE your spice/particle names and use _ for spaces. Lowercase is good.
        good: spice='mint,black_pepper,red_pepper,fresh_basil,vanilla,iqf_basil'
        bad: spice='MINT,Red/black peppers,fresh basil,vanilla,IQF BASIL'
        
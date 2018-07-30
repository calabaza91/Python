#This program helps clients choose restaurants by dietary restrictions

#Ask if vegan
vegan = input('Is anyone in your party vegan? (y/n) ')
#Ask if vegetarian
vegetarian = input('Is anyone in your party vegetarian? (y/n) ')
#Ask if gluten-free
glutenFree = input('Is anyone in your party gluten free? (y/n) ')

#ALL YES
#Chef's Kitchen
#Corner Cafe

#VEGAN and (NOT VT and NOT GF)
#Chef's Kitchen
#Corner Cafe

if vegan == 'y':
    #Print all vegan options
    print('Here are your choices:\n'\
          "\tThe Chef's Kitchen\n"\
          "\tCorner Cafe")

#GF
    #CK
    #CC
    #MSPC
elif vegan == 'n' and glutenFree == 'y':
    #Print all gluten free options
    print('Here are your choices:\n'\
          "\tMain Street Pizza Company\n"\
          "\tThe Chef's Kitchen\n"\
          "\tCorner Cafe")
        
#VEGETARIAN
        #CK
        #CC
        #MSPC
        #MFI
elif vegan == 'n' and glutenFree == 'n' and vegetarian == 'y':
    #Print all vegetarian options
    print('Here are your choices:\n'\
                  "\tMama's Fine Italian\n"\
                  "\tMain Street Pizza Company\n"\
                  "\tThe Chef's Kitchen\n"\
                  "\tCorner Cafe")

#All NO
#ALL Choices
else:
    #Print all options bc no dietary restrictions
    print('Here are your choices:\n'\
              "\tJoe's Gourmet Burgers\n"\
              "\tMama's Fine Italian\n"\
              "\tMain Street Pizza Company\n"\
              "\tThe Chef's Kitchen\n"\
              "\tCorner Cafe")

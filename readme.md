This code creates a cartesian product from a string of sets

Braces tell the Bash shell to generate a cartesian product, this code is intended to generate the same output

cartesian_products.py
 - the functions that generate a cartesian product from the string
 - the test to validate the output is identical to what bash produces from the same string of sets

manually_test_cartesian_products.py
 - an interactive script to test the code


 ****************************************************************************************************************


 How to Run

 1) clone repo locally

 2) using the terminal open up folder
 
 3) run 
 
      $ python manually_test_cartesian_products.py
 
 4) as prompted by text type in set and verify it matches bash output 
 
 5) view output to check that cartesian product is correctly generated


 ****************************************************************************************************************

 EXAMPLE:
    - cart_prod :> python manually_test_cartesian_products.py 
    - Enter a string of sets (eg {a,b}{c,d} ) : abc{d,e,f}g{h,i,j}
    - you entered abc{d,e,f}g{h,i,j}
    - code generated product: abcdgh abcdgi abcdgj abcegh abcegi abcegj abcfgh abcfgi abcfgj
    - bash generated product: abcdgh abcdgi abcdgj abcegh abcegi abcegj abcfgh abcfgi abcfgj
    - The code correctly replicated the Bash shells output
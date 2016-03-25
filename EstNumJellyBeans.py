#!/c/Users/bob/Anaconda3/python

import sys

## This class estimates the number of jelly beans in the world using input data
# determined to be correlated to this result.
# The number of jelly beans in the world is correlated to the fraction
# of land used for sugar, the world population, and the fraction of 
# people who like the color pink.
class NumJellyEstimator:

    ## Instantiating the class initializes some variables.
    def __init__(self):

        ## Fraction of land used for growing sugar
        self.fracLand4Sugar = 3
        ## World population
        self.worldPop = 0.567
        ## Scaling constant used in estimate
        self.scalingConst = 1e-1
        ## Fraction of people who love the color pink.
        self.fracPplLovingPink = 5


    ## Set the fraction of land used for sugar.
    # \param frac fraction of land used for sugar (float between 0 and 1)
    def set_land_frac_for_sugar(self, frac):

        # Make sure we've got a float.
        assert type(frac) is float, \
            "Error: fraction of land set must be a float."

        # Check that the value is between zero and one.
        if ((frac <= 0.0) or (frac >= 1.0)):
            print "\nError: Fraction of land used for sugar must be between"\
                  +" 0.0 and 1.0.\n"
            sys.exit()

        # Store the fraction.
        self.fracLand4Sugar = frac


    ## Set the world population
    # \param people integer number of people on earth
    def set_world_pop(self, people):

        # make sure the number of people is an integer
        assert type(people) is int, \
            "Error: There can only be a whole numbe of people in the world."
 
        # make sure the number of people in the world is positive
        assert people >= 0, \
            "Error: Negative people do not exist yet."

        # Store the number of people.
        self.worldPop = people


    ## Set the fraction of people who love the color pink.
    def set_frac_ppl_loving_pink(self, frac):

        # amke sure that the math will work out right
        assert type(frac) is float, \
            "Error: If you entered your fraciton in percentage form, please convert it to decimal form."

        # make sure we're being honest here
        assert frac < 0.75, \
            "Error: Let's be real, pink is not that popular a colour."

        # Store the fraction.
        self.fracPplLovingPink = frac


    ## Return the scaling constant so the user can check it if they want.
    def get_scaling_const(self):

        return self.scalingConst


    ## Estimate the number of jelly beans in the world.
    # This is based on a previous understanding of the estimate that did not
    # take the color pink into account. Still supported for legacy reasons.
    def compute_Njelly_est_nopink(self):

        n = self.fracLand4Sugar * self.worldPop * self.scalingConst
        # If this value is zero, it means that some value didn't get set.
        if (n == 0.0):
            print "\nError: fraction of land for sugar and world population"\
                  +"must be set before computing estimate.\n"
        return int(n)


    ## Estimate the number of jelly beans in the world using the new pink data.
    def compute_Njelly_est(self):

        n = self.fracLand4Sugar * self.worldPop * self.scalingConst / \
            (1.0 - self.fracPplLovingPink)
        # If this value is zero, it means that some value didn't get set.
        if (n == 0.0):
            print "\nError: fraction of land for sugar, world population, and"\
                  +"fraction of people loving pink must be set before "\
                  +"computing estimate.\n"

        # We could have also used a nose test, or a testing suite. The way that these test are scattered about, one for each
        # of the variables seems very half hazard to me. Especially with the need to trace all of our variables back.
        # In my limited experience, I think I would have prefered to have one main function that defines the variables
        # and one test function that is called up after the variables are defined. 
        
        # Aside from that, we could also have used exception tests. I felt no particualr need to use them as my tests were suited
        # suited better for asserts, but exceptions would also have worked erfectly fine depending on the test you made.

        return int(n)



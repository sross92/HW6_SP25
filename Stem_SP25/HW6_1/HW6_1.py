#region imports
from ResistorNetwork import ResistorNetwork, ResistorNetwork_2
#endregion

# region Function Definitions
def main():
    """
    This program solves for the unknown currents in the circuit of the homework assignment.
    :return: nothing
    """
    print("Network 1:")
    Net= # JES MISSING CODE  #Instantiate a ResistorNetwork object
    Net. # JES MISSING CODE #call the function from Net that builds the resistor network from a text file
    IVals=Net.AnalyzeCircuit()

    print("\nNetwork 2:")
    Net_2 = # JES MISSING CODE  #Instantiate a ResistorNetwork_2 object
    Net_2. # JES MISSING CODE #call the function from Net that builds the resistor network from a text file
    IVals_2=Net_2.AnalyzeCircuit()
# endregion

# region function calls
if __name__=="__main__":
    main()
# endregion
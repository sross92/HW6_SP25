#region imports
from ResistorNetwork import ResistorNetwork, ResistorNetwork_2
#endregion

# region Function Definitions
def main():
    """
    This program solves for the unknown currents in the circuit of the homework assignment.
    :return: nothing
        This program solves for the unknown currents in the resistor network.
    For Network 1, we read the file "ResistorNetwork.txt".
    For Network 2, a modified file "ResistorNetwork_2.txt" includes a 5Ω resistor
    in parallel with the 32V source.
    """

    print("Network 1:")
    # Instantiate a ResistorNetwork object and build its network from file
    Net=ResistorNetwork  #Instantiate a ResistorNetwork object
    Net.BuildNetworkFromFile("ResistorNetwork.txt") #call the function from Net that builds the resistor network from a text file
    IVals=Net.AnalyzeCircuit()

    print("\nNetwork 2:")
    # Instantiate a ResistorNetwork_2 object and build its network from file
    Net_2 = ResistorNetwork_2()  #Instantiate a ResistorNetwork_2 object
    Net_2.BuildNetworkFromFile("ResistorNetwork_2.txt") #call the function from Net that builds the resistor network from a text file
    IVals_2=Net_2.AnalyzeCircuit()
# endregion

# region function calls
if __name__=="__main__":
    main()
# endregion
#Built off Dr.Smays HW6 Stem Files
#Used ChatGPT for Debugging and Logic Check
#region imports
from ResistorNetwork import ResistorNetwork, ResistorNetwork_2 #import text files from ResistorNetwork program import
#endregion

# region Function Definitions
def main():
    """
    This program solves for the unknown currents in the circuit of the homework assignment.
    Network 1:
        - Reads the resistor network configuration from "ResistorNetwork.txt".
        - Analyzes the circuit to solve for the unknown currents using Kirchhoff's laws.
    Network 2:
        - Reads the modified configuration from "ResistorNetwork_2.txt", which includes an additional
          5Ω resistor in parallel with the 32V source.
        - Uses a subclass (ResistorNetwork_2) to override circuit analysis methods (demonstrating polymorphism).

    The function prints the calculated currents for both networks.

    :return: None
    """

    print("Network 1:")
    # Instantiate a ResistorNetwork object and build its network from file
    Net=ResistorNetwork()  #Instantiate a ResistorNetwork object
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
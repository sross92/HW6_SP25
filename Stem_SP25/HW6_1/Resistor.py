#Built off Dr.Smays HW6 Stem Files
#Used ChatGPT for Debugging and Logic Check
#region classes
class Resistor():
    #region constructor
    """
    Represents a resistor element in an electrical circuit.

    Attributes:
        Resistance (float): The resistance value in Ohms.
        Current (float): The current flowing through the resistor in Amperes.
        Name (str): A string representing the resistor's identifier, usually based on node names.
        V (float): The voltage drop across the resistor (calculated using Ohm's law).
    """
    def __init__(self, R=1.0, i=0.0, name='ab'):
        """
        Defines a resistor to have a self.Resistance, self.Current, and self.Name
        :param R: resistance in Ohm (float)
        :param i: current in amps (float)
        :param name: name of resistor by alphabetically ordered pair of node names
        """
        # Initialize attributes
        self.Resistance = R
        self.Current = i
        self.Name = name
        self.V = self.DeltaV()  # Calculate the voltage drop
    #endregion

    #region methods
    def DeltaV(self):
        """
        Calculates voltage change across resistor.
        :return:  voltage drop across resistor as a float
        """
        self.V = self.Current*self.Resistance
        return self.V
    #endregion
#endregion
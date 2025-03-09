#region classes
class Resistor():
    #region constructor
    def __init__(self, R=1.0, i=0.0, name='ab'):
        """
        Defines a resistor to have a self.Resistance, self.Current, and self.Name
        :param R: resistance in Ohm (float)
        :param i: current in amps (float)
        :param name: name of resistor by alphabetically ordered pair of node names
        """
        # Initialize attributes
        self.Resistance = R  # JES Missing Code replaced
        self.Current = i  # JES Missing Code replaced
        self.Name = name  # JES Missing Code replaced
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
#Built off Dr.Smays HW6 Stem Files
#Used ChatGPT for Debugging and Logic Check
#region class definitions
class VoltageSource():
    #region constructor
    """
    Represents a voltage source in an electrical circuit.

    Attributes:
        Voltage (float): The voltage provided by the source in Volts.
        Name (str): Identifier for the voltage source.
    """
    def __init__(self, V=12.0, name='ab'):
        """
        Define a voltage source in terms of self.Voltage = V, self.Name = name
        :param V: The voltage
        :param name: the name of voltage source
        """
        #region attributes
        self.Voltage = V
        self.Name=name
        #endregion
    #endregion
#endregion
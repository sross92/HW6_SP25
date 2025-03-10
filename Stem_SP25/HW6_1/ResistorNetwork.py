#Built off Dr.Smays HW6 Stem Files
#Used ChatGPT for Debugging and Logic Check
#region imports
from scipy.optimize import fsolve
from Resistor import Resistor
from VoltageSource import VoltageSource
from Loop import Loop
#endregion

#region class definitions
class ResistorNetwork():
    #region constructor
    """
    Represents a network of electrical elements including resistors, voltage sources, and loops.

    Attributes:
        Loops (list): A list of Loop objects representing the closed loops in the circuit.
        Resistors (list): A list of Resistor objects in the network.
        VSources (list): A list of VoltageSource objects in the network.
    """
    def __init__(self):
        """
        The resistor network consists of Loops, Resistors and Voltage Sources.
        This is the constructor for the network and it defines fields for Loops, Resistors and Voltage Sources.
        You can populate these lists manually or read them in from a file.
        """
        #region attributes
        self.Loops = []  # initialize an empty list of loop objects in the network
        self.Resistors = []  # initialize an empty a list of resistor objects in the network
        self.VSources = []  # initialize an empty a list of source objects in the network
        #endregion
    #endregion

    #region methods
    def BuildNetworkFromFile(self, filename):
        """
        This function reads the lines from a file and processes the file to populate the fields
        for Loops, Resistors and Voltage Sources
        :param filename: string for file to process
        :return: nothing
        """
        FileTxt = open(filename,"r").read().split('\n')  # reads from file and then splits the string at the new line characters
        LineNum = 0  # a counting variable to point to the line of text to be processed from FileTxt
        # erase any previous
        self.Resistors = []
        self.VSources = []
        self.Loops = []
        LineNum = 0
        lineTxt = ""
        FileLength = len(FileTxt)
        while LineNum < FileLength:
            lineTxt = FileTxt[LineNum].lower().strip()
            if len(lineTxt) <1:
                pass # skip
            elif lineTxt[0] == '#':
                pass  # skips comment lines
            elif "resistor" in lineTxt:
                LineNum = self.MakeResistor(LineNum, FileTxt)
            elif "source" in lineTxt:
                LineNum = self.MakeVSource(LineNum, FileTxt)
            elif "loop" in lineTxt:
                LineNum = self.MakeLoop(LineNum, FileTxt)
            LineNum+=1
        pass

    def MakeResistor(self, N, Txt):
        """
        Make a resistor object from reading the text file
        :param N: (int) Line number for current processing
        :param Txt: [string] the lines of the text file
        :return: a resistor object
        """
        R =Resistor()  # instantiate a new resistor object
        N += 1  # <Resistor> was detected, so move to next line in Txt
        txt =Txt[N].lower()   # retrieve line from Txt and make it lower case using Txt[N].lower()
        while "resistor" not in txt:
            if "name" in txt:
                R.Name = txt.split('=')[1].strip()
            if "resistance" in txt:
                R.Resistance = float(txt.split('=')[1].strip())
            N+=1
            txt=Txt[N].lower()

        self.Resistors.append(R)  # append the resistor object to the list of resistors
        return N

    def MakeVSource (self, N, Txt):
        """
        Make a voltage source object from reading the text file
        :param N: (int) Line number for current processing
        :param Txt: [string] the lines of the text file
        :return: a voltage source object
        """
        VS=VoltageSource()
        N+=1
        txt = Txt[N].lower()
        while "source" not in txt:
            if "name" in txt:
                VS.Name = txt.split('=')[1].strip()
            if "value" in txt:
                VS.Voltage = float(txt.split('=')[1].strip())
            if "type" in txt:
                VS.Type = txt.split('=')[1].strip()
            N+=1
            txt=Txt[N].lower()

        self.VSources.append(VS)
        return N

    def MakeLoop(self, N, Txt):
        """
        Make a Loop object from reading the text file
        :param N: (int) Line number for current processing
        :param Txt: [string] the lines of the text file
        :return: a resistor object
        """
        L=Loop()
        N+=1
        txt = Txt[N].lower()
        while "loop" not in txt:
            if "name" in txt:
                L.Name = txt.split('=')[1].strip()
            if "nodes" in txt:
                txt=txt.replace(" ","")
                L.Nodes = txt.split('=')[1].strip().split(',')
            N+=1
            txt=Txt[N].lower()

        self.Loops.append(L)
        return N

    def AnalyzeCircuit(self):
        """
        Uses fsolve to solve for the unknown currents such that Kirchhoff's Voltage and Current Laws are satisfied.

        For the network:
          - I1 flows through resistors 'ad' and 'bc'.
          - I2 flows through resistor 'ce'.
          - I3 flows through resistor 'cd'.
          - Kirchhoff's Current Law (KCL) at node c ensures I1 + I2 - I3 = 0.

        :return: List of currents [I1, I2, I3].
        """
        # need to set the currents to that Kirchoff's laws are satisfied
        i0 =[1.0, 1.0, 1.0]  # initial guess for [I1, I2, I3]  #define an initial guess for the currents in the circuit
        i = fsolve(self.GetKirchoffVals,i0)
        # print output to the screen
        print("I1 = {:0.1f}".format(i[0]))
        print("I2 = {:0.1f}".format(i[1]))
        print("I3 = {:0.1f}".format(i[2]))
        return i

    def GetKirchoffVals(self,i):
        """
        This function uses Kirchoff Voltage and Current laws to analyze this specific circuit
        KVL:  The net voltage drop for a closed loop in a circuit should be zero
        KCL:  The net current flow into a node in a circuit should be zero
        :param i: a list of currents relevant to the circuit
        :return: a list of loop voltage drops and node currents
                For Network 1, the assignments are as follows:
          - I1 flows in resistors 'ad' and 'bc'
          - I2 flows in resistor 'ce'
          - I3 flows in resistor 'cd'
        The node equation at node c is: I1 + I2 - I3 = 0.
        """
        # set current in resistors in the top loop.
        self.GetResistorByName('ad').Current=i[0]  #I_1 in diagram
        self.GetResistorByName('bc').Current=i[0]  #I_1 in diagram
        self.GetResistorByName('cd').Current=i[2]  #I_3 in diagram
        #set current in resistor in bottom loop.
        self.GetResistorByName('ce').Current=i[1]  #I_2 in diagram
        #calculate net current into node c
        Node_c_Current = sum([i[0],i[1],-i[2]])

        # Get the KVL equations from the loop definitions in the file
        KVL = self.GetLoopVoltageDrops()   # returns a list of voltage residuals for each loop
        KVL.append(Node_c_Current)    # append the node current equation residual
        return KVL

    def GetElementDeltaV(self, name):
        """
        Retrieves the voltage drop (or rise) for an element (resistor or voltage source) by name.

        :param name: The element's name identifier.
        :return: The voltage change (float) with appropriate sign.
        """
        for r in self.Resistors:
            if name == r.Name:
                return -r.DeltaV()
            if name[::-1] == r.Name:
                return -r.DeltaV()
        for v in self.VSources:
            if name == v.Name:
                return v.Voltage
            if name[::-1] == v.Name:
                return -v.Voltage

    def GetLoopVoltageDrops(self):
        """
        This calculates the net voltage drop around a closed loop in a circuit based on the
        current flowing through resistors (cause a drop in voltage regardless of direction of traversal) or
        the value of the voltage source that have been set up as positive based on the direction of traversal.
        :return: net voltage drop for all loops in the network.
        """
        loopVoltages=[]
        for L in self.Loops:
            # Traverse loops in order of nodes and add up voltage drops between nodes
            loopDeltaV=0
            for n in range(len(L.Nodes)):
                if n == len(L.Nodes)-1:
                    name = L.Nodes[0] + L.Nodes[n]
                else:
                    name = L.Nodes[n]+L.Nodes[n+1]
                loopDeltaV += self.GetElementDeltaV(name)
            loopVoltages.append(loopDeltaV)
        return loopVoltages

    def GetResistorByName(self, name):
        """
        Retrieves a resistor object by its name.

        :param name: The identifier of the resistor.
        :return: The corresponding Resistor object, or None if not found.
        """
        for r in self.Resistors:
            if r.Name == name:
                return r
        return None
    #endregion

class ResistorNetwork_2(ResistorNetwork):
    #region constructor
    """
    A subclass of ResistorNetwork that represents the modified circuit with an additional
    resistor in parallel with the 32V source. This class overrides certain methods to account for
    the fixed current through the additional branch.
    """
    def __init__(self):
        super().__init__()  # runs the constructor of the parent class
        #region attributes
        #endregion
    #endregion

    #region methods
    def AnalyzeCircuit(self):
        """
        Override AnalyzeCircuit for the modified circuit.
        We still solve for [I1, I2, I3] in the main branches,
        but the node equation is altered because of the parallel resistor.
        """
        i0 = [1.0, 1.0, 1.0]  # initial guess remains three unknowns
        i = fsolve(self.GetKirchoffVals, i0)
        print("I1 = {:0.1f}".format(i[0]))
        print("I2 = {:0.1f}".format(i[1]))
        print("I3 = {:0.1f}".format(i[2]))
        return i


    def GetKirchoffVals(self,i):
        """
        Override the base method to account for the extra resistor in parallel with the
        32V source. We assume:
          - I1 flows in 'ad' and 'bc'
          - I2 flows in 'ce'
          - I3 flows in 'cd'
        In addition, the resistor in parallel with the voltage source (named 'de_r')
        carries a fixed current given by Ohm's law:
            I_de_r = 32V / 5Ω = 6.4 A.
        Thus, at the relevant node (here node c is used as before) the current balance becomes:
            I1 + I2 - I3 - I_de_r = 0.
        """
        # assign currents to main branches as before
        self.GetResistorByName('ad').Current = i[0]
        self.GetResistorByName('bc').Current = i[0]
        self.GetResistorByName('cd').Current = i[2]
        self.GetResistorByName('ce').Current = i[1]
        # Fixed current through the additional resistor branch:
        I_de_r = 32.0 / 5.0  # 6.4 A

        # Modify the node equation to subtract the extra branch current
        Node_c_Current = i[0] + i[1] - i[2] - I_de_r

        # Use the same loop voltage drops as defined in the file.
        KVL = self.GetLoopVoltageDrops()
        KVL.append(Node_c_Current)
        return KVL
    #endregion
#endregion

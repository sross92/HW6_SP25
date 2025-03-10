#Built off Dr.Smay's criteria and Stem Files
#Used ChatGPT for debugging assistance and logic check
from Steam import steam

class rankine():
    def __init__(self, p_low=8, p_high=8000, t_high=None, name='Rankine Cycle'):
        '''
        Constructor for rankine power cycle.  If t_high is not specified, the State 1
        is assigned x=1 (saturated steam @ p_high).  Otherwise, use t_high to find State 1.
        :param p_low: the low pressure isobar for the cycle in kPa
        :param p_high: the high pressure isobar for the cycle in kPa
        :param t_high: optional temperature for State1 (turbine inlet) in degrees C
        :param name: a convenient name
        '''
        self.p_low=p_low
        self.p_high=p_high
        self.t_high=t_high
        self.name=name
        self.efficiency=None
        self.turbine_work=0
        self.pump_work=0
        self.heat_added=0
        self.state1=None
        self.state2=None
        self.state3=None
        self.state4=None

    def calc_efficiency(self):
        #calculate the 4 states
        #state 1: turbine inlet (p_high, t_high) superheated or saturated vapor
        if(self.t_high==None):
            self.state1 = steam(self.p_high, x=1, name='Turbine Inlet') # instantiate a steam object with conditions of state 1 as saturated steam, named 'Turbine Inlet'
        else:
            self.state1= steam(self.p_high, T=self.t_high, name='Turbine Inlet') # instantiate a steam object with conditions of state 1 at t_high, named 'Turbine Inlet'
        #state 2: turbine exit (p_low, s=s_turbine inlet) two-phase
        # At the low pressure, use the turbine inlet entropy (s) to determine the state
        self.state2=self.state2 = steam(self.p_low, s=self.state1.s, name='Turbine Exit') # instantiate a steam object with conditions of state 2, named 'Turbine Exit'
        #state 3: pump inlet (p_low, x=0) saturated liquid
        self.state3=steam(self.p_low, x=0, name='Pump Inlet') # instantiate a steam object with conditions of state 3 as saturated liquid, named 'Pump Inlet'
        #state 4: pump exit (p_high,s=s_pump_inlet) typically sub-cooled, but estimate as saturated liquid
        self.state4=steam(self.p_high,s=self.state3.s, name='Pump Exit')
        # Estimate pump exit enthalpy: h4 = h3 + v3*(p_high - p_low)
        self.state4.h=self.state3.h+self.state3.v*(self.p_high-self.p_low)

        self.turbine_work=self.state1.h - self.state2.h # Calculate turbine work (in kJ/kg).
        self.pump_work=self.state4.h - self.state3.h # Calculate pump work (in kJ/kg).
        self.heat_added=self.state1.h - self.state4.h  # Calculate the heat added in the boiler (in kJ/kg).
        self.efficiency=100.0*(self.turbine_work - self.pump_work)/self.heat_added # Cycle thermal efficiency (percentage).
        return self.efficiency

    def print_summary(self):

        if self.efficiency==None:
            self.calc_efficiency()
        print('Cycle Summary for: ', self.name)
        print('\tEfficiency: {:0.3f}%'.format(self.efficiency))
        print('\tTurbine Work: {:0.3f} kJ/kg'.format(self.turbine_work))
        print('\tPump Work: {:0.3f} kJ/kg'.format(self.pump_work))
        print('\tHeat Added: {:0.3f} kJ/kg'.format(self.heat_added))
        self.state1.print()
        self.state2.print()
        self.state3.print()
        self.state4.print()

def main():
    rankine1=rankine(p_low=8, p_high=8000, t_high=None, name='Cycle with Saturated Vapor') #Instantiate a Rankine cycle with saturated vapor at the turbine inlet.
    #t_high is specified
    #if t_high were not specified, then x_high = 1 is assumed
    eff=rankine1.calc_efficiency()
    print(eff)
    rankine1.print_summary()

if __name__=="__main__":
    main()
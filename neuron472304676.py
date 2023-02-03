'''
Defines a class, Neuron472304676, of neurons from Allen Brain Institute's model 472304676

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472304676:
    def __init__(self, name="Neuron472304676", x=0, y=0, z=0):
        '''Instantiate Neuron472304676.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472304676_instance is used instead
        '''
            
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Sst-IRES-Cre_Ai14_IVSCC_-173196.03.01.01_397206096_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
    
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472304676_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 30.79
            sec.e_pas = -85.9110921224
        
        for sec in self.axon:
            sec.cm = 1.92
            sec.g_pas = 0.000605958787892
        for sec in self.dend:
            sec.cm = 1.92
            sec.g_pas = 2.15844763942e-07
        for sec in self.soma:
            sec.cm = 1.92
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 0.000207396
            sec.gbar_NaV = 0.0773339
            sec.gbar_Kd = 4.00587e-05
            sec.gbar_Kv2like = 0.211796
            sec.gbar_Kv3_1 = 0.589116
            sec.gbar_K_T = 0.018146
            sec.gbar_Im_v2 = 0.000232013
            sec.gbar_SK = 0
            sec.gbar_Ca_HVA = 9.0187e-05
            sec.gbar_Ca_LVA = 0.00548619
            sec.gamma_CaDynamics = 0.0446558
            sec.decay_CaDynamics = 753.913
            sec.g_pas = 0.000856643
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)


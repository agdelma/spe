import numpy as np

# load an ascii .spe file as exported from DAVE2 or DAVE1 software for the 
# reduction, visualization and analysis of inelastic neutron scattering data.
def load_file(file_name):
    ''' input:  file_name of the .spe file
        output: Q-vectors
                Energies
                Scattering intensity
                Error in scattering intensity
    '''
    
    with open(file_name) as in_file:
        data_line = in_file.readline()
        header = data_line.split()
        num_E,num_Q = int(header[0]),int(header[1])

        # Get the Q-values
        data_line = in_file.readline()
        data_line = in_file.readline()
        Q = []
        while data_line[0] != '#':
            Q += [float(cdata) for cdata in data_line.split()]
            data_line = in_file.readline()

        # Now get the E-values
        data_line = in_file.readline()
        E = []
        while data_line[0] != '#':
            E += [float(cdata) for cdata in data_line.split()]
            data_line = in_file.readline()

        # Now we go through appending to either S or ΔS
        S,ΔS = [],[]

        data_line = in_file.readline()
        while data_line:

            cS = []
            while data_line[0] != '#':
                cS += [float(cdata) for cdata in data_line.split()]
                data_line = in_file.readline()
            S.append(cS)

            data_line = in_file.readline()

            cΔS = []
            while data_line and data_line[0] != '#':
                cΔS += [float(cdata) for cdata in data_line.split()]
                data_line = in_file.readline()
            ΔS.append(cΔS)

            if not data_line:
                break
            else:
                data_line = in_file.readline()
        
    return np.array(Q[:-1]),np.array(E[:-1]),np.array(S),np.array(ΔS)

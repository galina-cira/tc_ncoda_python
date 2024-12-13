import numpy as np
import os

class ReadNcoda3D:

    def __init__(self):
        self.M = 2161
        self.N = 1051
        self.L = 34
        self.pre_reclen = self.M * self.N * self.L * 4  # record length in bytes
        self.rmiss2 = -9999.9
        self.imiss = 9999

    def read_ncoda_3d(self, fndata):
        open3d_err = self.imiss
        read3d_err = self.imiss
        data_3d = np.full((self.M, self.N, self.L), self.rmiss2, dtype=np.float32)

        if not os.path.exists(fndata):
            print("3d_data: ERROR: file {} does not exist!".format(fndata))
            return None, open3d_err, read3d_err

        lcheck = os.path.getsize(fndata)

        if lcheck < self.pre_reclen:
            print("3d_data: ERROR: file size is smaller than pre_reclen!: {}   {}".format(fndata, lcheck))
            return None, open3d_err, read3d_err

        print("Reading file {}".format(fndata))

        try:
            with open(fndata, "rb") as file:
                data_3d = np.fromfile(file, dtype='>f4')
                data_3d = data_3d.reshape((self.L, self.N, self.M))  # change the order here
                data_3d = np.transpose(data_3d, (2, 1, 0))  # transpose the data to get the correct order
                open3d_err = 0
                read3d_err = 0
        except Exception as e:
            print("Data: Error reading file: {}".format(fndata))
            print(str(e))
            return None, open3d_err, read3d_err

        # Replace values close to -999.0 with NaN
        data_3d[np.isclose(data_3d, -999.0, atol=1e-6)] = np.nan

        if open3d_err != 0:
            print("Data: Error opening file: {}".format(fndata))
            return None, open3d_err, read3d_err

        if read3d_err != 0:
            print("Data: Error reading file: {}".format(fndata))
            return None, open3d_err, read3d_err

        return data_3d, open3d_err, read3d_err


# Example usage
if __name__ == "__main__":
    reader = ReadNcoda3D()
    fndata = "ncoda.dat"
    data_3d, open3d_err, read3d_err = reader.read_ncoda_3d(fndata)

    if data_3d is not None:
        print(data_3d)


import numpy as np
import os

class ReadNcodaLonLat:
    def __init__(self):
        self.M = 2161
        self.N = 1051
        self.sfc_reclen = self.M * self.N * 4  # record length in bytes
        self.rmiss = -999.9
        self.rmiss2 = -9999.9
        self.imiss = 9999

    def read_ncoda_lon(self, fnlon):
        open_lon_err = self.imiss
        read_lon_err = self.imiss
        data_2d_lon_deg = np.full((self.M, self.N), self.rmiss, dtype=np.float32)

        if not os.path.exists(fnlon):
            print("Lon: Error: file {} does not exist!".format(fnlon))
            return None, open_lon_err, read_lon_err

        lcheck = os.path.getsize(fnlon)

        if lcheck < self.sfc_reclen:
            print("Lon: Error: file size is smaller than sfc_reclen!: {}   {}".format(fnlon, lcheck))
            return None, open_lon_err, read_lon_err

        try:
            with open(fnlon, "rb") as file:
                data_2d_lon_deg = np.fromfile(file, dtype='>f4')
                data_2d_lon_deg = data_2d_lon_deg.reshape((self.N, self.M))  # change the order here
                data_2d_lon_deg = np.transpose(data_2d_lon_deg, (1, 0))  # transpose the data to get the correct order
                
                open_lon_err = 0
                read_lon_err = 0
        except Exception as e:
            print("Lon: Error reading file: {}".format(fnlon))
            print(str(e))
            return None, open_lon_err, read_lon_err

        if open_lon_err != 0:
            print("Lon: Error opening file: {}".format(fnlon))
            return None, open_lon_err, read_lon_err

        if read_lon_err != 0:
            print("Lon: Error reading file: {}".format(fnlon))
            return None, open_lon_err, read_lon_err

        return data_2d_lon_deg, open_lon_err, read_lon_err

    def read_ncoda_lat(self, fnlat):
        open_lat_err = self.imiss
        read_lat_err = self.imiss
        data_2d_lat_deg = np.full((self.M, self.N), self.rmiss, dtype=np.float32)

        if not os.path.exists(fnlat):
            print("Lat: Error: file {} does not exist!".format(fnlat))
            return None, open_lat_err, read_lat_err

        lcheck = os.path.getsize(fnlat)

        if lcheck < self.sfc_reclen:
            print("Lat: Error: file size is smaller than sfc_reclen!: {}   {}".format(fnlat, lcheck))
            return None, open_lat_err, read_lat_err

        try:
            with open(fnlat, "rb") as file:
                data_2d_lat_deg = np.fromfile(file, dtype='>f4')
                data_2d_lat_deg = data_2d_lat_deg.reshape((self.N, self.M))  # change the order here
                data_2d_lat_deg = np.transpose(data_2d_lat_deg, (1, 0))  # transpose the data to get the correct order
                open_lat_err = 0
                read_lat_err = 0
        except Exception as e:
            print("Lat: Error reading file: {}".format(fnlat))
            print(str(e))
            return None, open_lat_err, read_lat_err

        if open_lat_err != 0:
            print("Lat: Error opening file: {}".format(fnlat))
            return None, open_lat_err, read_lat_err

        if read_lat_err != 0:
            print("Lat: Error reading file: {}".format(fnlat))
            return None, open_lat_err, read_lat_err

        return data_2d_lat_deg, open_lat_err, read_lat_err


# Example usage
if __name__ == "__main__":
    reader = ReadNcodaLonLat()
    fnlon = "lon_file.dat"
    fnlat = "lat_file.dat"
    data_2d_lon_deg, open_lon_err, read_lon_err = reader.read_ncoda_lon(fnlon)
    data_2d_lat_deg, open_lat_err, read_lat_err = reader.read_ncoda_lat(fnlat)

    if data_2d_lon_deg is not None:
        print(data_2d_lon_deg)

    if data_2d_lat_deg is not None:
        print(data_2d_lat_deg)


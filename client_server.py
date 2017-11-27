from matplotlib import pyplot as plt

class ClientServer:

    def __init__(self):
        self.peer_list = [n for n in range(0, 100, 5)]
        self.bitrate_server_in_bits = 12582912 # * 8 bits
        self.file_size_in_bits = 2147483648 *8 # *8 voor bits
        self.download_speed_peers = 1048576

    def calculate_client_server_distribution_time(self):
        distribution_time_list = []

        for i in range(0, len(self.peer_list)):
            if i == 0:
                distribution_time_list.append(0)
            else:
                #bit_rate = self.bitrate_server_in_bits / i
                distribution_time = (i * self.file_size_in_bits) / self.bitrate_server_in_bits
                distribution_time_list.append(distribution_time)
        print(distribution_time_list)
        return distribution_time_list

    def calculate_peer_to_peer_distribution_time(self, upload_speed):
        upload_speed_in_bits = upload_speed * 1024
        distribution_time_list = []

        for i in range(0, len(self.peer_list)):
            if i == 0:
                distribution_time_list.append(0)
            else:
                distribution_time = (i * self.file_size_in_bits) / (self.bitrate_server_in_bits + (upload_speed_in_bits * i))
                distribution_time_list.append(distribution_time)

        return distribution_time_list
    def plot_graph(self):
        fig, ax = plt.subplots()

        ax.grid(True)  # set grid

        plt.xlabel('amount of peers')
        plt.ylabel('distribution time(s)')

        ax.plot(self.peer_list, self.calculate_client_server_distribution_time(), label='client_server') #blauwe lijn

        ax.plot(self.peer_list, self.calculate_peer_to_peer_distribution_time(100), color='y', label='p2p-100Kbps') #gele lijn
        ax.plot(self.peer_list, self.calculate_peer_to_peer_distribution_time(300), color='g', label='p2p-300Kbps') #groene lijn
        ax.plot(self.peer_list, self.calculate_peer_to_peer_distribution_time(600), color='r', label='p2p-600Kbps') #rode lijn
        ax.legend()
        plt.show()
c = ClientServer()
c.plot_graph()

from matplotlib import pyplot as plt

class ClientServer:

    def __init__(self):
        self.peer_list = [n for n in range(0, 100, 5)]
        self.bitrate_server_in_bits = 12582912 # * 8 bits
        self.file_size_in_bits = 2147483648 *8 # *8 voor bits

    def calculate_client_server_distribution_time(self):
        distribution_time_list = []

        for i in range(0, len(self.peer_list)):
            if i == 0:
                distribution_time_list.append(0)
            else:
                bit_rate = self.bitrate_server_in_bits / i
                distribution_time = self.file_size_in_bits/ bit_rate
                distribution_time_list.append(distribution_time)
        print(distribution_time_list)
        return distribution_time_list

    def plot_graph(self):
        fig, ax = plt.subplots()

        ax.grid(True)  # set grid

        ax.plot(self.peer_list, self.calculate_client_server_distribution_time())

        plt.show()
c = ClientServer()
c.plot_graph()
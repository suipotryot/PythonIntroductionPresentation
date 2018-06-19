class DataHandler:

    data = []

    def fetch_data(self):
        DataHandler.data = []
        with open("electrical_consumption.data", "r") as data_file:
            data_raw = data_file.read()
            for row in data_raw.split("\n"):
                cells = row.split("|")
                DataHandler.data.append([cell.strip() for cell in cells if cell != ''])

if __name__ == "__main__":
    data_handler = DataHandler()
    data_handler.fetch_data()

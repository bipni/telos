class BubbleSort:

    @staticmethod
    def sort(data_list = [], method = 'asc'):

        if len(data_list) == 0:
            return []

        for i in range(len(data_list)):
            for j in range(0, len(data_list) - i - 1):
                if method == 'asc':
                    if data_list[j] > data_list[j+1]:
                        temp = data_list[j]
                        data_list[j] = data_list[j+1]
                        data_list[j+1] = temp
                elif method == 'desc':
                    if data_list[j] < data_list[j+1]:
                        temp = data_list[j]
                        data_list[j] = data_list[j+1]
                        data_list[j+1] = temp
                else:
                    raise Exception("Wrong Argument")

        return data_list

def run():
    return BubbleSort.sort()